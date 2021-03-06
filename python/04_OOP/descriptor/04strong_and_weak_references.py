# Strong and Weak references

import ctypes
def ref_count(address):
    return ctypes.c_long.from_address(address).value

class Person:
    pass

#______________________________________________________________________________________________
# strong references:

p1 = Person()    # p1 = <__main__.Person object at 0x000001>
# p1 is a strong reference to that Person object instance.

id_p1 = id(p1)   # 0x000001
ref_count(id_p1) # 1

p2 = p1          # p2 = <__main__.Person object at 0x000001>
# p2 is also a strong referencee to that same Person object instance.

p1 is p2         # True
ref_count(id_p1) # 2

# they both are strong references to that Person object instance at 0x000001.


# now if we try to delete p1 or p2 (doesnt matter which one), the Person object instance 
# wont be destroyed cause we still have a strong reference (p1) to that Person object 
# instance at 0x000001.
del p2

# that Person object instance still there, Python doesnt garbage collected it:
ref_count(id_p1) # 1

# Python will not garbage collect an object which reference count is not 0.

# if we delete p1 as well, it wont have strong references to that Person instance anymore:
del p1

ref_count(id_p1) # 0
# the object instance at 0x000001 was garbage collected at this point now.

ref_count(id_p1) # 23889287412394846 


# that's the problem we faced in our data descriptor. we had a strong reference to the 
# Point2D object instance inside the descriptor instance namespace (dictionary).


#_______________________________________________________________________________________________
# weak references:

# think of it as a reference to an object that does not affect the reference count.

# first, we should have a strong reference to some object:
p1 = Person()  # <__main__.Person object at 0x000001>
id_p1 = id(p1) # 0x000001

# then we can make a weak reference to that same object:
import weakref

w1 = weakref.ref(p1) # type(w1) <class 'weakref'>
# obs: while ref() is running, we do have another strong reference to p1, but, by the time 
# the ref() returns, that reference is gone.

ref_count(id_p1)     # 1
# it references the object but doesnt increment the number of references of that object.

# the weakref instance (w1) isnt the same object as p1:
w1 is p1  # False

w1 # <weakref at 0x000002; to 'Person' at 0x000001>
# it shows the weakref instance and the object that is pointing to.


# we can also get the object that w1 is pointing to. the weakref object instance 
# is a callable, we just need to call it:
w1()      # <__main__.Person object at 0x000001>

# Python checks if that object still around or not. if is there, it returns the object.
# but if the object has been garbage collected, it returns None instead.

# we can create another strong reference to an object if we store that returned object:
p2 = w1()        # p2 = <__main__.Person object at 0x000001>
ref_count(id_p1) # 2

# now we would have to delete both strong references (p1, p2) to destroy the Person object:
del p2
ref_count(id_p1) # 1

# weak references doesnt affect the number of reference counts.
# so, whenever we delete the last strong reference of an object, the reference count 
# will be 0. and once it happen, the object will be garbage collected:
del p1
ref_count(id_p1) # 0


# that weak reference will be considered "dead" now cause that object was garbage collected:
w1    # <weakref at 0x000002; dead>

# if we try to access that old Person object by calling the weakref instance:
w1()  # None   it returns None.


# we can also use weak references to track if a particular object still alives or not. cause
# weak references will automatically be updated to show us that the object is "dead", 
# meaning that the object is gone.

#_________________________________________________________________________________________________
# most of the builtin types dont support weak references. 

# we cant create a weak reference that points to a list, dict, int, etc:
# weakref.ref([1, 2, 3])   # cannot create weak reference to 'list' object
# weakref.ref({'age': 26}) # cannot create weak reference to 'dict' object
# weakref.ref(123)         # cannot create weak reference to 'int'  object


#_________________________________________________________________________________________________
p1 = Person()     # <__main__.Person object at 0x000001>
ref_count(id_p1)  # 1

# the hole problem we had was, if we store p1 as a key in our dictionary we would increment 
# the number of reference counts of that object. 

# using the traditional dictionary would creates a strong reference to p1:
data = {p1: 'Fabio'}

# now we have p1 and an entry in 'data' dict pointing to that Person object at 0x000001:
ref_count(id_p1)  # 2    

del data
ref_count(id_p1)  # 1

#_________________________________________________________________________________________________
# WeakKeyDictionary
# weakref provides a specialized kinda of dictionary that allow us to store weak references 
# to objects that are ment to be keys inside our dictionary.

# first we create the WeakKeyDictionary and then, when we store a custom object as key, 
# it will automatically be a weak reference to that particular object:
d = weakref.WeakKeyDictionary() 
d # <WeakKeyDictionary at 0x19189bced30>

# adding a new entry to the WeakKeyDicionary: 
d[p1] = 'Fabio'
# the key inside our WeakKeyDictionary was made into a weak reference to that p1 object.
# the important thing to be aware is that, our custom objects must be hashable. otherwise,
# we wouldnt be able to store then as key.

# now it does not affect the reference count anymore:
ref_count(id_p1)   # 1


# we can see the number of weak references some object has by using the getweakrefcount():
weakref.getweakrefcount(p1)  # 1


# creating another weak reference to p1:
d2 = weakref.WeakKeyDictionary()
d2[p1] = 'Giu'

weakref.getweakrefcount(p1)  # 2


# somehow Python is tracking the number of weak references to the objects. the way
# Python stores this information its actually storing it in the object instance itself.

# whenever we call the getweakrefcount(p1) it will go and look inside __weakref__ property:
p1.__weakref__  # <weakref at 0x000002; to 'Person' at 0x000001> its a Double Linked List.

# we can easily see the weak references objects inside our WeakKeyDictionary 
# by using keyrefs():
p1              # <__main__.Person object at 0x000001>
d.keyrefs()     # [<weakref at 0x000002; to 'Person' at 0x000001>]


# if we delete the last strong reference, the object will be garbage collected:
del p1

# and by the way weak references works, once that weak reference goes "dead", Python will 
# automatically removes that entry from the WeakKeyDictionary:
d.keyrefs()     # []


# for our data descriptor, instead of storing the object as key, we could store a 
# weak reference to the object. it will take care of memory leak we had with that approach.


# as we saw early, most of the builtin types dont support weak references. so we can only
# use keys in the WeakKeyDictionary that Python can creates weak references to.

# we cannot do it for exemple:
d = weakref.WeakKeyDictionary()
# d['Python'] = '3.7'   # TypeError: cannot create weak reference to 'str' object


# our custom classes do support weak references. but the object must be hashable:
class Person:
    pass

p = Person()   # hash(p) 138227236858

# the Person object is hashable, so we can create weak references to it:
d = weakref.WeakKeyDictionary()
d[p] = 'Fabio'
d.keyrefs()    # [<weakref at 0x000002; to 'Person' at 0x000001>]


# lets implement the __eq__ and disable Python default hash functionality:
class Person:
    def __eq__(self):
        pass

p = Person()      # hash(p)  TypeError: unhashable type: 'Person'

# we are no longer able to make weak references to Person objects:
d = weakref.WeakKeyDictionary()
# d[p] = 'Fabio'  # TypeError: unhashable type: 'Person'


# NOTE: if we are iterating over the WeakKeyDictionary views the dictionary can change size
# and the program may raise an exception.

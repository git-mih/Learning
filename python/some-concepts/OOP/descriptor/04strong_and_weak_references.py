# Strong and Weak references

import ctypes
def ref_count(address):
    return ctypes.c_long.from_address(address).value

class Person:
    pass

#______________________________________________________________________________________________
# strong references:

p1 = Person() # p1 = <__main__.Person object at 0x000001>
# p1 is a reference to that Person object instance.

print(ref_count(id(p1))) # 1

p2 = p1       # p2 = <__main__.Person object at 0x000001>
# p2 is also a referencee to that same Person object instance.

p1 is p2      # True
print(ref_count(id(p1))) # 2

# they both are Strong references to that Person object instance.


# now if we try to delete p1 or p2 reference (doesnt matter which one), 
# the Person object instance wont be destroyed cause we still have a strong reference (p2) 
# to that Person object instance.
del p2

print(ref_count(id(p1))) # 1
# the Person object is still there, so Python doesnt garbage collect it.


# Python wont garbage collect an object which reference count is not 0.

# so now, if we delete p2, it wont have more strong references to that Person object. it will
# then be destroyed by GC.

# that's the problem we faced in our data descriptor. we had a strong reference to the 
# Point2D object instance inside the descriptor instance dictionary.

#_______________________________________________________________________________________________
# weak references:

# think of it as a reference to an object that does not affect the reference count as far as the
# memory manager is concerned.

# its a reference to the object but it doesnt count, doesnt increment the number of references
# of the object.

# we should have a strong reference pointing to some object first. 
# and then we can have a weak reference thats point to that same object.
# meaning that we can still get the object from the weak reference without affecting the 
# reference counter of that object.
# whenever we delete the strong reference, the reference count will be 0 cause the weak reference
# doesnt affect it. and then the object is going to be destroyed by Python GC.

# the weak reference will be considered "dead" after it. if we try to use it now, Python will
# tell us that we cant, that object was gone.

# so, for our data descriptor, instead of storing the object as key, we going to store a weak
# reference to the object. it will take care of the memory leak we had with that approach.

# use the weakref module
import weakref
p1 = Person() # p1 has a strong reference to the object
p2 = weakref.ref(p1) # p2 will be a weak reference to p1
# NOTE: while ref() is running, we will have another strong reference to p1. but by the time
# the ref() returns, that reference is gone.

# also, p2 is now a callable. and if we call p2() it will then retursn the original object.
# this is how we get to the object that p2 points to __weakref__. we just call p2(). then
# Python go in and determine if that object still around or is gone. if stills there, it
# returns the original object or it will return None if the object has been garbage collected.

# we should be careful, cause we can create another strong reference to an object by mistake
# if we assign a reference to the p2(), like:

p3 = p2()  
p3  # <__main__.Person object at 0x000001>
# we just created a strong reference to the object. now we would have to delete p1 and p3
# to destroy the object.


# dictionaries of weak references:
# so, we will want to create a dictionary of weak references for our keys inside the data
# descriptor.

# we could do that manually with regular dictionaries.
# but instead, weakref has a WeakKeyDictionary to do just that for us.

p1 = Person()  # p1 is a strong reference to the Person object instance.

d = weakref.WeakKeyDictionary() # <WeakKeyDictionary at 0x242fab29e50>
d[p1] = 'some value'

next(d.items())   # (<__main__.Person object at 0x000001>, 'some value')

# and now if we delete p1, we will no longer have strong references. object will be GC:
del p1

# the item will automatically be removed from the dictionary.
# we are using weak references as key dictionary and once that weak reference goes "dead", 
# Python will automatically removes that from the dictionary. that is cool.

# should be careful. if we are iterating over the dictionary views cause the dictionary will
# change size and the program may raise an exception.

#_______________________________________________________________________________________________

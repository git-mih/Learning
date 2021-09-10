# Back to instance properties

import ctypes
from os import access

def ref_count(address):
    return ctypes.c_long.from_address(address).value

#_______________________________________________________________________________________________
# we could use the WeakKeyDictionary approach to solve that issue, but it will only works 
# for hashable objects.
import weakref

class IntegerValue:
    def __init__(self):
        # the only difference is that, we are using a WeakKeyDictionary now.
        self.wd = weakref.WeakKeyDictionary()
    
    def __set__(self, instance, value):
        self.wd[instance] = int(value)

    def __get__(self, instance, owner_class):
        if instance is None:
            return self
        return self.wd.get(instance)

class Point:
    # creating the descriptor instance with a WeakKeyDictionary inside it:
    x = IntegerValue()

Point.x.__dict__     # {'wd': <WeakKeyDictionary at 0x000002>}
Point.x.wd           # <WeakKeyDictionary at 0x000002>

# WeakKeyDictionary is empty right now.
Point.x.wd.keyrefs() # []

p = Point() # <__main__.Point object at 0x000001>

# adding a entry inside the WeakKeyDictionary:
p.x = 100

# and when we try to retrieve it:
p.x  # 100

# essentially Python looks inside the descriptor instance namespace:
Point.x.wd[p] # 100


# now we have a weak reference to p inside the descriptor instace namespace:
Point.x.wd.keyrefs() # [<weakref at 0x000002; to 'Point' at 0x000001>]

# now if we delete the strong reference (p), Python will automatically remove 
# that entry from the WeakKeyDictionary:
del p

# we no longer have strong references to that Person object at 0x000001. The object was GC.
Point.x.wd.keyrefs() # []


# but the problem is, it only works for hashable objects. but this approach works almost ever.

#___________________________________________________________________________________________________
# lets try to address the hashability issue now

# since we can not use the object itself as the key in our dictionary, we could use only the
# id of the object which is just an fixed int value as the key inside some regular dictionary:
class IntegerValue:
    def __init__(self):
        self.d = {}
    
    def __set__(self, instance, value):
        # not storing strong references to objects anymore. just storing the id:
        self.d[id(instance)] = int(value)

    def __get__(self, instance, owner_class):
        if instance is None:
            return self
        # get the object based on id of that particular object:
        return self.d.get(id(instance))

class Point:
    x = IntegerValue()

    # implementing __eq__ just to remove Python default hash functionality:
    def __eq__(self, other):
        pass

# simulating what Python will essentyally do:
p1 = Point() # <__main__.Point object at 0x000001> // id(p1) 2564209427168 // <class 'int'>
p2 = Point() # <__main__.Point object at 0x000002> // id(p2) 2564209427120 // <class 'int'>

d = {id(p1): p1, id(p2): p2} 
# d = {2564209427168: <__main__.Point object at 0x000001>,   id(p1) -> p1
#      2564209427120: <__main__.Point object at 0x000002>}   id(p2) -> p2


# back to the descriptor instance namespace now:
p = Point() #  1534789861968  (id)

id_p = id(p)
ref_count(id_p) # 1

# storing a entry inside the descriptor namespace (dictionary):
p.x = 100
# now lets see the descriptor instance namespace (dictionary):
Point.x.d   # {1534789861968: 100}

# destroying the last strong reference to Person object:
del p
ref_count(id_p) # 0

# this will works just fine, but once the garbage collector destroy the object, that 
# key will still be there. we gonna still having a "dead" entry inside the dictionary:
Point.x.d   # {1534789861968: 100}


#___________________________________________________________________________________________________
# we need a way to determine if the object was gone. 
# if we can do that, then we can also go in and remove his entry (id of that object) 
# from the dictionary. 
# we know that weak references are somehow aware of it.

# whenever we creates a weak reference, there is an additional parameter that we can specify 
# for a callback function. this is going to be a function that is gonna get called whenever
# the entry becomes "dead":
def fn(obj):
    print(f'{obj} is being destroyed')

p = Point()
w = weakref.ref(p, fn)

# lets make the Point object instance be destroyed:
del p     # <weakref at 0x000001CF22422F90; dead> is being destroyed
# function fn was called as soon that the entry of the WeakKeyDictionary became "dead".
# and is important to know that, was the weakref object instance that was passed to the fn.
# it doesnt receive the object that was destroyed! 

# the only thing that we can know is that, that particular weakref object became "dead". 
# but we can still make use of that. 
# we can use this callback function to remove that id issue we had:
class IntegerValue:
    def __init__(self):
        self.d = {}
    
    def __set__(self, instance, value):
    # we still gonna use the id of the object instance as key. but now we gonna store
    # a weak reference as well, just so we can register a callback function to clean up
    # that id entry in the dictionary once the weak reference goes dead.
        self.d[id(instance)] = (weakref.ref(instance, self._fn) , int(value))
    # now, whenever we require to return a value, we have to use the 2nd element of 
    # the tuple. the 1st element will just track if the object was gone or not.

    def _fn(self, weak_ref): # weak_ref = <weakref at 0x000002; dead>

        # we still have that id key entry:
        # Point.x.d    {1990946690912: (<weakref at 0x000002; dead>, 100)}
        dead_entry = [k for k, v in self.d.items() if v[0] is weak_ref] 
        # dead_entry = [1990946690912]
        if dead_entry:          # if there is a dead_entry:
            key = dead_entry[0] # we store the id value (1990946690912) and
            del self.d[key]     # delete this key from the descriptor instance dict

        # or we could do this way tho:
        # for k, v in d.items():
        #     if v[0] is weak_ref:
        #         del self.d[k]
        #         break

    def __get__(self, instance, owner_class):
        if instance is None:
            return self
        return self.d.get(id(instance))[1] # <<   getting 2nd element of the tuple

class Point:
    x = IntegerValue()

p = Point()
id_p = id(p)  # 1990946690912

# adding a entry to the descriptor namespace (dictionary):
p.x = 100

# essentially:
IntegerValue.__set__(Point.x, p, 100) 

Point.x.d # {1990946690912: (<weakref at 0x000002; to 'Point' at 0x000001>, 100)}
# the id of p is the key that is just an integer value: 1990946690912.

# the value is a tuple, where the 1st element is the weak reference that tracks if p is there 
# or not and the 2nd value of the tuple is the value stored itself (100).


# whenever we try to access it, Python will essentially do:
p.x  # 100
IntegerValue.__get__(Point.x, p, Point)
Point.x.d[id(p)][1] # 100

# the weak reference is there just to track the p object:
Point.x.d[id(p)][0] # <weakref at 0x000002; to 'Point' at 0x000001>

# we have an entry inside the descriptor instance namespace:
Point.x.d # {1990946690912: (<weakref at 0x000002; to 'Point' at 0x000001>, 100)}

# if we destroy the last strong reference, the weak refence will realize the object was gone
# and will trigger the _fn function:
del p 
# the _fn receives the weakref instance:  <weakref at 0x000002; dead>


# if an object is garbage collected at some point, the corresponding entry will not be in the 
# descriptor instance dictionary anymore. the callback function _fn will removes that 
# key entry (id) from the descriptor instance:
Point.x.d # {}

#__________________________________________________________________________________________________
# but there is one last caveat. when we create weak references to the objects, the weak
# reference instances are actually stored in the object instances itself inside a property
# called __weakref__.
class Person:
    pass

Person.__dict__ #   {'__weakref__': <attribute '__weakref__' of 'Person' objects>, ...}

# the __weakref__ is technicaly a data descriptor:
hasattr(Person.__weakref__, '__get__') # True
hasattr(Person.__weakref__, '__set__') # True

# therefore, Person object instances will also have that property __weakref__:
p = Person()  # <__main__.Person object at 0x000001>
hasattr(p, '__weakref__') # True


# we can look what is in there currently:
p.__weakref__ # None

# there is no weak references to p yet, lets create it:
w = weakref.ref(p)

# now we have a weak reference to that Person object instance:
p.__weakref__ # <weakref at 0x000002; to 'Person' at 0x000001>



# the problem is, if we use slots, we gonna lose the __dict__ and __weakref__, the 
# object instances will no longer have that attribute __weakref__ as well:
class Person:
    __slots__ = 'name',

# we no longer have __dict__ and __weakref__:
Person.__dict__
# {'__module__': '__main__', 
#  '__slots__' : ('name',), 
#  'name'      : <member 'name' of 'Person' objects>, 
#  '__doc__'   : None}


# and we are no longer able to create weak references now:
p = Person()
hasattr(p, '__dict__')    # False
hasattr(p, '__weakref__') # False

# w = weakref.ref(p) #  TypeError: cannot create weak reference to 'Person' object

#__________________________________________________________________________________________________
# we could fix it by adding the attribute __weakref__ into our slots:
class Person:
    __slots__ = 'name', '__weakref__'

p = Person()       # <__main__.Person object at 0x000001>

# now we can create a weak reference to that Person object instance:
w = weakref.ref(p) # <weakref at 0x000002; to 'Person' at 0x000001>


# so if we want to use data descriptors by using weak references using our own regular
# dictionaries or WeakKeyDictionary with classes that implement __slots__, we will need to
# make sure to add __weakref__ to the slots.

class ValidString:
    def __init__(self, min_length=0, max_length=255):
        self.data = {}
        self._min_length = min_length
        self._max_length = max_length
    
    def __set__(self, instance, value):
        if not isinstance(value, str):
            raise ValueError('Value must be a string.')
        if len(value) < self._min_length:
            raise ValueError(f'Value should be at least {self._min_length} characters.')
        if len(value) > self._max_length:
            raise ValueError(f'Value cant exceed {self._max_length} characters.')
        # if value is valid, then we store it inside self.data dictionary:
        self.data[id(instance)] = (weakref.ref(instance, self._fn), value)

    def __get__(self, instance, owner_class):
        if instance is None:
            return self
        value_tuple = self.data[id(instance)]
        # getting the 2nd element of the tuple:
        return value_tuple[1] 

    def _fn(self, weak_ref):
        dead_entry = [k for k, v in self.data.items() if v[0] is weak_ref]
        if dead_entry:
            key = dead_entry[0]
            del self.data[key]

class Person:
    __slots__ = '__weakref__',

    first_name = ValidString(1, 100)
    last_name = ValidString(1, 100)

    def __eq__(self, other):
        return (
            isinstance(other, Person) and
            self.first_name == other.first_name and
            self.last_name == other.last_name
        )

class BankAccount:
    __slots__ = '__weakref__', 

    account_number = ValidString(5, 255)

    def __eq__(self, other):
        return isinstance(other, BankAccount) and self.account_number == other.account_number

p1, p2 = Person(), Person()
p1.first_name, p1.last_name = 'Fabio', 'machado'
p2.first_name, p2.last_name = 'Eric', 'idle'

b1 = BankAccount()
b1.account_number = 'Cheking...'

p1.first_name, p1.last_name # Fabio machado
p2.first_name, p2.last_name # Eric idle

b1.account_number           # Cheking...

Person.first_name.data
# {2236011111111: (<weakref at 0x000001111; to 'Person' at 0x000001>, 'Fabio'), 
#  2236022222222: (<weakref at 0x000002222; to 'Person' at 0x000002>, 'Eric')}

Person.last_name.data
# {2236011111111: (<weakref at 0x000003333; to 'Person' at 0x000001>, 'machado'), 
#  2236022222222: (<weakref at 0x000004444; to 'Person' at 0x000002>, 'idle')}

BankAccount.account_number.data
# {2236033333333: (<weakref at 0x000005555; to 'BankAccount' at 0x000003>, 'Cheking...')}

del p1
del p2
del b1

Person.first_name.data          # {}
Person.last_name.data           # {}
BankAccount.account_number.data # {}

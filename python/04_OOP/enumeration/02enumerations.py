# Python enumerations

# enumerations are created by subclassing the Enum class. which is going to generate a lot of 
# related stuffs for us behind the scenes.

#_______________________________________________________________________________________________________
import enum

class Color(enum.Enum):
# the Color class is called enumeration. and Color.RED is called an enumeration member.
    RED = 1
    GREEN = 2
    BLUE = 3

type(Color)      # <class 'enum.EnumMeta'>

# if Color was a regular class without inheriting from Enum, Color.RED would be just a
# class attribute that points to the integer instance 1.


# but the type of the member objects is the enumeration that it belongs to. 
# what happens is that, whenever a class inherit from Enum, all class attributes will become 
# references to object instances of the enumeration class itself.

type(Color.RED)  # <enum 'Color'>    object instance of Color class.


# is important to know that, the member associated values can be of any data type:
class Status(enum.Enum):
    # strings
    PENDING = 'pending'
    RUNNING = 'running'
    COMPLETED = 'completed'

class UnitVector(enum.Enum):
    # tuples
    V1D = (1, )  
    V2D = (1, 1)
    V3D = (1, 1, 1)

# essentially, even though the Color.RED points to the integer instance '1', some 
# metaprogramming implementation will make that Color.RED points to a object instance of the 
# Color class:
isinstance(Color.RED, Color)          # True
isinstance(Status.PENDING, Status)    # True
isinstance(Status.PENDING, enum.Enum) # True


# representation of the members:
str(Status.PENDING)  # 'Status.PENDING'
repr(Status.PENDING) # <Status.PENDING: 'pending'>       | <member: associated_value>


# the Enum class adds new properties that can return the name of the member in string and
# also the member associated value:
Color.RED.name       # 'RED'
Color.BLUE.value     # 3

UnitVector.V3D.name  # 'V3D'
UnitVector.V3D.value # (1, 1, 1)


# we can do member equality by using the identity operator (is) to compare members:
Color.RED is Color.RED  # True
Color.RED is Color.BLUE # False
# the (==) works but we realy should use (is), is faster and we could modify the (==)
# by implementing __eq__

# note that, members objects and its associated value are not equal anymore:
Color.RED == 1    # False


# enumerations dont have comparision by default:
class Constants(enum.Enum):
    ONE = 1
    TWO = 2

# Constants.ONE < Constants.TWO 
# TypeError: '<' not supported between instances of 'Constants' and 'Constants'


# we can also use membership operator:
Status.PENDING in Status # True

Status.PENDING.name  # 'PENDING'
Status.PENDING.value # 'pending'
# note that, we dont have these strings inside the Status enumeration:
# 'PENDING' in Status.PENDING    # TypeError: argument of type 'Status' is not iterable


# to get a member by value is very simple, enumerations are callables. we can lookup a 
# member by passing a value and get the respective member object:
Status('pending')  # Status.PENDING
UnitVector((1, ))  # UnitVector.V1D
Color(3)           # Color.Blue

# but if we try to lookup an invalid value:
# Status('invalid')    # ValueError: 'invalid' is not a valid Status


# enumerations implements __getitem__ method:
hasattr(Status, '__getitem__')  # True

# it means that we can lookup and get a member by using his name:
Status['PENDING']  # Status.PENDING

# we can also use the getattr() if we want an functional approach:
getattr(Status, 'PENDING')             # Status.PENDING
getattr(Status, 'xyz', Status.RUNNING) # Status.RUNNING


# enumeration member objects are always hashables. the Enum class is responsible to do it.
class Person:
    __hash__ = None

p = Person()
# hash(p)   # TypeError: unhashable type: 'Person'

class Family(enum.Enum):
    person_1 = Person()  # members are hashables. the associative values are Person instances
    person_2 = Person()  # that are unhashable objects.

# the associated value is unhashable:
# hash(Family.person_1.value)  # TypeError: unhashable type: 'Person'

# but the member object itself is hashable:
hash(Family.person_1) # -7047559212361810963

# so we can use members as keys in the a set or dictionary:
d = {Family.person_1: 'Fabio', 
     Family.person_2: 'John'}

# {<Family.person_1: <__main__.Person object at 0x000001>>: 'Fabio', 
#  <Family.person_2: <__main__.Person object at 0x000002>>: 'John'}


# enumerations are essentially iterables as well: 
hasattr(Status, '__iter__') # True

# we can loop through it:
for member in Status:
    repr(member)

# <Status.PENDING: 'pending'>
# <Status.RUNNING: 'running'>
# <Status.COMPLETED: 'completed'>

# we can iterate and store the member objects in a list:
list(Status)
# [<Status.PENDING: 'pending'>, <Status.RUNNING: 'running'>, <Status.COMPLETED: 'completed'>]

# ordering is defined based on the same order that they were defined in the enumeration.
# is important to know that, the order is not based on the value.


# enumerations are immutables. we cant modify the associative values inside the enumerations
# essentially, we cant modify the object that the members are pointing to.

# Status.PENDING.value = 10  # AttributeError: can't set attribute
# Status['NEW'] = 100        # TypeError: 'EnumMeta' object does not support item assignment

# and we cannot add or remove elements inside enumerations:
class EnumBase(enum.Enum):
    ONE = 1 # member defined

# class EnumExt(EnumBase):   # TypeError: EnumExt: cannot extend enumeration 'EnumBase'
#     TWO = 2  

# we cant, cause we defined a member at the EnumBase enumeration.

# but, if we dont define any member object, we can inherit it:
class EnumBase(enum.Enum):
    pass

# now we could inherit that BaseEnum enumeration and define the member here:
class EnumExt(EnumBase):
    ONE = 1 # member defined

#_______________________________________________________________________________________________________
# why we have two ways of referencing members ny name? like:
Status.PENDING    # Status.PENDING
Status['PENDING'] # Status.PENDING

# suppose we have a JSON:
import json

payload = """{"name": "Alex", "status": "PENDING"}"""

# deserializing that:
data = json.loads(payload)
data # {'name': 'Alex', 'status': 'PENDING'}

# checking:
Status[data['status']]  # Status.PENDING


# enumerations also have a third property called __members__ that returns a mapping proxy 
# with all member objects and their associated values:
Status.__members__ 
# {'PENDING': <Status.PENDING: 'pending'>, 
#  'RUNNING': <Status.RUNNING: 'running'>, 
#  'COMPLETED': <Status.COMPLETED: 'completed'>}

# we can use it to get members as well:
Status.__members__['PENDING']   # Status.PENDING
Status.__members__['PENDING'] is Status.PENDING  # True

# the easiest way of checking if some string correspond to some member in our enumeration is
# by using the membership operation:
'PENDING' in Status.__members__ # True
'OK' in Status.__members__      # False

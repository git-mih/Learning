# Customizing and extending enumerations

# Enumerations are just regular classes. and the class attributes of the enumeration class 
# will become object instances of that same class, they become members.

#____________________________________________________________________________________________________________
import enum

# enumerations are essentially regular classes, that means, we could define functions inside 
# the enumeration class:
class Color(enum.Enum):
    # red, green and blue became members. they are object instances of the Color class itself:
    red = 1   # <enum 'Color'> 
    green = 2 # <enum 'Color'>
    blue = 3  # <enum 'Color'>

    def purecolor(self, value):
        return {self: value} # {<Color.red: 1>: 255}

# the 'purecolor' is just a regular function inside the enumeration class (Color):
Color.purecolor     # <function Color.purecolor at 0x000001>

# members are instances of the class itself essentially. therefore, functions will be bound 
# to the instances.
# it means that we can create our custom methods and add then to the enumeration. 
# we can also implement/overwrite dunder methods, like: __str/repr/eq/bool__ etc...

# the 'purecolor' function will become a method bound to the instances:
Color.red.purecolor # <bound method Color.purecolor of <Color.red: 1>>

# and we can call it:
Color.red.purecolor(255) # {<Color.red: 1>: 255}

# essentially Python will do it:
Color.purecolor(Color.red, 255) # {<Color.red: 1>: 255}


# we can also overwrite the default dunder methods:
class Color(enum.Enum):
    red = 1  
    green = 2 
    blue = 3

    def __str__(self):
        return f'{self.name} ({self.value})'

Color.blue  # blue (3)


# enumerations dont have ordering by default, but we could implement it:
class Number(enum.Enum):
    ONE = 1
    TWO = 2

    def __lt__(self, other):
        return isinstance(other, Number) and self.value < other.value

    def __eq__(self, other):
        if isinstance(other, Number):
            return self is other  # Number.ONE == Number.TWO
        elif isinstance(other, int):
            return self.value == other # Number.ONE.value == 1
        return False

# now we have ordering defined:
Number.ONE < Number.TWO  # True

# we can also compare members with integers:
Number.ONE == 1          # True
Number.ONE == Number.ONE # True
Number.ONE == 'one'      # False

# the problem is that, we no longer have member objects being hashables:
# hash(Number.ONE)    TypeError: unhashable type: 'Number'

# if we want to use it inside dictionaries and sets, we would have to implement the __hash__.


# by default, every member of an enumeration is truthy, irrespective of the member value.
class State(enum.Enum):
    READY = 1  # bool(State.READY)  True
    BUSY = 0   # bool(State.BUSY)   True

# we can implement the __bool__ method to override this behavior:
class State(enum.Enum):
    READY = 1
    BUSY = 0

    def __bool__(self): 
        return bool(self.value) # bool(State.READY.value) // bool(1) essentially.

state = State.READY

if state:  # True
    print('system ready to process next item')
else:      # False
    print('system is busy')

#____________________________________________________________________________________________________________
# extending enumerations:
# enumerations are classes, so they can be extended (subclassed) essentially. but, as we saw, 
# we can only do it if they dont contain any members defined.

# it might seems to be limiting, but is quite useful to be able to define some functionality 
# inside some base class enumeration just once and reuse it whenever we want:
class ColorBase(enum.Enum):
    def hello(self):
        return f'{self} says hello'

# then we can extend that functionality and define the members itself inside a subclass:
class Color(ColorBase):
    RED = 'red'
    GREEN = 'green'
    BLUE = 'blue'

Color.RED.hello()  # Color.RED says hello

# another exemple:
from functools import total_ordering

@total_ordering
class OrderedEnum(enum.Enum):
    def __lt__(self, other):
        if isinstance(other, OrderedEnum):
            return self.value < other.value 
        return NotImplemented

# by subclassing the enum base class (OrderedEnum) we can get its functionalities:
class Number(OrderedEnum):
    ONE = 1
    TWO = 2
    THREE = 3
class Dimension(OrderedEnum):
    D1 = 1,
    D2 = 1, 1
    D3 = 1, 1, 1

Number.ONE < Number.TWO  # True
Dimension.D2 > Dimension.D3  # False


#______________________________________________________________________________________________________
# multiples associated values:

# the http module contains an enumeration class called HTTPStatus:
from http import HTTPStatus

type(HTTPStatus)  # <class 'enum.EnumMeta'>

# first 5 members of the HTTPStatus enumeration:
list(HTTPStatus)[0:5]
# [<HTTPStatus.CONTINUE: 100>, 
#  <HTTPStatus.SWITCHING_PROTOCOLS: 101>, 
#  <HTTPStatus.PROCESSING: 102>, 
#  <HTTPStatus.EARLY_HINTS: 103>, 
#  <HTTPStatus.OK: 200>]

# known properties:
HTTPStatus.OK.name  # OK
HTTPStatus.OK.value # 200

# we can lookup for a member by value:
HTTPStatus(200)  # HTTPStatus.OK

# HTTPStatus enum class also have a property called 'phrase' that provides a friendly message:
HTTPStatus.NOT_FOUND.phrase  # Not Found

#______________________________________________________________________________________________________
# as we can see, there is more than 1 associated value with each member in this enumeration.

# lets implement it ourselves:
class AppStatus(enum.Enum):
    # member associated values is going to be a tuple with N values:
    OK = 0, 'No problem ath all'
    FAILED = 1, 'crap!!'  

# looking up the member:
repr(AppStatus.OK)    # <AppStatus.OK: (0, 'No problem ath all')>
AppStatus.OK          # AppStatus.OK

# member default properties:
AppStatus.OK.name     # OK
AppStatus.OK.value    # (0, 'No problem at all')

# we require to use the indexing approach to get the value for the tuple:
AppStatus.OK.value[1] # No problem at all
# isnt a good approach tho.


# to solve that, we could create a properties that will return the tuple values:
class AppStatus(enum.Enum):
    OK = 0, 'No problem at all'  
    FAILED = 1, 'crap!!'          

    @property
    def code(self):
        return self.value[0] # AppStatus.OK.value[0]   # 0

    @property
    def phrase(self): 
        return self.value[1] # AppStatus.OK.value[1]   # 'No problem at all' 

# now it will work properly:
AppStatus.OK.code   # 0
AppStatus.OK.phrase # No problem at all

# but if we try to access the property 'value', we still gonna get the tuple back:
AppStatus.OK.value  # (0, 'No problem at all')

# another problem is that, with the HTTPStatus we could get a member object by his value like:
HTTPStatus(200) # HTTPStatus.OK

# but we cant do it cause our enumeration member associated values are tuples:
# AppStatus(1)   # ValueError: 1 is not a valid AppStatus


# in order to get the member object by value, we would have to lookup for the tuple itself 
# which represents a particular member:
AppStatus((0, 'No problem at all')) # AppStatus.OK

# that is not user friendly.

#______________________________________________________________________________________________________
# to fix that we could use the __new__ method:
class AppStatus(enum.Enum):
    OK = 0, 'No problem at all'  
    FAILED = 1, 'crap!!'          

    def __new__(cls, member_value, member_phrase):
    # the __new__ must return a member object, it must return an instance of AppStatus.

    # how we can instantiate AppStatus being inside the class itself?
    # we cant call the AppStatus cause it will call the __new__ recursively. instead, 
    # we can call the __new__ method of the object class. the __new__ method in the 
    # object class receives the class that we want to create an instance:
        member = object.__new__(cls) 
        # 'member' points to an AppStatus object instance now.

        # now we just require to add the 'value' and 'phrase' attributes inside the member:
        member._value_ = member_value 
        # '_value_' is a special attribute that is actually the 'value'.

        member.phrase = member_phrase

        # member now have the 'value' and 'phrase' attributes defined, we just require to
        # return this member object:
        return member
            # essentially it will do it:
            # OK = object.__new__(AppStatus, 0, 'No problem at all')   # <enum 'AppStatus'>
            # OK._value_ = 0
            # OK.phrase = 'No problem at all'
            # return OK   (return the object instance of AppStatus)

# when AppStatus get compiled, our __new__ method will overwrite the __new__ of the Enum class. 
# our __new__ will get called for each AppStatus class attribute and return member objects.


# we could not lookup for a member based on its value cause we had a tuple before. 
# but we can do it now:
AppStatus(1)  # AppStatus.FAILED

# Enumerations introduction, why would we want to use it?

# how do we deal with a collection of related constants? 
# inside our module we could basicly define a bunch of symbols and assign some values:
STATUS_STARTED = 'started'
STATUS_PENDING = 'pending'
STATUS_ERROR = 'error'
STATUS_OK = 'ok'

# and then group then all together using a list or tuple:
STATUSES = [STATUS_STARTED, STATUS_PENDING, STATUS_ERROR, STATUS_OK]

# Essentially, Enumerations provides this functionality and a lot more related to it.
# the question is, why we may want enumerations? what special thing we gonna get of it?


#_________________________________________________________________________________________________
# to deal with a collection of related constants, we could try this approach:
RED = 1
GREEN = 2
BLUE = 3

COLORS = (RED, GREEN, BLUE)

# then we could use it inside a dictionary like:
pixel_color = {RED: 255, BLUE: 0, GREEN: 200} # {1: 255, 2: 0, 3: 200} essentially.

pixel_color[RED] # 255
pixel_color[1]   # 255


# there is a lot of downsides with that:
RED in COLORS    # True   ok.
1 in COLORS      # True   1 is really a COLOR?

# we also have operations such as ordering and multiplication defined:
RED < GREEN      # True      ??
RED * 2          # redred    meaningless...

# does the string 'red' correspond to a valid color name? we could do it:
RED = 'red'
GREEN = 'green'
BLUE = 'blue'

# works but it is repetitive and nothing stop us to possibly change it later:
RED = 'violet'

# we could have bugs by having non-unique values by mistake:
RED = 'red'
GREEN = 'red'
BLUE = 'blue'


# we shoud have more high-level control of these things

#_________________________________________________________________________________________________
# what we really want is something that provides an immutable collection of related constants.
# we want a collection to be immutable and we want the members to be constant values that 
# have unique names that may have meaning.

# we also want to have an associated constant value like, RED could be 1 or the string 'red'.
# but we want this to be constant and unique value.
# we should not be able to change its value later:  
RED = 'violet'
# and not beeing able to have duplicate associated values:  
RED = 'red'
GREEN = 'red'

# and probably operations such as multiplication or ordering should not be allowed:
RED * 2
RED < GREEN 

# we also need support to enumerating members by the name like, 'RED', 'GREEN' and 'BLUE'.

# also be able to lookup for member by using the name, like giving the string 'red' we should 
# be able to get the object RED. or maybe lookup the member by value and get the 
# corresponding member.

#_________________________________________________________________________________________________
# we could try to use a class to get some functionalities:
class Colors:
    RED = 1
    GREEN = 2
    BLUE = 3

# we have class attributes RED, GREEN and BLUE that have value associated. 

# now we can refer to it by using these class attributes:
Colors.RED  # 1

# we can also check to see if some particular string is an attribute of that class:
hasattr(Colors, 'RED') # True

# also beeing able to get the value:
getattr(Colors, 'RED') # 1


# but what if we look up for a member based on its value? suppose we ask for the value 2 and 
# we want to get the corresponding member (GREEN). we cant do it easily this way.

# and how do we iterate over the members? we could, but the order would not be guaranteed.

# also, we still not having uniqueness of the values with this approach. we could still make 
# the mistake of doing RED and GREEN = 1.

#_________________________________________________________________________________________________
# sometimes we also want a thing called aliases. 
# this is where we want multiple symbols to refer to the same "thing", the same element:

POLY_4 = 4
RECTANGLE = 4
SQUARE = 4
RHOMBUS = 4
# the main element in this collection is POLY_4. and all the other ones are actually aliases 
# to the POLY_4. they all are just different symbols that represents the same POLY_4 object.

# so whenever we lookup for the value 4, it will return the POLY_4 object. 
# same if we lookup for the name SQUARE, it will return the POLY_4 object as well.

# we want this kind of functionality and isnt easy to achieve by using our own classes.

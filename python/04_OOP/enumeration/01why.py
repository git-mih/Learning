# Enumerations introduction, why would we want to use it?

# how do we deal with a collection of related constants? 
# inside our module we could basicly define a bunch of symbols and assign some values:
STATUS_STARTED = 'started'
STATUS_PENDING = 'pending'
STATUS_ERROR = 'error'
STATUS_OK = 'ok'

# and then we group then all together using a list or tuple:
STATUSES = [STATUS_STARTED, STATUS_PENDING, STATUS_ERROR, STATUS_OK]

#_________________________________________________________________________________________________
# to deal with a collection of related constants, we could try this approach:
RED = 1
GREEN = 2
BLUE = 3

COLORS = (RED, GREEN, BLUE)

# then we could use it inside a dictionary like:
pixel_color = {RED: 255, BLUE: 0, GREEN: 200} # {1: 255, 2: 0, 3: 200} essentially.

# we can access the value by using the symbol:
pixel_color[RED] # 255

# but the symbol RED points to the integer object 1, so they both are the same, essentially:
RED == 1 # True

# and we could endup doing it as well:
pixel_color[1]   # 255

# we dont necessarily want this kind of behavior. there is a lot of downsides with that, like:
1 in COLORS      # True   1 is really a COLOR?

# operations such as ordering and multiplication:
RED < GREEN      # True
RED * 2          # redred    meaningless...


# to make the string 'red' correspond to a valid color name, we could do it:
RED = 'red'
GREEN = 'green'
BLUE = 'blue'

# works well but it is repetitive and nothing stop us to possibly change it later on, like:
RED = 'violet'

# we could potentialy have bugs by having non-unique values by mistake:
RED = 'red'
GREEN = 'red'
BLUE = 'blue'


# we shoud have more high-level control of these things

#_________________________________________________________________________________________________
# what we really want is something that provides an immutable collection of related constants.
# a immutable collection with constant element values that have unique names.

# we want to be able to lookup for a element by using his name, like giving the string 'RED', 
# we should be able to get the object that correspond to RED. or maybe lookup the element by 
# value and get the corresponding object.


# we could try to use a regular class to get some functionalities:
class Colors:
    RED = 1
    GREEN = 2
    BLUE = 3

# we have class attributes RED, GREEN and BLUE that have value associated. 

# now we can get then by using class attributes:
Colors.RED  # 1

# we can also check to see if some particular string is a class attribute:
hasattr(Colors, 'RED') # True

# and get the value:
getattr(Colors, 'RED') # 1


# but what if we look up for a member based on its value? suppose we ask for the value 2 and 
# we want to get the corresponding member GREEN. we cant do it easily this way.

# and how do we iterate over the members? we could, but the order would not be guaranteed.

# also, we still not having uniqueness values with this approach. we could still making the 
# mistake of doing RED and GREEN = 1.


# sometimes we also want a thing called aliases. 
# this is where we want multiple symbols to refer to the same "thing", the same element:
POLY_4 = 4
RECTANGLE = 4
SQUARE = 4
RHOMBUS = 4

# we want the main element in this collection to be POLY_4. and all the other ones to be 
# actually aliases to the POLY_4. 
# we want to be able to have different symbols that represents the same POLY_4 object.

# so whenever we lookup for the value 4, we want it to return the POLY_4 object.
# or if we lookup for the name SQUARE, it will return the POLY_4 object as well.

# we want this kind of functionality and isnt easy to achieve by using regular classes.

# Essentially, Enumerations provides these functionalities and a lot more related to it.

# Aliases

import enum

# member objects are guaranteed to be unique.

# members and their associated values should be unique. so this should not work essentially:
class Color(enum.Enum):
    red = 1  # master member
    crimson = 1 
    carmine = 1 

    blue = 2 # master member
    aquamarine = 2 

# but even though the red, crimson and carmine have different names, they have the same 
# associated value, they all are pointing to the same "master" member.

# in fact it works, we do have unique members there but now we also got aliases as well.

# essentially, our enumeration contains only two members. the "master" members:
Color.red        # Color.red
Color.blue       # Color.blue

# the remaining "members" are aliases that just points to these two "master" members:
Color.crimson    # Color.red
Color.carmine    # Color.red
Color.aquamarine # Color.blue

Color.crimson is Color.red  # True


# lookups with aliases will always return the "master" member:
Color(1)         # Color.red
Color['crimson'] # Color.red
# essentially, it will find the alias and then finds the "master" member of that alias.


# containment works the same:
Color.crimson in Color   # True


# iterating aliases:
# when we iterate over the members of an enumeration, we will only get the "master" members:
list(Color)  # [<Color.red: 1>, <Color.blue: 2>]


# only way to see the aliases is by using the __members__ property which returns 
# a mapping proxy that will contains the keys in string and the particular members as values:
Color.__members__
# {'red': <Color.red: 1>, 'crimson': <Color.red: 1>, 'carmine': <Color.red: 1>, 
#  'blue': <Color.blue: 2>, 'aquamarine': <Color.blue: 2>}

# note how the keys are different but they point to the same member.


# we may want to guarantee that our enumerations dont contain aliases and ensure unique values.
# enum provides a decorator that we can add to our enumaration and it will guarantee that we cant have 
# aliases in our enumeration:
@enum.unique
class Color(enum.Enum):
    red = 1
    crimson = 1  # alias

# whenever this enumeration class (Color) get compiled it will raises an exception:
# ValueError: duplicate values found in <enum 'Color'>: crimson -> red

# Automatic values

# its a way where Python can automaticaly assign values to member objects in our enumerations.

# we can use the 'auto()' function as member associated value to automaticaly assign a value.

import enum

class State(enum.Enum):
    WAITING = enum.auto() # called when the State class gets compiled.
    STARTED = enum.auto()
    FINISHED = enum.auto()

list(State) # [<State.WAITING: 1>, <State.STARTED: 2>, <State.FINISHED: 3>]

# we just require to be careful to not mix it with our own values:
class State(enum.Enum):
    WAITING = 100
    STARTED = enum.auto()
    FINISHED = enum.auto()

list(State) # [<State.WAITING: 100>, <State.STARTED: 101>, <State.FINISHED: 102>]

# that seems to work but we cant rely on that:
class State(enum.Enum):
    WAITING = enum.auto()  # 1
    STARTED = 1
    FINISHED = enum.auto() # 2

list(State) # [<State.WAITING: 1>, <State.FINISHED: 2>]

# the State.STARTED became a alias to State.WAITING member:
State.__members__ 
# {'WAITING': <State.WAITING: 1>, 'STARTED': <State.WAITING: 1>, 'FINISHED': <State.FINISHED: 2>}

#_____________________________________________________________________________________________________
# so how does this auto() function works? well, enumerations actually implement a static method 
# called _generate_next_value_:
hasattr(State, '_generate_next_value_')  # True

# this is the function that actually gets called when we use enum.auto(). it goes and find the
# _generate_next_value_ function in our class and calls it. 
# the returned value of _generate_next_value_ will be assigned to the member object.

# by default, the implementation of _generate_next_value_ results in sequential int numbers:
list(State) # [<State.WAITING: 1>, <State.STARTED: 2>, <State.FINISHED: 3>]

# we can overwrite it inside our enumeration class:
class State(enum.Enum):
    def _generate_next_value_(name, start, count, last_values):
        return 100

    A = enum.auto()
    B = enum.auto()
    C = enum.auto()

# arguments of the _generate_next_value_ function:
# name  = name of the member.
# start = only used in functional creation.
# count = is the number of members that was already created. including aliases.
# last_values = is a list that contains all the previous values that was already been assigned 
#               to the members. as we call the enum.auto(), this list will keep growing.

# essentially, it will happen for each member:
# name = 'A',   start = 1,   count = 0,   last_values = []
# A = 100

# name = 'B',   start = 1,   count = 1,   last_values = [100]
# B = 100

# name = 'C',   start = 1,   count = 2,   last_values = [100, 100]
# C = 100

#_____________________________________________________________________________________________________
# exemple by using the 'last_values' argument:
import random

class State(enum.Enum):
    def _generate_next_value_(name, start, count, last_values):
        while True:
            value = random.randint(1, 100)
            if value not in last_values:
                return value

    A = enum.auto()  # last_values = [].append(50)
    B = enum.auto()  # last_values = [50].append(98)
    C = enum.auto()  # last_values = [50, 98].append(34)
    D = enum.auto()  # last_values = [50, 98, 34].append(8)

list(State)  # [<State.A: 50>, <State.B: 98>, <State.C: 34>, <State.D: 8>]

#_____________________________________________________________________________________________________
# exemple by using the 'name' argument:
class State(enum.Enum):
    WAITING = 'waiting' 
    STARTED = 'started'   # having to write it again and again is really tedious.
    
# instead, we could do it:
class State(enum.Enum):
    def _generate_next_value_(name, start, count, last_values):
        return name.lower()
    # it will auto generate a string value of whatever 'name' the member have:

    WAITING = enum.auto() # name = 'WAITING'.lower()
    STARTED = enum.auto() # name = 'STARTED'.lower()

list(State)  # [<State.WAITING: 'waiting'>, <State.STARTED: 'started'>]

#_____________________________________________________________________________________________________
# suppose that we dont want the user to access a member by looking up the value:
class State(enum.Enum):
    """pls do not use member values - they are meaningless and it may change later on."""
    WAITING = 1
    STARTED = 2

# we specified that we should only get the members by his name:
State.WAITING    # State.WAITING
State['WAITING'] # State.WAITING

# but the problem is, the users could access the member by value, like:
State(1)   # State.WAITING


# and what will happen if we update the associated value of some member:
class State(enum.Enum):
    PREPARE = 1 # the value 1 is no longer associated with State.WAITING.
    WAITING = 2 
    STARTED = 3

# if someone was relying on value 1 to be the WAITING, now his code is broken:
State(1)   # State.PREPARE


# we may want to write our enumeration in such a way that they cant do that. we want to be
# able to use the enumeration but we are only interested in the member names, we are not 
# interested in the associated values, they have no meaning for us. we could do it instead:
class State(enum.Enum):
    # making the members associated values in a way that the user wont be able to recover it:
    PREPARE = object()
    WAITING = object()
    STARTED = object()

# our enumeration will still working just fine looking up by member names:
State.WAITING     # State.WAITING
State['WAITING']  # State.WAITING

# but the members associated values are meaningless now:
State.WAITING.value  # <object object at 0x000001>


#_____________________________________________________________________________________________________
# exemple by using the 'count' argument with aliases:
class Aliased(enum.Enum):
    def _generate_next_value_(name, start, count, last_valeus):
        return last_valeus[-1]
     # it will always create an alias to the last value of the list whenever auto gets called.

class Color(Aliased):
    RED = object()   # meaningless "master" member
    CRIMSON = enum.auto()
    CARMINE = enum.auto()

    BLUE = object()  # meaningless "master" member
    AQUAMARINE = enum.auto() 
    AZURE = enum.auto()      

# when we iterate the enumeration, we only see two "master" members:
list(Color) 
# [<Color.RED:  <object object at 0x000001>>, 
#  <Color.BLUE: <object object at 0x000002>>]

# the remaining members became aliases based on the last value of the 'last_values' list:
Color.__members__
# {'RED':     <Color.RED: <object object at 0x000001>>,
#  'CRIMSON': <Color.RED: <object object at 0x000001>>, 
#  'CARMINE': <Color.RED: <object object at 0x000001>>, 

#  'BLUE':       <Color.BLUE: <object object at 0x000002>>,
#  'AQUAMARINE': <Color.BLUE: <object object at 0x000002>>, 
#  'AZURE':      <Color.BLUE: <object object at 0x000002>>}

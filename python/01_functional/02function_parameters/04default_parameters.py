# Default parameters:

# what happens during run-time is that, when a module is loaded, all code on that particular 
# module is executed immediately. for exemple, if we have an variable assignement like:
a = 10

# whenever Python load the main module, it will essentially creates that integer object and 
# assign that reference `a` to that integer object.


# when we have a function defined, isnt different:
def f(a):
    # that integer object will be created only when we call the function. after it gets created,
    # then Python will assign `a` to that integer object in memory.
    return a

# whenever Python executes the `def` keyword, it will essentially creates that function object 
# in memory and reference to it with that `f` symbol.

# and by the time that function object is already defined, we can call it:
f(10)  # 10



# but what about the default values?
def f(a=10):
    return a

# in this case, that default value will be created during the function definition. it means that, 
# the integer object gets created and its reference `a` is assigned with the function object 
# itself. whenever Python reaches the `def` keyword, that integer object and its reference `a` 
# will be created. 

# the function itself isnt being executed, it is just being created. and if we defined a default
# parameter, it will be created as well.

# now if we executes that function object:
f() # 10

# by the time we call the function, that default value (integer object) has already been created 
# and assigned to `a`. 
# it will not re-evaluate again if we call that function again.


# using a callable as default parameter value:
from datetime import datetime

def log(msg, *, dt=datetime.utcnow()): # dt = 2021-08-20 12:45:26.842649: message 1...
    # dt will be created when Python runs the module and define the function object.
    return f'{dt}: {msg}'

# by the time we call the function, `dt` was already created:
log('message 1...') # 2021-08-20 12:45:26.842649: message 1...


# if we try to call it a few minutes later, that datetime object was already created. 
# it will not be re-define:
log('message 2...') # 2021-08-20 12:45:26.842649: message 2...

# a solution would be to explicitly creates the datetime object every time we call the function:
log('message 3...', dt=datetime.utcnow()) 
#                     2021-08-20 14:47:29.343843: message 3...


# instead, we could use a solution pattern where we set a default value to None:
def log(msg, *, dt=None):
    dt = dt or datetime.utcnow()
    # by doing that, we can test if we provided ourselves that optional argument. 
    # if not, it creates a new datetime object for every function call that we make.
    return f'{dt}: {msg}'

log('message 1...') # 2021-08-20 13:01:49.739602: message 1...

# few minutes later:
log('message 2...') # 2021-08-20 13:03:23.440531: message 2...

# and we can still providing our optional keyword argument:
log('message 3...', dt='20/04/95') # 20/04/95: message 3...


# NOTE: in general, beware of using mutable objects or callables as default parameters.

# realize that, it will not be called again once it has already created during compilation.
# if its a function that is supposed to change its value over the time, that will not happen.

# in the other hand, if we set a default parameter with is an mutable object, such as list,
# that indeed will be evaluated once, but now the default is poiting to a object that is 
# mutable in memory, which means that it can change:
def f(name, cards=[]):
    # we want a new empty list for every call we make, but this approach will keep appending
    # new elements inside that list.
    cards.append(name)
    return cards

f('dark')   # ['dark']
f('light')  # ['dark', 'light']
f('earth')  # ['dark', 'light', 'earth']
f('water')  # ['dark', 'light', 'earth', 'water']

def f(name, cards=None):
    if cards is None:
        cards = [] 
        # a new list will be created everytime we call the function and we dont provide an list.
    cards.append(name)
    return cards

f('dark')  # ['dark']
f('light') # ['light']

# providing an existent list now:
deck = []
f('fire', deck)
f('wind', deck)
deck       # ['fire', 'wind']

# another exemple:
def add_item(name, quantity, unit, grocery_list=[]): 
    # grocery_list will be created when Python load the main module. that is when the default
    # parameter is evaluated, it will be create once this function gets created during compilation.
    grocery_list.append(f'{name} - {quantity} {unit}') 
    return grocery_list

store_1 = add_item('banana', 4, 'units')
add_item('milk', 2, 'liters', store_1)

store_1 # ['banana - 4 units', 'milk - 2 liters']

# creating a new list by using our function:
store_2 = add_item('eggs', 12, 'units')
store_2 # ['banana - 4 units', 'milk - 2 liters', 'eggs - 12 units']

# that doesnt work properly, we have the itens from `store_1` on it. what about `store_1`:
store_1 # ['banana - 4 units', 'milk - 2 liters', 'eggs - 12 units']

# what we have in fact is that, they both share the same memory address, the same list:
store_1 is store_2  # True

# everytime we call `add_item()`, that default list object was already been created. that means,
# if we dont provide an list as argument, it will use that default list object.


# fixing it by setting the default parameter to None:
def add_item(name, quantity, unit, grocery_list=None): 
    if grocery_list is None:
        grocery_list = []
    grocery_list.append(f'{name} - {quantity} {unit}')
    return grocery_list

store_1 = add_item('banana', 4, 'units')
add_item('milk', 2, 'liters', store_1)  # store_1 = ['banana - 4 units', 'milk - 2 liters']

store_2 = add_item('eggs', 12, 'units') # store_2 = ['eggs - 12 units']

store_1 is store_2 # False
store_1 # ['banana - 4 units', 'milk - 2 liters']

# Mutability:

# consider an object in memory, it is basicly something that has a data type, internal state/data,
# and a memory address.

# whenever we change the data inside the object itself, we are essentially modifying the internal
# state of that particular object.

# an object whose internal state can be change is called: Mutable.
# and an object whose internal state cannot be changed is Immutable.

#   mutables:               immutables:
# lists                 # numbers (int, float, booleans, etc)
# sets                  # strings
# dictionaries          # tuples
# user-defined classes  # frozen sets
#                       # user-defined classes

# the tuple itself is immutable. and all the elements are integers, immutables as well:
t = (1, 2, 3)

# but now consider that we have a tuple with mutable elements:
t = ([1, 2], 3, [4, 5])

# we can insert elements inside the tuple elements that are mutables, such as list objects.
t[0].append(777)
t[2].append(999)

# the tuple itself still the same size, was indeed not mutated. but the element of the tuple is
# mutable and was mutated:
# t = ([1, 2, 777], 3, [4, 5, 999])

#____________________________________________________________________________________________________
# Function arguments and mutability 

# how our variables may or may not be affected by functions when we call them and pass these 
# variables as arguments.

# as we know, strings are immutable objects. once a string object has been created, the contents 
# of the object can never be changed.

# suppose that we have this variable:
a = 'hello'  # 0x000001

# the only way to modify the "value" of `a` is to re-assign `a` to another object:
a = 'world'  # 0x000002



# immutable objects are generally safe from unintended:
# whenever Python compile these lines of code, Python will stores it inside the module scope:
def f(arg):
    arg = arg + ' world'
    return arg

a = 'hello'

# module namespace:
globals() # {..., 'f': <function f at 0x000001>, 'a': 'hello'}


# whenever we call that function and pass our variable `a` as argument, we are actually passing
# its reference to that function:
f(a)  # f(0x000001)

# the function scope will stores that reference in the variable `arg`. therefore, `arg` is also
# referencing that 'hello' string object at 0x000001.

# now, whenever Python compiles that function body scope, it will actually creates that new 
# 'hello world' string object and `arg` will reference that.


# in the module scope, that `a` reference still pointing to that 'hello' object at 0x000001.
# and inside the function `f` scope, `arg` has now changed its reference to a new string object.

# we can see that `a` was not changed:
print(a) # hello


# mutable objects are not safe from unintended side-effects:
def f(l):
    l.append(777)

a = [1, 2, 3]  # 0x000001

f(a) # f(0x000001) passing the reference to the function essentially.

# `a` and `l` points to that same object, as we saw before. but, whenever Python compiles
# the function body scope, we are essentially mutating that object which both variables are
# referencing to.

# the memory address of that [1, 2, 3] list object stills the same, but we changed its state:
print(a) # [1, 2, 3, 777]
id(a)    # 0x000001

# same applies to immutable collection objects that contain mutable element objects.

#____________________________________________________________________________________________________
# Shared references and mutability

# the term shared reference is the concept of two variables sharing the same object in memory:
a = 10  # a = 0x000001
b = a   # b = 0x000001

# samething happen when we have a function, like:
def f(arg):
    arg = 10 # <'int' object at 0x000001>

a = 10       # <'int' object at 0x000001>

f(a)

# in fact, the following also share the same reference:
a = 10    # <'int' object at 0x000001>
b = 10    # <'int' object at 0x000001>

a = 'hey' # <'str' object at 0x000002>
b = 'hey' # <'str' object at 0x000002>

# Python memory manager decides to automatically re-use these memory references in order to 
# optimize performance.

# this is safe to do cause these objects are immutable essentially. so, even though they all
# shared share references, if we try to modify one of them, they will point to another object.
# there is no way of changing its internal state.


# but when we are working with mutable objects, we have to be more careful:
a = [1, 2, 3]  # <'list' object at 0x000001>
b = a          # <'list' object at 0x000001>

# they both share the same mutable object. therefore, if we modify its internal state:
b.append(777)

# both variables will be affected:
print(a) # [1, 2, 3, 777]   # <'list' object at 0x000001>


# but, with mutable objects Python will never create shared references this way:
a = [1, 2, 3] # <'list' object at 0x000001>
b = [1, 2, 3] # <'list' object at 0x000005>

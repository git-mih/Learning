# *args

# unpacking iterables recall:
a, b, c = (1, 2, 3)
a # 1
b # 2
c # 3

a, b, *c = 1, 2, 'fa'
a # 1
b # 2
c # ['f', 'a']

# something similar happens when positional arguments are passed to a function:
def f(a, b, c):
    # essentially:
    # a, b, c = (1, 2, 3)
    return a, b, c

f(1, 2, 3)


# in fact, functions also supports the * unpacking operator:
def f(a, b, *c):
    # essentially:
    # a, b, *c = 1, 2, 'fa'
    # a = 1 
    # b = 2
    # c = ('f', 'a')  `c` will collect the rest of the positional arguments that we passed in.
    return a, b, c 

f(1, 2, 'fa')

# note that, `c` is a tuple and not a list now, that is the minor difference.


# the * parameter name is arbitraty, but we usually call it *args:
def f(a, b, *args):
    pass

# is important to know that, *args will exhausts the remaining positional arguments. 
# it means that, we cannot add more positional arguments after we define the *args:
def f(a, b, *args, c):
    #essentially:
    # a = 10
    # b = 20
    # args = ('a', 'b', ???)
    # c = ???
    pass

# that function will compile, but whenever we try to call it:
# f(10, 20 ,'a', 'b', 100)   TypeError: f() missing 1 required keyword-only argument: 'c'


# we can also unpack arguments, like:
def f(a, b, c):
    # essentially:
    # a = 1
    # b = 2
    # c = 3
    return a, b, c

# we want to pass these elements of the list as arguments to that function:
l = [1, 2, 3]

# we can unpack the list first and then pass it to the function:
f(*l) # f(1, 2, 3)  it will essentially unpack before it assign to the function variables:

#_____________________________________________________________________________________________________
# Keyword arguments:

# positional parameters can optionally be passed as named (keyword) arguments as we know:
def f(a, b, c):
    return a, b, c

f(1, 2, 3)       # (1, 2, 3)
f(b=2, a=1, c=3) # (1, 2, 3)

# using named arguments in this case is entirely up to the caller. 

# but sometimes we may want to make these keyword arguments mandatory, and we can do it by 
# defining parameters after the positional parameters got exhausted:
def f(a, b, *args, d): # *args effectively exhausts all positional arguments.
    #essentially:
    # a = 1
    # b = 2
    # args = (3, 4, 5)
    # c = 6
    return a, b, args, d

# once we exhaust all positional arguments, we are only able to specify new arguments by using 
# keyword arguments. therefore, `c` must be passed as named (keyword) argument only:
f(1, 2, 3, 4, 5, d=6)
f(1, 2, d=3) # essentially:  a = 1, b = 2, args = (), c = 3


# we can omit any mandatory positional arguments:
def f(*args, a):
    # essentially:
    # args = (1, 2, 3)
    # a = 777
    return args, a

f(1, 2, 3, a=777)

# positional arguments are not required:
f(a=777) # essentially:  args = (), d = 777


# in fact, we can also force no positional arguments at all:
def f(*, d):
# * indicates the "end" of positional arguments we cant pass positional arguments anymore. 
# we are only able to specify keyword arguments.
    return d

f(d=777)  # 777

# putting it together:
def f(a, b=2, *, c, d=True):
    # a: mandatory positional argument
    # b: optional positional argument
    # *: no additional positional arguments allowed from here
    # c: mandatory keyword-only argument
    # d: optional keyword-only argument
    return a, b, c, d

f(1, c=2)  # (1, 2, 2, True)

#_____________________________________________________________________________________________________
# **kwargs

# *args is used for a variable number of additionals positional arguments which returns a tuple
# with all remaining positional arguments that were passed to the function.

# the **kwargs is kinda the same thing, but it is used to create dictionary with all remaining 
# keyword arguments instead. all remaining named arguments will be stored inside an dict object
# under the name of whatever variable we are using. we usually call it **kwargs.


# the important thing to notice is that, **kwargs can be specified even if the positional
# arguments have not been exhausted. 

# to use keyword-only arguments before, we had to exhaust all positional arguments by using *args. 
# but now we are no longer able to define parameters after the **kwargs:
def f(*, a, **kwargs):
    # *: no additional positional arguments allowed from here
    # a: mandatory keyword-only argument
    # **kwargs: additional keyword-only arguments

    # essentially:  
    # a = 1
    # kwargs = {'b': 2, 'c': 3, 'd', 4}
    return a, kwargs

f(a=1, b=2, c=3, d=4) 
f(a=777)  # essentially:  a = 777, kwargs = {}

def f(**kwargs):
    return kwargs

f() # kwargs = {}
f(name='fabio', age=26, city='POA') # kwargs = {'name': 'fabio', 'age': 26, 'city': 'POA'}


# we can also mix both, *args and **kwargs to be able to collect any number of positional args 
# and any number of named arguments as well:
def f(*args, **kwargs):
    # args = (1, 2, 3)
    # kwargs = {'a': 4, 'b': 5}
    return args, kwargs

f(1, 2, 3, a=4, b=5)
f() # args = (), kwargs = {}

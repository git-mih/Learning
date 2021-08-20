# Argument vs parameters:

# while defining some function, we are essentially specifying the 'parameters' of that function:
def f(a, b): 
    # `a` and `b` are variables that are local to its function body scope.
    pass


# whenever we call a function we are passing 'arguments' to it essentially:
x = 10
y = 20

f(x, y) 

# NOTE: important to remember is that, `x` and `y` are passed by reference.
# their memory addresses are passed to that function essentially.

#___________________________________________________________________________________________________
# positional arguments:
# the most common way of assigning arguments to parameters is via the order in which they are
# passed in. basicly their positions:
def f(a, b):
    return a - b

f(100, 200) # -100
#  a    b

# if we change order we may not get the same output:
f(200, 100) #  100
#  a    b


# default values:
# positional arguments can be made optional by specifying a default value for the corresponding
# parameter:
def f(a, b=777, c=999):
    # a: mandatory positional argument
    # b: optional positional or keyword argument
    # c: optional positional or keyword argument
    return a, b, c

# we are not required to specify the 2nd or 3rd argument to that function:
f(10)      # (10, 777, 999)
f(1, 2)    # (1, 2, 999)
f(1, 2, 3) # (1, 2, 3)


# but what if we want to specify `a` and `c` and use the default `b`? to that, we have to use
# keyword arguments, also called named arguments:
f(a=1, c=2) # (1, 777, 2)
f(1, c=2)   # (1, 777, 2)

# positional arguments can also be specified by using the parameter name wheter it have default 
# value or not:
def f(a, b, c):
    return a, b, c

# once we use a named argument, all arguments thereafter must be named arguments too:
f(c=10, a=20, b=30) # (20, 30, 10)
f(1, b=2, c=3)      # (1, 2, 3)

# we cant do it:  
# f(c=10, 20, 30)
# f(10, b=20, 30)


# we can specify positional-only arguments by using a '/' character after the number of positional 
# arguments required:
def f(a, b=777, /):
    # a: mandatory positional-only argument
    # b: optional positional-only argument
    return a, b
f(1)    # a = 1, b = 777
f(1, 2) # a = 1, b = 2
# f(1, b=2)  TypeError: f() got some positional-only arguments passed as keyword arguments: 'b'

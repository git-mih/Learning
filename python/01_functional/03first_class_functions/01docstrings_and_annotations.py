# Docstrings and annotations

# we can use docstrings and annotations inside our functions (modules, classes, etc) to provide 
# a better documentation. they are essentially just metadata, doesnt affecting how our code runs.

# Python doesnt really use docstrings or annotations. it is mainly used by external tools and modules. 
# for exemple, applications that generate documentation from our code. (like, sphinx)


# if the first line inside the function body is a string (not an assignement or a comment), 
# it will be interpreted as a docstring:
def f(a):
    "documentation..."
    return a

# docstrings are special types of comments, it gets compiled inside our code, and comments do not.
# most importantly, docstrings are used for documentation.

# we can see that by using the builtin `help` function:
help(f)
# Help on function f in module __main__:
# f(a)
#     documentation...


# we can also have multi-line docstrings by using multi-line strings:
def f(a, b):
    # this comment doesnt get compiled.
    """a: positional argument
       b: positional argument"""

# dosctrings gets compiled and they became part of our code. that comment doesnt.


# the function object provides a property called __doc__ which stores that docstring:
def fact(n):
    """factorial:
    inputs:
        n: non-negative integer
    returns:
        n!
    """

fact.__doc__   # type(fact.__doc__)  <'str' object>
# factorial:
#     inputs:
#         n: non-negative integer
#     returns:
#         n!


# external tools that are trying to create documentation of our code will use that __doc__ property
# to find it. same happens when we call the `help` function to get the documentation string.

#__________________________________________________________________________________________________________
# Function annotations:

# we also have another way of add documentation to our functions, by documenting the function 
# parameters essentially. we can document parameters of the function and its return value:

def f(a: 'a string', b: 'a positive integer') -> 'a string':
    return a * b

help(f) # f(a: 'a string', b: 'a positive integer') -> 'a string'
#             # notice that, comments right above the function will be displayed here.


# annotations can be any expression essentially:
def f(a: str, b: [1, 2, 3]) -> None:
    return None


# in fact, we can even call functions inside our annotations, since function calls are expressions:
x, y = 3, 777
def f(a: str) -> f'a repeated {max(x, y)} times':
    return a * str(max(x, y))

help(f) # f(a: str) -> 'a repeated 777 times'

# but is important to know that, like default parameters, same happens with annotations. 
# they get created when the function object gets evaluated. it means that, if later on we decide
# to change the values from `x` and `y`, that max return value may change. however, the annotation
# will not be updated cause it was already been evaluated during the function object creation:
x, y = 999, 3
help(f) # f(a: str) -> 'a repeated 777 times'   # it doesnt update.


# we can still use default values and *args, **kwargs:
def f(a: str = 'xyz', 
      *args: 'additional arguments',
      b: int = 1,
      **kwargs: 'additional keyword-only arguments') -> None:
    pass

help(f) 
# f(a: str = 'xyz', *args: 'additional arguments', b: int = 1, **kwargs: 'additional keyword-only arguments') -> None


# annotations get stored inside the __annotations__ property of the function: 
def f(a: 'info on a', b: int) -> float:
    pass

# stored as a dictionary where the keys are the parameter names and the values are the annotations itself:
f.__annotations__ # {'a': 'info on a', 'b': <class 'int'>, 'return': <class 'float'>}

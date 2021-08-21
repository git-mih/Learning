# Lambda expressions

# we can create functions using the `def` statement. but lambda expressions are another way of 
# creating function objects as well.

# syntax:  
# lambda [parameter_list]: return_value [, argument_list] -> function object

# parameters are optinal but the `:` is required. the `return_value` is evaluated and returned 
# when the lambda function object gets called. we can think of it as the "body" of the function.
# the lambda expression itself returns a function object.


# when Python execute that `lambda` keyword, it is not actually evaluating the expression.
# just like when the `def` keyword gets compiled, it is actually creating the function object, 
# same with lambda expressions.


# whenever we use `def`, it require us to define a symbol to reference that function object. 
# but lambda expressions do not, they are just a function object that exist in memory and doesnt
# get assigned to a symbol:
type(lambda x: 'python')  # <class 'function'>

type(lambda x: x**2)      # <class 'function'>
type(lambda x, y: x + y)  # <class 'function'>
type(lambda: 'python')    # <class 'function'>
type(lambda s: s[::-1])   # <class 'function'>

# note that, all these expressions are function objects, but they are not "named", thats why they
# are also called anonymous functions. 
# they are essentially just function objects, just like the one that we create using `def`.


# whenever Python loads the module and compile that lambda expression, it will create a new 
# function object in memory. but they dont get assigned to a symbol by default, but we can:
f = lambda: 'python'    # <function <lambda> at 0x000001>

# still being a function object, but having a reference to that object in memory now:
type(f)  # <class 'function'>

# we can call it by using its reference:
f()      # python


# its the same thing that doing it with the `def` keyword essentially:
def f():
    return 'python'

type(f)  # <class 'function'>
f()      # python



# these function objects can be passed as an argument to another function as well:
def f(x, fn):
    fn(x)

f('python', lambda x: print(x)) # python

# equivalently by using `def`:
def my_f(x):
    print(x)

f('python', my_f) # python


# we can set default values to lambdas:
f = lambda x, y=777: print(x, y)
f(10)     # 10, 777
f(10, 20) # 10, 20


# variable length arguments such as *args, **kwargs are allowed as well:
f = lambda *args, **kwargs: f'args={args}, kwargs={kwargs}'

f(1, 2, 3, key1='dark', key2='magician') 
# args=(1, 2, 3), kwargs={'key1': 'dark', 'key2': 'magician'}

#______________________________________________________________________________________________________
# flow of lambdas:
def f(fn, *args, **kwargs):
    # args   = (1, 2)
    # kwargs = {'key1': 'dark}
    return fn(args, kwargs) # return fn((1, 2), {'key1': 'dark})

# that is not what we want. therefore, we required to unpack it as well:
def f(fn, *args, **kwargs):
    # args = (1, 2)
    # kwargs = {'key1': 'dark'}
    return fn(*args, **kwargs) # fn(1, 2, key1='dark') -> 'YEAH'

f(lambda a, b, key1: 'YEAH', 1, 2, key1='dark') # YEAH
# notice that, the arguments are specified after the return value.

# another exemples:
f(lambda x, y: x-y, 7, 2)      # 5
f(lambda x, *, y: x+y, 7, y=3) # 10
f(lambda *args: sum(args), 1, 2, 3, 4, 5) # 15

f(sum, (1, 2, 3, 4, 5)) # 15  sum(1, 2, 3, 4, 5) is being called essentially.


# some limitations of lambda expressions is that, the "body" of a lambda is limited to a 
# single expression, and we cant do assignments inside it and annotations either.


# an important note is that, lambdas are not equivalent to closures. they are regular functions
# essentially, but lambdas can be used as closures as well.

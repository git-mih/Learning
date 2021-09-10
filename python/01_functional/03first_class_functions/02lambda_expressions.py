# Lambda expressions

# we can create functions objects using the `def` statement. but lambda expressions are another 
# way of creating function objects as well.

# syntax:  
# lambda [parameter_list]: return_value [, argument_list] -> function object

# parameters are optinal but the `:` is required. 
# the `return_value` will be executed and return its value only when the lambda function object 
# gets called. we can think of it as the "body" of the function. 

# the lambda expression itself returns a function object.


# when Python execute that `lambda` keyword, it is not actually executing its "body" scope.
# just like when the `def` keyword gets compiled, it is actually creating the function object.
# and is the same with lambda expressions, it just creates that function object in memory.


# whenever we use `def`, it require us to define a symbol to reference that function object. 
# lambda expressions doesnt. they are just a function object that exist in memory and doesnt
# get assigned to a symbol:
type(lambda x: 'python')  # <class 'function'>

type(lambda x: x**2)      # <class 'function'>
type(lambda x, y: x + y)  # <class 'function'>
type(lambda: 'python')    # <class 'function'>
type(lambda s: s[::-1])   # <class 'function'>

# note that, all these expressions are function objects, but they are not "named", thats why they
# are also called anonymous functions. 
# they are essentially just function objects, just like the one that gets created using `def`.


# whenever Python loads the module and compile that lambda expression, it will create a new 
# function object in memory. but they dont get assigned to a symbol by default, but we can:
f = lambda: 'python'    # <function <lambda> at 0x000001>

# still being a function object, but having a reference to that function object in memory now:
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
# notice that, the arguments itself are specified after the return value.


# another exemples:
f(lambda x, y: x-y, 7, 2)      # 5
f(lambda x, *, y: x+y, 7, y=3) # 10
f(lambda *args: sum(args), 1, 2, 3, 4, 5) # 15

f(sum, (1, 2, 3, 4, 5)) # 15  sum(1, 2, 3, 4, 5) is being called essentially.


# some limitations of lambda expressions is that, the "body" of a lambda is limited to a 
# single expression, and we cant do assignments inside it and annotations either.


# an important note is that, lambdas are not equivalent to closures. they are regular functions
# essentially. but lambdas can be used as closures as well.


#______________________________________________________________________________________________________
# lambdas and sorting:

# Python has a function called `sorted` that will takes an iterable, and return a list 
# containing all items from that iterable in ascending order (by default). 
# so we can supply list, dictionary, tuple, strings, etc.

l = [1, 5, 3, 10, 9, 6] # 0x000001

# we can sort that list object by using `sorted()`, but is important to know that, it will not 
# do an in-place ordering. meaning that, it will not sort the list object 0x000001 but return a 
# new sorted list object:
sorted(l) # [1, 3, 5, 6, 9, 10]
l         # [1, 5, 3, 10, 9, 6]



# the sorted function works pretty well, but take a look at this:
sorted(['c', 'B', 'D', 'a']) # ['B', 'D', 'a', 'c']

# sorting strings will be based on the ASCII code table:
ord('A') # 65  capital letters will precede lower case letters. 
ord('a') # 97  that is why the they came first. 



# a custom key function can be supplied to customize the sort order of `sorted`:
#   sorted(iterable [,key=fn]) -> list

# it is used to change the way in which elements will be ordered, it does that by 
# calling a function to each element of the iterable, and threi return value will be sorted.

# for every element in the iterable, we can associate another element to sort, that element 
# could be the upper case version of each element for exemple:
sorted(['c', 'B', 'D','a'], key=lambda e: e.upper()) # ['a', 'B', 'c', 'D']


# another exemple:
d = {'def': 200, 'abc': 300, 'ghi': 100}

# if we sort that dictionary, it will iterate only over the keys essentially:
sorted(d) # ['abc', 'def', 'ghi']

# but we can sort that dictionary based on its values and not in the keys:
sorted(d, key=lambda e: d[e]) # ['ghi', 'def', 'abc']
# d['def'] = 200  //  d['abc'] = 300 //  d['ghi' = 100] essentially.


# we are sorting elements by associating a function call that give us an specified order for 
# each element of that iterable, we can order things the way that we want.

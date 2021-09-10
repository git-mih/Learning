# Partial functions

# they are high order functions essentially. and the ideia behind partial functions is simple, 
# the ideia is to just reduce the number of required arguments of some function.

# it essentially create aliases of the original function, but any aliases have different 
# pre-determined values. it means that, we can create various partial functions and call them
# without having to specify arguments that were pre-defined during the partial function object
# creation.


# creating the main function:
def my_func(a, b, c):
    return a, b, c

# the idea is to create a partial function object that takes only 2 arguments and delegates 
# the partial function call to the main function:
def f(b, c):
    return my_func(777, b, c) # pre-setting the symbol `a` to reference that integer object (777).

# we can call that partial function that only takes 2 arguments now:
f(20, 30) # (777, 20, 30)


# we could also use default values to do the same thing essentially:
def f(b, c, a=777):
    return my_func(a, b, c)

f(20, 30) # (777, 20, 30)


# lambda expression works as well:
f = lambda b, c: my_func(777, b, c)
f(20, 30) # (777, 20, 30)

#_______________________________________________________________________________________________________
# built-in partial function:

from functools import partial

# partial(fn, <positional_arguments>) -> function object


f = partial(my_func, 777) # my_func(a=777, b, c)  essentially.
callable(f)  # True    functools.partial(<function my_func at 0x000001>, 777)

# first position arguments was already pre-defined. we just need to pass the remaining arguments:
f(20, 30) # (777, 20, 30)


# we can handle more complex arguments as well:
def my_func(a, b, *args, kw1, kw2, **kwargs):
    # a = 10
    # kw1 = 'sup
    return a, b, args, kw1, kw2, kwargs

# creating the partial function object:
def f(b, *args, kw2, **kwargs):
    # we are implicitly passing `a` and `kw1` to the main function.
    return my_func(10, b, *args, kw1='sup', kw2=kw2, **kwargs)

# we just require to provide the remaininig arguments:   b, *args, kw2, **kwargs
f(20, 30, 40, kw2=50, number=60)  # (10, 20, (30, 40), 'sup', 50, {'number': 60})


# using the built-in partial function to do that:
f = partial(my_func, 10, kw1='sup') 
f(20, 30, 40, kw2=50, number=60)  # (10, 20, (30, 40), 'sup', 50, {'number': 60})


# another exemple:
def power(base, exponent):
    return base ** exponent

# creating "aliases" that have the pre-defined argument values:
square = partial(power, exponent=2)
cube = partial(power, exponent=3)

# we just require to pass a single argument now:
square(5) # 25
cube(5)   # 125

# its important to know that, nothing stop us of override that pre-defined argument:
cube(5, exponent=2) # 25

#____________________________________________________________________________________________________
# we should be careful while passing variables (references) as argument to partial functions.

# we may have the same issue that happens with default-value arguments. that one that happen when
# the function object get compiled:
def my_func(a, b, c):
    return a, b, c

var_ = 10  # 0x000001
print(id(var_))

f = partial(my_func, var_)
# whenever the partial function get compiled (when Python creates that object essentially), 
# the symbol `a` of the partial function object will reference that integer object at 0x000001:
f.args  # (10,)  (<'int' object at 0x000001>,)  essentially.

# it will works properly:
f(20, 30)  # (10, 20, 30)

# but if later on we decide to change the `var_` reference to another object:
var_ = 777  # 0x000003

# the partial function object still have a reference to that integer object at 0x000001:
f.args  # (10,)  (<'int' object at 0x000001>,)

# it happens cause when the partial function object was created, the `var_` was referencing that 
# integer object at 0x000001.

# therefore, if we try to call the partial function again, we are going to have that same reference:
f(20, 30)  # (10, 20, 30)


# the same is applied to mutable objects when dealing with partial functions:
def my_func(a, b, c):
    return a, b, c

l = [1, 2, 3]  # 0x000001

f = partial(my_func, l) 

# the partial function object `l` is referencing that mutable object at 0x000001:
f.args    # ([1, 2, 3],)  (<'list' object at 0x000001>,) essentially.

f(20, 30) # ([1, 2, 3], 20, 30)


# but if later on we mutate that list object at 0x000001:
l.append(777)

# it will reflect the partial function as well:
f.args    # ([1, 2, 3, 777],)

f(20, 30) # ([1, 2, 3, 777], 20, 30)

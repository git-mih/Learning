# Decorators

# we already decorated a function before by dealing with closures:
def counter(fn):
    count = 0
    def inner(*args, **kwargs):
        nonlocal count
        count += 1
        print(f'{fn.__name__} function was called: {count} time(s)')
        return fn(*args, **kwargs)
    return inner

def add(x, y):     # <function add at 0x000001>
    return x + y

# now we call the decorator function `counter` which will return an closure function.
# that closure itself have an reference to the original `add` function:
add = counter(add) # <function counter.<locals>.inner at 0x000002>

# the thing is that, we are actually replacing its variable name. the `add` symbol was 
# previously pointing to the original `add` function object at 0x000001, but it is now
# referencing the closure function object at 0x000002. that closure will actually call the
# original `add` function at 0x000001, but it will do some extra work now:
add(3, 7)  # add function was called: 1 time(s)  10
add(2, 3)  # add function was called: 2 time(s)  5


# in general, a decorator function:
#     - takes a function object as an argument;
#     - returns an closure;
#     - the closure usually accepts any combination of parameters (*args, **kwargs);
#     - runs some extra code inside the inner function (closure);
#     - then the closure function calls the original function by using the arguments that
#       were passed in to the closure;
#     - the closure function returns whatever is returned by the original function call.



# an convenient way of doing that decoration is by using the decorator syntax with @ symbol:
@counter
def sub(x, y):
    return x - y

# Python is essentially passing that `sub` function as argument to the `counter` function and
# assigning that returned closure object to the symbol `sub` again:
sub = counter(sub)  # <function counter.<locals>.inner at 0x000002>

# so whenever we call `sub` now, we are actually calling that closure (inner function):
sub(12, 2) # sub function was called: 1 time(s)  10

# that closure function will be responsible to call the original `sub` function essentially.

#_________________________________________________________________________________________________
# introspecting decorated functions:

# using the same decorator function:
def counter(fn):
    count = 0
    def inner(*args, **kwargs):
        nonlocal count
        count += 1
        print(f'{fn,__name__} function was called: {count} time(s)')
        return fn(*args, **kwargs)
    return inner

@counter
def multiply(a, b):
    """returns the product of two values"""
    return a * b

# essentially:
multiply = counter(multiply) # <function counter.<locals>.inner at 0x000002>

# the thing is that, `multiply` is no longer referencing the original `multiply` function:
multiply.__name__  # inner

# same will happen if we try to access the function documentation:
help(multiply)
# Help on function inner in module __main__:
# inner(*args, **kwargs)

# we have also "lost" our docstrig and even the original `multiply` function signature.
# we basicly "lost" all the information that the original `multiply` function provides. 

# the local variable `fn` avaiable inside the `counter` function is the only one that actually 
# have the original `multiply` function reference.

# the variable name `multiply` that is in our global scope only have the closure function 
# details right now.

# even using the inspect module would not yield better results. what we could do to actually
# fix that, is by using the functools.wraps function:
from functools import total_ordering, wraps
from time import time

# it will fix the metadata of our closure (inner function) inside our decorator function.

# in fact, the functools.wraps function is a decorator as well, but it needs to know what was
# our original function object, and we do that by passing the received function as argument
# to the decorator wraps function:
def counter(fn):
    count = 0
    @wraps(fn) # passing the original function object to the wraps function decorator.
    def inner(*args, **kwargs):
        nonlocal count
        count += 1
        print(f'{fn,__name__} function was called: {count} time(s)')
        return fn(*args, **kwargs)
    # wraps is essentially doing it:    inner = wraps(fn)(inner)
    return inner

@counter
def multiply(a, b):
    """returns the product of two values"""
    return a * b

# now we will get what we expected, details about the original `multiply` function object:
multiply.__name__ # multiply

help(multiply)
# Help on function multiply in module __main__:
# multiply(a, b)
#     returns the product of two values


# we dont have to use @wraps, but it will make our life eaiser while debugging.


#__________________________________________________________________________________________________
# parametrized decorators:

# to be able to make parametrized decorators, we should know how nested closures works.

# what is happening is that, we can not pass more than the function object as argument to the
# decorator function:
def timed(fn, n): # passing two arguments (fn, n) to the decorator function.
    from time import perf_counter

    def inner(*args, **kwargs):
        elapsed = 0
        # calling the function `n` times:
        for i in range(n):
            start = perf_counter()
            result = fn(*args, **kwargs)
            elapsed += (perf_counter() - start)
        print(elapsed)
        return result
    return inner

# we cant do that, cause by doing that, we are not able to call it this way:
# @timed(5)
# def add(a, b):
#     return a + b

# TypeError: timed() missing 1 required positional argument: 'n'

# that @timed(5) is essentially doing it:
# add = timed(5)

# we are not passing the required function to the decorator.


# to fix that, we usually create an "decorator factory", where we use nested closures.
# the thing is that, we are going to pass that variable name `n` via the decorator factory:
def outer(n): # <_________________________
    def timed(fn): # <____________________\_________
        from time import perf_counter # cell obj    \
#                                          |      cell obj
        def inner(*args, **kwargs): #      |         |
            elapsed = 0             #      |         |
            for i in range(n): # ---> free variable  |
                start = perf_counter() #             |
                result = fn(*args, **kwargs) # free variable
                elapsed += (perf_counter() - start)
            print(f'calling {n} times - time elapsed: {elapsed:2f}')
            return result
        return inner # returning the decorated function.
    return timed # returning the original decorator function.

# calling outer (the decorator factory), will return our original decorator function with that
# free variable `n` defined:
outer(5) # <function outer.<locals>.timed at 0x000001>


# now we can decorate our regular functions by using that parametrized @ syntax:
@outer(5)      # add = outer(5)(add)
def add(a, b): #         dec(add)
    return a + b

add(7, 3) # calling 5 times - time elapsed: 0.000003   10

# it is essentially doing it:
decorator = outer(5)  # <function outer.<locals>.timed at 0x000001>
add = decorator(add)  # <function outer.<locals>.timed.<locals>.inner at 0x000002>

# one shot representation:
add = outer(5)(add) # <function outer.<locals>.timed.<locals>.inner at 0x000002>


add(7, 3) # calling 5 times - time elapsed: 0.000003   10


# the outer function itself isnt a decorator. instead, it returns an decorator when called.
# any arguments that was passed to the outer function can be referenced (as free variables)
# inside our decorator. 
# we usually call this outer function as a decorator factory cause, it is a decorator that 
# creates a new decorator function each time its called.

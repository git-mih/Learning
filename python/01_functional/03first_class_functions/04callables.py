# Callables

# an callable is any object that can be called by using the () operator essentially.

# callable objects will always return a value, and by default it always return None:
return_value = print('sup')
return_value # None


# to see if an object is callable, we can use the `callable` built-in function:
callable(print)       # True
callable('mih'.upper) # True
'mih'.upper           # <built-in method upper of str object at 0x000001>

# there is also objects that are not callable:
callable([1, 2, 3]) # False
callable(10)        # False



# things like functions and methods are callables, but it goes beyond just those two. in fact, 
# many other objects in Python are also callables that are not technically functions/methods.

#____________________________________________________________________________________________________
# Different types of callable objects:

# built-in functions:  any, len, callable, ...:
callable(any) # True


# built-in methods:  'string'.upper, [1, 2].append, ...:
callable({'name': 'fabio'}.keys) # True


# user-defined functions:  function objects created using def or lambda expressions:
def f():
    return 'sup'

callable(f)              # True
callable(lambda : 'sup') # True


# methods:  function objects that are bound to an object (instance, class, etc):
class Person:
    def f(self):
        pass

p = Person()
p.f  # <bound method Person.f of <__main__.Person object at 0x000001>>
callable(p.f) # True

str.upper  # <method 'upper' of 'str' objects> 
callable(str.upper) # True


# classes:  MyClass() -> __new__() -> __init__ -> instance
callable(Person) # True


# class instances:  if parent class implements the __call__ method:
class Person:
    def __call__(self):
        pass
p = Person()
callable(p) # True


# generators, coroutines, asynchronous generators...

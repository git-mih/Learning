# Decorator class

# we can use class to decorate functions or even classes.

# class object instances can be callables, all we have to do is implement the __call__ method.

#______________________________________________________________________________________________________
# lets see the parallel with decorator functions:
import functools

def decorator(fn):
    def wrapper(*args, **kwargs):
        return fn(*args, **kwargs)
    return wrapper

@decorator
def func(a, b):
    return a, b
# func = decorator(func)    # type(func)  <class 'function'>

func(10, 20)  # (10, 20)


# doing the same but using a decorator class:
class Decorator:
    def __init__(self, fn):
        self.fn = fn
    # we receive a function object, then we store it inside the object instance namespace.
    
    def __call__(self, *args, **kwargs):
        return self.fn(*args, **kwargs)
    # Decorator instances will be callable objects. son, whenever we call them, they will go 
    # and looks inside its namespace for the `fn` attribute and calls it.

@Decorator
def func(a, b):
    return a, b
# func = Decorator(func)    # type(func)  <class '__main__.Decorator'>

callable(func) # True
func(10, 20)   # (10, 20)

# essentially, Python is calling the __call__ method:
Decorator.__call__(func, 10, 20)  # (10, 20)

#______________________________________________________________________________________________________
# Function vs the class approach:
def func():
    pass

f = decorator(func)  # <function object at 0x000001>
# calling it will actually calls the `wrapper` function that was returned from the decorator.

# and if we do it from the class, like:
f = Decorator(func)  # <'__main__.Decorator' object at 0x000002>
# `f` is no longer a function object. 
# it is actually an object instance of Decorator class. however, the Decorator class defined 
# the __call__ method, so `f` still being a callable object. 
# when we call it now, it will calls the __call__ method of that object instance essentially:
Decorator.__call__(f)


# both approaches works fine to decorate regular functions, but there is a major diference:
#   when we use a function decorator, the decorated function remains being a function.
#   but when we use an decorator class, the decorated function will become an object instance
#   of that class.


# it will affects our ability to decorate functions inside other classes. methods essentially.
# functions that are defined inside a class become bound methods when called from a instance.
# because functions are non-data descriptors essentially. 
# which means that, they have the __get__ method defined, and our decorator class doesnt.

# we should implement the descriptor protocol in our decorator class to be able to work with
# functions inside other classes. 
# so we can bound the callable Decorator instance to the other class object instance.


#_______________________________________________________________________________________________________
# decorator class:
class Logger:
    def __init__(self, fn):
        self.fn = fn  # object instance namespace: {'fn': <function say_hello at 0x000002>}
    
    def __call__(self, *args, **kwargs):
        print(f'log: {self.fn.__name__} called...')
        return self.fn(*args, **kwargs)  

@Logger
def say_hello():
    pass
# say_hello = Logger(say_hello)   # <__main__.Logger object at 0x000001>

say_hello()  # log: say_hello called...

#______________________________________________________________________________________________________
# the big difference though, between using a decorator function and using a decorator class
# is that, the object type is changed dramatically. even both being callables, it lead us to an 
# issue that, we cant decorate methods inside any class by using our decorator class:
class Person:
    def __init__(self, name):
        self.name = name
    
    # trying to decorate an instance method with our decorator class:
    @Logger
    def say_hello(self):
        return f'{self.name} says hello...'
    # say_hello = Logger(say_hello)  <__main__.Logger object at 0x000001>

p = Person('Fabio')
# p.say_hello()

# log: say_hello called...
# TypeError: say_hello() missing 1 required positional argument: 'self'


# the `self` was not passed to the `say_hello` function. it means that, Python isnt binding 
# `say_hello` to the Person instance `p`. why Python isnt doing it:   Person.say_hello(p)


# during compilation, when the class Person gets created, it takes the code, runs it and creates 
# the class namespace.
# that `say_hello` function inside the class will become an Logger instance during compilation 
# of that Person class
p.say_hello  # <__main__.Logger object at 0x000001>


# now, whenever we create a new Person object instance, the class namespace doesnt have that 
# `say_hello` as a function object anymore. therefore, when the Person instance tries to call 
# that `say_hello` which is now a Logger instance, Python doesnt know how to bound that callable
# Logger instance to the Person instance.


# functions are non-data descriptors, whenever we call an function object, it will call the
# __get__ method and will see if its getting called from some instance or not. 
# if its called from an instance, the function object will be transformed into a method that is
# bound to that instance.

# the reason why functions get transformed into methods when they get called from instances 
# is that, functions implement the non-data descriptor protocol. so, when we have a function, 
# Python see's that as a descriptor and then it uses that by calls the __get__ method.

# in our case, it doesnt see that as a descriptor. cause the Logger class doesnt implement the 
# descriptor protocol. the __get__ method will never be called. so when we runs: p.say_hello()
# it doesnt get called as a bound method. it just gets called as a regular callable, it will
# calls the the Decorator __call__ method without passing any argument, like: Logger.__call__()


#______________________________________________________________________________________________________
# we just require to implement the __get__ method in our decorator class and turn it into a 
# non-data descriptor, just like functions. 

# we just need to return the Decorator instance which is a callable, but return it bounded to 
# the other class instance:
from types import MethodType

class Logger:
    def __init__(self, fn):
        self.fn = fn

    def __call__(self, *args, **kwargs):
        print(f'log: {self.fn.__name__} called...')
        return self.fn(*args, **kwargs)
    
    def __get__(self, instance, owner_class):
        print(f'__get__ called: self={self}, instance={instance}')
        if instance is None:
            return self
        print(f'returning self as a method bound to {instance}...')
        return MethodType(self, instance)
# self is the Logger instance. and it have the __call__ method, so its a callable essentially.
# so we are going to bind this callable to the other class instance that called the Logger instace.

class Person:
    def __init__(self, name):
        self.name = name
    
    @Logger
    def say_hello(self):
        return f'{self.name} says hello...'
    # say_hello = Logger(say_hello)

# whenever Python compiles the Person class, `say_hello` will become a Logger instance:
Person.say_hello    # <__main__.Logger object at 0x000001>


p = Person('Fabio') # type(p.say_hello)   <class 'method'>

# when we call `say_hello` by using the Person instance, it will call the Logger __get__ method:
p.say_hello 
# __get__ called: self=<__main__.Logger object at 0x1>, instance=<__main__.Person object at 0x2>
# returning self as a method bound to <__main__.Person object at 0x2>

# like this essentially:
Logger.__get__(Person.say_hello, p, Person)


# our decorator class is working properly now, we can call it:
p.say_hello() 
# log: say_hello called...
# Fabio says hello...


# also, we still able to use our decorator class (Logger) to decorate functions:
@Logger
def say_bye():
    pass
# say_bye = Logger(say_bye)   <__main__.Logger object at 0x000001>


say_bye()  # log: say_bye called...

# in this case, Python isnt looking for a descriptor, so it will just call the __call__ method
# with the Logger instance:
Logger.__call__(say_bye)  # log: say_bye called...


# it also works properly with static and class methods:
class Person:
    @classmethod
    @Logger
    def class_method(cls):
        return 10

    @staticmethod
    @Logger
    def static_method():
        return 20

Person.class_method()
# log: class_method called...
# 10

Person.static_method()
# log: static_method called...
# 20


#______________________________________________________________________________________________________
# NOTE: 
# we just need to remember, if and only if we are going to use decorator classes to decorate
# methods inside another class, then we need to remember to implement the __get__ method.
# we only require to use the descriptor protocol when we are in the context of decorating a 
# function inside a class, for exemple, decorating an instance method with decorator classes.

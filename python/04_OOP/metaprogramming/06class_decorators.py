# Class decorators

# metaclasses are not always the best approach though. they can be very powerful, but they
# can also be hard to understand when reading the code.

# and sometimes decorators can work just as metaclasses and decorators are generally easier to 
# understand because they are more functional in nature.


# decorating classes:
# we can actually decorate a class by using the decorator: `@my_dec` syntax in the same way that
# we would decorate a function. it does the exactly same thing that it does to de functions.

# so we can write a decorator that basicly expects a class as the input, not a function but a
# class, and then it returns the tweaked, modified class for us:
def savings_account(cls):
    # we get a class object, and add a new entry inside the class namespace:
    cls.account_type = 'savings'
    return cls # then we return the class object

# now we can use this decorator to decorate a class by just using the decorator syntax:
@savings_account
class BankAccount:
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance

# essentially its doing it:
class BankAccount:
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance

BankAccount = savings_account(BankAccount)

# what happen is that, the class object is created firts, then it gets decorated.


# we can even make an parametrized decorator. all we need is is basicly an inner level of 
# nesting where the outer level is going to receive the parameter and it is going to return
# an decorator that will have that parameter as part of its closure. 
# its essentially the same thing as parametrized functions decorarators where we actually 
# creates a decorator factory function.

# we could use metaclasses to do it instead, but having to pass parameters to the metaclass is
# probably overkill.


# class decorators can be used to create, delete or modify class attributes. it can modify
# plain attributes, methods, and we can even apply decorators to class methods, where we can
# have a class decorator that applies function decorators to its class methods.

# we are not using metaclasses, but it is metaprogramming as well.

#____________________________________________________________________________________________________
# class decorator:
def account_type(type_):
    def decorator(cls):
        cls.account_type = type_
        return cls
    return decorator

@account_type('Savings')
class Bank1Savings:
    pass

@account_type('Checking')
class Bank1Checking:
    pass

Bank1Savings.__dict__   #  {..., 'account_type': 'Savings'}
Bank1Checking.__dict__  #  {..., 'account_type': 'Checking'}


# we are not restricted to add only data attributes, we can inject functions/methods as well:
def hello(cls):
    cls.hello = lambda self: f'{self} says hello'
    return cls

@hello
class Person:
    def __init__(self, name):
        self.name = name
    
    def __str__(self):
        return self.name

p = Person('Fabio')
p.hello()  # Fabio says hello


#____________________________________________________________________________________________________
# making a decorator that will log every call for every callable in some class:
from functools import wraps
import functools

def func_logger(fn):
    @wraps(fn)
    def inner(*args, **kwargs):
        result = fn(*args, **kwargs)
        print(f'log: {fn.__qualname__}({args}, {kwargs}) = {result}')
        return result
    return inner

class Person:
    @func_logger
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @func_logger
    def greet(self):
        return f'hello, im {self.name}, and im {self.age}.'

p = Person('Fabio', 26)
# log: Person.__init__((<__main__.Person object at 0x000001>, 'Fabio', 26), {}) = None

p.greet()
# log: Person.greet((<__main__.Person object at 0x000001>,), {}) = hello, im Fabio, and im 26.

#____________________________________________________________________________________________________
# that works, but would be kinda tedious if we have many methods inside our class, we would 
# have to repeat the @func_logger decorator everytime.

# so instead of doing this way, we could create a class decorator that will do the same thing,
# will decorate every object that is callable with that func_decorator function. but it will
# decorate automatically now, without we have to write it again and again:
def class_logger(cls):
    for atrib_name, obj in cls.__dict__.items():  # also: vars(cls).items()
        if callable(obj):
            print('decorating:', cls, atrib_name)
            setattr(cls, atrib_name, func_logger(obj)) # Person.greet = func_logger(greet)
    return cls
# iterating through all items in the Person class namespace, and if the object is callable, we
# decorate that callable object with the func_logger decorator.

@class_logger
class Person:
    def __init__(self, name, age): # callable(__init__)  True
        self.name = name
        self.age = age

    def greet(self): # callable(greet)  True
        return f'hello, im {self.name}, and im {self.age}.'

# after the class object gets created, it will be decorated. essentially, Python will do it:
Person = class_logger(Person)
# decorating: <class '__main__.Person'> __init__
# decorating: <class '__main__.Person'> greet

p = Person('Fabio', 26)
# log: Person.__init__((<__main__.Person object at 0x000001>, 'Fabio', 26), {}) = None

p.greet()
# log: Person.greet((<__main__.Person object at 0x000001>,), {}) = hello, im Fabio, and im 26.



# but we have to be careful tho. this class decorators looks like it works just fine, but it
# is going to have issues with static and class methods.
# it will happen because
@class_logger
class Person:
    @staticmethod
    def static_method():
        print('static_method invoked')

    @classmethod
    def cls_method(cls):
        print(f'cls_ethod invoked for {cls}')

    def instance_method(self):
        print(f'instance_method invoked for {self}')

# decorating: <class '__main__.Person'> instance_method

# note that, when Person gets decorated. our class_logger class decorator only decorated the
# instance_method function. but why?

# class and static methods are descriptors essenstially, they are not functions. 
# descriptors are not directly callables, and the `callable(static/classmethod)` is evaluating 
# to False.

callable(Person.__dict__['static_method']) # False
#        <staticmethod object at 0x000001>   the descriptor instance.

# we require to decorate the functions before we turn them into static or class methods. cause 
# otherwise, we would try to decorate a descriptor instance, and possibly get issues with that:
class Person:
    @staticmethod
    @func_logger 
    def static_method():
        pass

# now it will works properly:
Person.static_method()  # log: Person.static_method((), {}) = None

#____________________________________________________________________________________________________
# to be able to deal with static and class methods, we just require to get the original function
# instead of getting the descriptor object:
Person.__dict__['static_method'] # <staticmethod object at 0x000001>  descriptor instance.
Person.__dict__['static_method'].__func__ # <function Person.static_method at 0x000002>

def class_logger(cls):
    for attrib_name, obj in vars(cls).items():
        if callable(obj):
            print(f'decorating callable: {cls.__name__}.{attrib_name}')
            original_fn = obj
            decorated_func = func_logger(original_fn)
            setattr(cls, attrib_name, decorated_func)
        elif isinstance(obj, staticmethod): # obj = <staticmethod object at 0x01>
            print(f'decorating static method: {cls.__name__}.{attrib_name}')
            original_fn = cls.__dict__[attrib_name].__func__ # <function Person.static_method at 0x02>
            decorated_func = func_logger(original_fn)       # <function Person.func_logger at 0x03>

        # at this point we decorated the object, now we require to make it a descriptor again:
            method = staticmethod(decorated_func)           # <staticmethod object at 0x04>
            setattr(cls, attrib_name, method) # Person.static_method = <staticmethod object at 0x04>
        # finally we add the descriptor instance inside the class namespace
        elif isinstance(obj, classmethod):
            print(f'decorating class method: {cls.__name__}.{attrib_name}')
            original_fn = cls.__dict__[attrib_name].__func__
            decorated_func = func_logger(original_fn)
            method = classmethod(decorated_func)
            setattr(cls, attrib_name, method) # Person.class_method = <classmethod object at 0x05>
    return cls

@class_logger
class Person:
    @staticmethod
    def static_method(a, b):
        print('static_method called', a, b)

    @classmethod
    def class_method(cls, a, b):
        print(f'class_method called for {cls} {a} {b}')

    def instance_method(self, a, b):
        print(f'instance_method called for {self} {a} {b}')

# decorating static method: Person.static_method
# decorating class method:  Person.cls_method
# decorating callable:      Person.instance_method

# we can see in the Person namespace that we still have the descriptors, but decorated now:
Person.__dict__
# {static_method': <staticmethod object at 0x04>, 
# 'cls_method': <classmethod object at 0x05>, 
# 'instance_method': <function Person.instance_method at 0x07>, ...}

Person.static_method(10, 20) # static_method called 10 20
#                              log: Person.static_method((10, 20), {}) = None

Person.class_method(10, 20)  # class_method called for <class '__main__.Person'> 10 20
#                  log: Person.class_method((<class '__main__.Person'>, 10, 20), {}) = None

p = Person()
p.instance_method(10, 20) # instance_method called for <__main__.Person object at 0x009> 10 20
#        log: Person.instance_method((<__main__.Person object at 0x009>, 10, 20), {}) = None

#____________________________________________________________________________________________________
# this is really good, but what about properties? they are callables in essence but they are
# also implemented by using the descriptor protocol, and we are not specific handling 
# properties in our code.
@class_logger
class Person:
    def __init__(self, name):  
    # __init__ will be decorated normally.
        self._name = name

    @property
    def name(self):
    # but the property wont.
        return self._name

# so whenever Python compile the class and apply the decorator in the callables:
# decorating callable: Person.__init__

type(Person.__dict__['name'])  # <class 'property'>
isinstance(Person.__dict__['name'], property)  # True

# how do we get the original function of a property? cause we need to unwrap the property and
# get the original 'name' function to be able to apply the func_logger decorator:
Person.__dict__['name'].fget  # <function Person.name at 0x000001>
Person.__dict__['name'].fset  # None
Person.__dict__['name'].fdel  # None

# maybe we could decorate if defined, the fget,f set and fdel functions of the property. but we
# cant just replace the functions in the property because fget, fset, fdel are essentially just
# read-only properties themselves.


# we could create a new property based on the original one. and by doing that, we would simple
# substitute the fget, fset and fdel for our decorated fget, fset and fdel.

# we have methods like getter(), setter() and deleter(). they essentially create a copy of the
# original property but they will substitue the fget, fset, fdel methods. 
# that is how we do it essentially, we usually replace the property that only have a fget
# defined to a new property with a fset, like:  
prop = property(fget=lambda:'getter')           # <property object at 0x000001>
prop = prop.setter(lambda:'getter and setter')  # <property object at 0x000002>

# lets implement it to support properties as well:
def class_logger(cls):
    for attrib_name, obj in vars(cls).items():
        if callable(obj):
            print(f'decorating callable: {cls.__name__}.{attrib_name}')
            original_fn = obj
            decorated_func = func_logger(original_fn)
            setattr(cls, attrib_name, decorated_func)
        elif isinstance(obj, property): # obj = <property object at 0x222222>
            print(f'decorating property: {cls.__name__}.{attrib_name}')
        # if the property object has a fget function defined, we replace that by taking the
        # original function and we create a new property with the decorated function:
            if obj.fget:  # obj.fget <function Person.name at 0x000001>
                obj = obj.getter(func_logger(obj.fget))
        # we got a new property object now:     <property object at 0x333333>

        # we do the same to the setter and deleter if its implemented:
            if obj.fset:
                obj = obj.setter(func_logger(obj.fset))  # <property object at 0x444444>
            if obj.fdel:
                obj = obj.deleter(func_logger(obj.fdel)) # <property object at 0x555555>
        # once we get this new property object that contains every function decorated, we can 
        # add it to the class namespace (dict):
            setattr(cls, attrib_name, obj)  # Person.name = <property object at 0x55555>
    return cls

@class_logger
class Person:
    def __init__(self, name):
        self._name = name
    
    @property
    def name(self):
        return self._name

# once the Person class gets created, it will get decorated:   Person = class_loger(Person)
# decorating callable: Person.__init__
# decorating property: Person.name

p = Person('Fabio') 
# log: Person.__init__((<__main__.Person object at 0x000001>, 'Fabio'), {}) = None

# now when we call the name property, it will call the decorated function:
p.name #  Fabio
# log: Person.name((<__main__.Person object at 0x000001>,), {}) = Fabio


#____________________________________________________________________________________________________
# well, we still have a problem though, cause not every callable is a function. and if isnt a
# function, it cant be decorated. 

# callables are not necessarelly functions:
@class_logger
class Person:
    class Other:    # callable(Other) True
        def __call__(self):
            pass
    other = Other() # callable(other) True  ||  <'__main__.Other' object at 0x000001>
 
 # the inner class (Other) is also a callable, its instance is a callable as well. therefore,
 # Python will apply the @func_logger decorator on them as well:
# decorating callable: Person.Other
# decorating callable: Person.other

# once it happen, we no longer have that class object and object instance, cause they became 
# functions now:
Person.Other # <function Person.Other at 0x000001>
Person.other # <function func_logger.<locals>.inner at 0x000002>


# it happened cause they are callables essentially, so they were replaced by what comes out of the
# func_logger decorator function, which is a function.

#____________________________________________________________________________________________________
import inspect

def class_logger(cls):
    for attrib_name, obj in vars(cls).items():
        if isinstance(obj, staticmethod): 
            print(f'decorating static method: {cls.__name__}.{attrib_name}')
            original_fn = cls.__dict__[attrib_name].__func__ 
            decorated_func = func_logger(original_fn)       
            method = staticmethod(decorated_func)           
            setattr(cls, attrib_name, method) 
        elif isinstance(obj, classmethod):
            print(f'decorating class method: {cls.__name__}.{attrib_name}')
            original_fn = cls.__dict__[attrib_name].__func__
            decorated_func = func_logger(original_fn)
            method = classmethod(decorated_func)
            setattr(cls, attrib_name, method) 
        elif isinstance(obj, property):
            print(f'decorating property: {cls.__name__}.{attrib_name}')
            if obj.fget:
                obj = obj.getter(func_logger(obj.fget))
            if obj.fset:
                obj = obj.setter(func_logger(obj.fset))
            if obj.fdel:
                obj = obj.deleter(func_logger(obj.fdel))
            setattr(cls, attrib_name, obj)
        elif inspect.isroutine(obj):
            print(f'decorating callable: {cls.__name__}.{attrib_name}')
            original_fn = obj
            decorated_func = func_logger(original_fn)
            setattr(cls, attrib_name, decorated_func)
    return cls

@class_logger
class Person:
    # we want to decorate every routine inside the Person class:
    @staticmethod
    def static_method():
        pass

    @classmethod
    def class_method(cls):
        pass

    @property
    def name(self):
        pass

    def instance_method(self, name):
        pass

    def __add__(self, a, b):
        pass

    # by the way, we could certainly decorate the inner class with our class_logger decorator:
    @class_logger #   it will decorate any routine inside the Other class as well.
    class Other:    # inspect.isroutine(Person.Other)  False
        def __call__(self): # inspect.isroutine(Person.Other.__call__)  True
            pass
    other = Other() # inspect.isroutine(Person.other)  False


# decorating callable: Other.__call__
# decorating static method: Person.static_method
# decorating class method:  Person.class_method
# decorating property: Person.name
# decorating callable: Person.instance_method
# decorating callable: Person.__add__

#____________________________________________________________________________________________________
# lets clean our code now:

def class_logger(cls):
    for attrib_name, obj in vars(cls).items():
        if isinstance(obj, classmethod) or isinstance(obj, staticmethod):
            print(f'decorating: {attrib_name}')
            type_ = type(obj)  # classmethod or staticmethod
            original_fn = cls.__dict__[attrib_name].__func__ 
            decorated_func = func_logger(original_fn)       
            method = type_(decorated_func)
            setattr(cls, attrib_name, method) 
        elif isinstance(obj, property):
            print(f'decorating property: {cls.__name__}.{attrib_name}')
            methods = (('fget', 'getter'), ('fset', 'setter'), ('fdel', 'deleter'))
            for prop, method in methods:     # prop = 'fget', method = 'getter'
                if getattr(obj, prop):       # if Person.name.fget:
                    obj = getattr(obj, method)(func_logger(getattr(obj, prop)))
                    #       obj.method(func_logger(obj.fget))
                    # obj = obj.getter(func_logger(obj.fget)) 
                    setattr(cls, attrib_name, obj)
        elif inspect.isroutine(obj):
            print(f'decorating callable: {cls.__name__}.{attrib_name}')
            original_fn = obj
            decorated_func = func_logger(original_fn)
            setattr(cls, attrib_name, decorated_func)
    return cls

@class_logger
class Person:
    @staticmethod
    def static_method():
        pass

    @classmethod
    def class_method(cls):
        pass

    @property
    def name(self):
        pass

    def instance_method(self, name):
        pass

    def __add__(self, a, b):
        pass

    class Other:  
        def __call__(self): 
            pass
    other = Other() 

# decorating static method: Person.static_method
# decorating class method:  Person.class_method
# decorating property: Person.name
# decorating callable: Person.instance_method
# decorating callable: Person.__add__

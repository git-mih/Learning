# Functions and descriptors

# lets take a look at the role of the descriptors in functions context:

def say_hello(a, b):   # <function say_hello at 0x000001>
    pass

# Functions are essentially Non-data Descriptors:
hasattr(say_hello, '__get__')  # True
hasattr(say_hello, '__set__')  # False


# but what the __get__ method actually returns?  
# it returns the function itself when it gets called from the main module.

# main module reference:
import sys
sys.modules['__main__']  #  <module '__main__' from '09functions_and_descriptors.py'>

# using the descriptor __get__ method to call the 'add' function:
fn = say_hello.__get__(None, sys.modules['__main__'])

# if we call the 'add' function from the main module, the 'instance' will be set to None and 
# the 'owner_class' will be the __main__ module itself.

# Python will automatically pass the 'self' value cause we are calling __get__ as a method.

fn # <function add at 0x000001>

fn is say_hello  # True


# the descriptor __get__ will also return the function when it gets called from a class:
class Person:
    def __init__(self, name):
        self.name = name
    
    def say_hello(self):
        return f'{self.name} says hello'

# if we call the 'say_hello' function directly from the class, it will returns the original
# function object:
Person.say_hello   # <function Person.say_hello at 0x000001>

# Essentially, since functions are just Non-data descriptors, it will call the descriptor 
# __get__ method by setting the 'instance' to None and the owner_class to the Person class. 

# the __get__ method will then returns the original 'say_hello' function object:
f = Person.say_hello.__get__(None, Person)
f                  # <function Person.say_hello at 0x000001>


# but, if we access from an object instance, that 'say_hello' function will be bound to the 
# object instance, like:
p = Person('Fabio')
p.say_hello  # <bound method Person.say_hello of <__main__.Person object at 0x000002>>

# Python is essentially doing it:
m = Person.say_hello.__get__(p, Person)
m            # <bound method Person.say_hello of <__main__.Person object at 0x000002>>


# by the way, how does the method object knows which function it should calls? 
# method objects actually have an attribute called __func__ that keep track of the original 
# function that it should calls:
p.say_hello.__func__ # <function Person.say_hello at 0x000001>
m.__func__           # <function Person.say_hello at 0x000001>

# they both works the same:
p.say_hello() # Fabio says hello
m()           # Fabio says hello


# NOTE: should be careful with the way that __get__ method works. the __get__ will returns a 
# new method object everytime it gets called:
f1 = p.say_hello # 0x000001   f1 = Person.say_hello.__get__(p, Person)
f2 = p.say_hello # 0x000002   f2 = Person.say_hello.__get__(p, Person)

# it looks like we are calling the __get__ method in the same way and we should get the same
# return value but no. we are actually calling different methods, it just happen to be the 
# same function that is bound to the same  object 'p'. but they are not the same:
f1 is f2        # False


#____________________________________________________________________________________________________
# lets create a non-data descriptor that mimics what a function does essentially.
# so we want our descriptor __get__ method to:
#   whenever it gets called from the class, we want it to return the function object. 
#   when it get called from an object instance, we return the bound method object instead.

import types

class DescriptorFunc:
    def __init__(self, fn):
        self._fn = fn

    def __get__(self, instance, owner_class):
        if instance is None:
            # returns the original function (hello)
            return self._fn
        # returns the original function (hello) bound to the instance (p): method(fn, instance)
        return types.MethodType(self._fn, instance)

# original hello function at 0x000001
def hello(self):
    return f'{self.name} says hello'

class Person:
    def __init__(self, name):
        self.name = name

    say_hello = DescriptorFunc(hello)  # descriptor instance
    # passing the original function to the descriptor __init__, so it can returns when
    # 'say_hello' gets called either from the class or some object instance.

# accessing the 'say_hello' property from the class:
Person.say_hello     # <function hello at 0x000001>

# accessing the 'say_hello' property from an object instance:
p = Person('Fabio')  # <__main__.Person object at 0x000002>
p.say_hello          # <bound method hello of <__main__.Person object at 0x000002>>

p.say_hello.__func__ # <function hello at 0x000001>
p.say_hello()        # Fabio says hello

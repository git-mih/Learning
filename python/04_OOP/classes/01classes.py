# Classes:

# A classes is an template used to create objects. but a class is itself an object.

isinstance(type, object) # True
isinstance(object, type) # True

# when we create a class like:
class MyClass: pass

# Python is essentially inheriting from object:
class MyClass(object): pass

# when Python compiles that statement, it creates the class object and 'MyClass' is a symbol 
# that reference that class object in memory:
globals()
# {..., 
#   'MyClass': <class '__main__.MyClass'>
# }


# classes are object instances of a metaclass called (type):
isinstance(MyClass, type) # True
isinstance(str, type)     # True
isinstance(int, type)     # True

type(MyClass) # <class 'type'>
type(str)     # <class 'type'>
type(dict)    # <class 'type'>


# it inherit certain default attributes and methods to our custom class:
dir(MyClass)
# [
#   '__class__', 
#   '__delattr__', 
#   '__dict__', 
#   '__dir__', 
#   '__doc__',
#   '__name__,
#   ...
# ]


# type object instances (classes) are callables:
hasattr(type, '__call__')    # True
hasattr(MyClass, '__call__') # True

callable(MyClass) # True

# when we call a class object, we essentially create a new object instance of that class:
MyClass() # <__main__.MyClass object at 0x0001>

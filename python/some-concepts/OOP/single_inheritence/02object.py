# The object Class

# what is tipical in Python is that, everything that is implemented in C
# uses the C style convention name. And C doesnt use uppercase convention
# when write classes.

# object is a class is implemented in C

# When we define a classs that doesnt inherit from another class
# explicitly, Python makes the class inherit from object implicitly.
class Person:
	pass

issubclass(Person, object) # True

type(object) # <class 'type'>
type(Person) # <class 'type'>

# this means, every class we create is a subclass of object.
# everything, every object, functions, modules... they all are subclass of object class.

# Implications of inheriting from object
# any class we create automatically inherits behaviors and attributes from object class.
dir(object)
# __class__
# __delattr__
# __dir__
# __doc__
# __eq__
# __format__
# __ge__
# __getattribute__
# __gt__
# __hash__
# __init__
# __init_subclass__
# __le__
# __lt__
# __ne__
# __new__
# __reduce__
# __reduce_ex__
# __repr__
# __setattr__
# __sizeof__
# __str__
# __subclasshook__

#_____________________________________________________________________________________
type(object) # <class 'type'>
type(int)    # <class 'type'>
type(str)    # <class 'type'>
type(dict)   # <class 'type'>

# everything in Python is a object, everything inherits from object class
issubclass(int, object)  # True
issubclass(dict, object) # True

import math
type(math) # <class 'module'>
issubclass(type(math), object) # True

# some data objects arent inside builtins, such as module object
import types
dir(types) # FunctionType, GeneratorType, MethodType, ModuleType and many more.

def f():
	pass

type(f) # function (string representation)
type(f) is types.FunctionType  # True
type(math) is types.ModuleType # True

isinstance(f, object) # True


#___________________________________________________________________________________
obj = object()
str(obj)  # <object object at 0x000001A04B0681A0>
repr(obj) # <object object at 0x000001A04B0681A0>

obj1 = object()
obj2 = object()

obj1 is obj2 # False
obj1 == obj2 # False

obj3 = obj1
obj1 is obj3 # True
obj1 == obj3 # True

class Person:
	pass

# it is actually calling the __str__ / __repr__ method in the object class.
p = Person()
str(obj)  # <__main__.Person object at 0x000001A04B0681A0>
repr(obj) # <__main__.PErson object at 0x000001A04B0681A0>

p1 = Person()
p2 = Person()

p1 is p2 # False
p1 == p2 # False

id(Person.__eq__) # 2659649327888
id(object.__eq__) # 2659649327888

# same happens if we dont provide the __init__ method in our custom class.
# it is going to use the __init__ of object class, which doesnt allow us to pass
# any arguments.

id(Person.__init__) is id(object.__init__) # True

# we can override the object.__init__ method
class Person:
	def __init__(self):
		pass

id(Person.__init__) is id(object.__init__) # False

# and whenever we want to create a new instance, it is going to call the
# __new__ from object class if we're not providing it explicitly

p = Person() # object.__new__ -> object.__init__

# Object and classes

# What is an object?
# is a container that contains data/state/attributes and contains functionalities.

# my_car = Car('Ferrari', '599XX', '2010')

# we can access attributes/methods by using dot notation 

# my_car.brand         # state
# my_car.model         # state
# my_car.year          # state

# my_car.accelerate()  # behavior
# my_car.brake()       # behavior
# my_car.steer()       # behavior

# my_car.purchase_value = 1_600_000  # new attribute assignment

#__________________________________________________________________________________
# A class is like a template used to create objects. 
# objects created from that class are called instances.

# classes are themselves objects, python implement these attributes/methods for us
# attributes: C.__name__, C.__init__, C.__eq__
# behavior  : C()   they are callable. its a behavior that python give to us and it
#                   returns an instance of the class.

class MyClass:
	pass
# when this line of code is compiled by python, it creates the MyClass object, 
# just like if we had a: def f() would create an function object.

# the type class is responsible to create it
type(MyClass)     # <class 'type'>
# Python creates an object from this type class. and it automatically provides 
# certain attributes and methods to MyClass

MyClass.__name__   # state.    returns a string with class name: 'MyClass'
my_obj = MyClass() # behavior. returns an instance of MyClass

type(my_obj)                # <class '__main__.MyClass'>
my_obj.__class__            # <class '__main__.MyClass'>
isinstance(my_obj, MyClass) # True

#__________________________________________________________________________________
# if a class is an object, and objects are created from classes, how classes are created?
# classes are created from the type metaclass.

#__________________________________________________________________________________
class Person:
	pass

isinstance(Person, type) # True

type(Person)     # <class 'type'>
# or
Person.__class__ # <class 'type'>
type(Person) is Person.__class__ # True

type(str) # <class 'type'>
isinstance(str, type) # True

type(int) # <class 'type'>
isinstance(int, type) # True

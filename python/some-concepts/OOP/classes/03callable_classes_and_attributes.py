# class attributes can be callable

# Setting an attribute value to a callable

# attributes values can be any object like: other classes, any callable, anything...
# so we can do this:
class MyClass:
	def say_hello(): 
		print('hello world!')

MyClass.__dict__ # {..., 'say_hello': <function __main__.MyClass.say_hello()>}

# how do we call it? we can get it straight from the namespace dictionary:
f = MyClass.__dict__['say_hello']
f()                              # hello world!

# or doing in one shot
MyClass.__dict__['say_hello']()  # hello world!

# using getattr()
getattr(MyClass, 'say_hello')()  # hello world!

# dot notation
MyClass.say_hello()              # hello world

#______________________________________________________________________________________
# Classes itself are callable
# when we create a class using the class keyword. 
# Python automatically adds behaviors to the class, in particular will
# add something to make the class callable. 
# the return value of that callable is an object. we call it an instance of the class

my_obj = MyClass()
type(my_obj)                # <class '__main__.MyClass'>
isinstance(my_obj, MyClass) # True

# Instantiating classes
# when we call a class, a class instance object is created and this
# class instance object has its own namespace.
# it is distinct from the namespace of the class that was used to create the object

# this object has some attributes that Python automatically implement for us, like:
# __dict__, __class__

class Program:
	language = 'Python'

	def say_hello():
		print(f'hello from {Program.language}')

Program.__dict__  # {..., 'laguage': 'Python', 'say_hello': <function...>}
# class namespace

p = Program()
p.__dict__        # {} 
# instance object namespace

type(p)           # <class '__main__.Program'>
p.__class__       # <class '__main__.Program'>

# we should use type(), cause we can modify the __class__ attribute like:
class C:
	__class__ = str

obj = C()

type(obj)      # <class '__main__.C'>  safer to use type()
obj.__class__  # str

# but take a look at isinstance() now:
isinstance(obj, C)    # True
isinstance(obj, str)  # True
isinstance(obj, int)  # False

#__________________________________________________________________________________

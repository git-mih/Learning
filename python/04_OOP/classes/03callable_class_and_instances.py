# Callable classes and class object instances:

# class objects itself are callable:
callable(type)    # True
callable(object)  # True
callable(str)     # True

class MyClass: pass
callable(MyClass) # True

# the return value of that callable is an object (object instance):
o = MyClass()          # <__main__.MyClass object at 0x0001>
isinstance(o, MyClass) # True

#_________________________________________________________________________________________________
# instantiating classes (object instances):

# class instances have its own namespace. its namespace is distinct from the namespace of the 
# class object that was used to create the object instance.

class Program:
	language = 'Python'
	def say_hello():
		print(f'{Program.language} rocks')

# class namespace:
Program.__dict__
# {..., 
#   'laguage': 'Python', 
#   'say_hello': <function Program.say_hello at 0x1234>
# }


# instantiating:
p = Program()  # <__main__.Program object at 0x0001>

# object instance namespace:
p.__dict__  # {} 

#_________________________________________________________________________________________________
# obj.__class__ vs type(obj):

# is safer to use 'type(obj)' to check the real class of an particular object.

# it happens because we could modify the __class__ attribute of the class object:
class Person:
	__class__ = str

p = Person() # <__main__.Person object at 0x001>

type(p)     # <class '__main__.Person'>
p.__class__ # <class 'str'>

# it is basicly inheriting from both:
isinstance(p, Person) # True
isinstance(p, str)    # True

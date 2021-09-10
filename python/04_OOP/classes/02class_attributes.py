# Class Attributes (class level attributes):

# in addition to default Python attributes, we can add our custom attributes:
class MyClass:
	language = 'Python'
	version = '3.6'

# attribute names are strings:
MyClass.__dict__ # <class 'mappingproxy'>
# {'__module__': '__main__', 'language': 'Python', 'version': '3.6', ...}

#_________________________________________________________________________________________________
# Retrieving attribute values from objects:

class MyClass:
	language = 'Python'
	version = '3.6'

getattr(MyClass, 'language')  # Python
# getattr(MyClass, 'x')       # AttributeError 'MyClass' has no attribute called 'x'


# default argument value (if isnt avaiable):
getattr(MyClass, 'x', 'N/A')  # N/A


# dot notation:
MyClass.language # Python
# MyClass.x      # AttributeError 'MyClass' has no attribute called 'x'

#_________________________________________________________________________________________________
# Setting attribute values in objects:

class MyClass:
	language = 'Python'
	version = '3.6'

setattr(MyClass, 'version', '3.7')
MyClass.version = '3.7'

#_________________________________________________________________________________________________
# Deleting attributes:

class MyClass:
	language = 'Python'
	version = '3.6'

delattr(MyClass, 'language')
del MyClass.version

#_________________________________________________________________________________________________
# callable attributes:
class MyClass:
	def say_hello(): 
		return 'hey'

MyClass.__dict__ 
# {..., 
#   'say_hello': <function __main__.MyClass.say_hello()>
# }

# using namespace to access:
MyClass.__dict__['say_hello']() # hey

# getattr:
getattr(MyClass, 'say_hello')() # hey

# dot notation
MyClass.say_hello()  # hey

#_________________________________________________________________________________________________
# Accessing attributes directly in the namespace of the object:

class MyClass:
	language = 'Python'
	def say_hello():
		return 'hey'

MyClass.__dict__['language']   # Python
MyClass.__dict__['say_hello']  # <function MyClass.say_hello at 0x0001>

# although this isnt a regular dictiorary, its a mapping object, we can use its methods:
list(MyClass.__dict__.items()) 
# [
#   (...), 
#   ('language', 'Python'), 
#   ('say_hello', <function MyClass.say_hello at 0x0001>)
# ]


# the __dict__ attribute returns a mappingproxy (dict like) object that cant be modified:
MyClass.__dict__['language'] = 'Perl'    # TypeError: 'mappingproxy' doesnt support it.

# also, not everything is stored inside the __dict__ attribute.

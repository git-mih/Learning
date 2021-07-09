# defining Attributes in Classes (class context only)

class MyClass:
	language = 'Python'
	version = '3.6'

# in addition to whatever attributes python automatically creates for us, 
# it also has language and version attributes now.

# attribute names are always strings.

# Retrieving attribute values from objects
getattr(MyClass, 'language')  # Python
# getattr(MyClass, 'x')       # AttributeError 'MyClass' has no attribute called 'x'
getattr(MyClass, 'x', 'N/A')  # N/A
# or
MyClass.language # Python
# MyClass.x      # AttributeError 'MyClass' has no attribute called 'x'
# dot notation doesnt have an equivalent to default value like getattr()

# Setting attribute values in objects
setattr(MyClass, 'version', '3.7')
# or
MyClass.version = '3.7'

# this has modified the state of MyClass. MyClass was mutated
getattr(MyClass, 'version') # 3.7
MyClass.version             # 3.7

# Python is dynamic, if we try to set an attribute that we didnt 
# defined in our class, it will automatically set for us.
setattr(MyClass, 'x', 100)
MyClass.y = 200

getattr(MyClass, 'x') # 100
getattr(MyClass, 'y') # 200

#______________________________________________________________________________________
# Where is the state stored? in a dictionary
class MyClass:
	language = 'Python'
	version = '3.6'

MyClass.__dict__ # {..., 'language': 'Python', 'version': '3.6'}

type(MyClass.__dict__) # <class 'mappingproxy'>
# mappingproxy isnt of type dict, but its still being a dictionary, a hash map 
# we can thing about it as a read only hash map. python does it to make sure that
# all keys are strings.

# this hash map (dictionary) is the object namespace.

# it is not directly mutable, we cant mutate this mappingproxy by adding key and values
# # or modifying existing ones directly. 
# but we can do it with setattr().

# Mutating attributes
class MyClass:
	language = 'Python'
	version = '3.6'

MyClass.__dict__ # {..., 'language': 'Python', 'version': '3.6'}
setattr(MyClass, 'x', 100)
MyClass.y = 200  # shorthand

# this was reflected in the namespace
MyClass.__dict__ # {..., 'language': 'Python', 'version': '3.6', 'x': 100, 'y': 200}


# Deleting attributes
delattr(MyClass, 'x')
del MyClass.y    # shorthand

MyClass.__dict__ # {..., 'language': 'Python', 'version': '3.6'}


# Accessing the namespace directly

# as we saw the class namespace uses a dictionary, which we can request 
# using __dict__ attribute of the class that returns a mappingproxy object. 
# we cant modify directly, but we can read it.
# although this isnt a dict, it still a hash map (dictionary).

class MyClass:
	language = 'Python'
	version = '3.6'

getattr(MyClass, 'language')  # Python
MyClass.language              # Python

MyClass.__dict__['language']  # Python
# isnt commom practice. because not everything is stored in this dictionary.

# mappingproxy object behaves like a dict. 
list(MyClass.__dict__.items()) # [(...), ('language', 'Python'), ('version', '3.6')]

# but we can not try to modify it like we do with regular dict type
MyClass.__dict__['language'] = 'Perl'  # TypeError: 'mappingproxy' doesnt support it

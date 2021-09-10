# Initializing class instances

# when we create an object instance, by default python does two separate things:
# creates a new instance of the class
# initializes the namespace of the class

class MyClass:
	language = 'Python'

obj = MyClass()

# namespace of this object was also initialized and created the __dict__ and more
obj.__dict__    # {}

# we can provide a custom initializer method that python will use instead of its own.
class MyClass:
	language = 'Python'          # class attribute

	def __init__(self, version): # class attribute
		self.version = version

obj = MyClass('3.6')  
# when we call MyClass('3.6'), python creates a new instance of the object with 
# an empty namespace:
obj.__dict__  # {}

# if we have defined an __init__ function in the class, then it calls it next:
obj.__init__('3.6') 

# essentially Python is doing it:
MyClass.__init__(obj, '3.6')

# now our function runs and adds the 'version' attribute to the instance object namespace
obj.__dict__ # {'version': '3.6'}  # 'version' is an instance attribute

# by the time __init__ is called, Python has already created the instance object
# and a namespace for it.
# then __init__ is called as a method bound to the newly created instance object.

# __init__ isnt creating the object, its only running some code after the object
# instance has been created

#_________________________________________________________________________________________









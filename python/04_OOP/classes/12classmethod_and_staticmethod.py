# Class and static methods

# as we saw before, when we define a function in a class, how we call it will 
# alter his behavior
class MyClass:
	def hello():
		return 'hello'

obj = MyClass()

# the hello() function will be a regular function at class level
MyClass.hello    # <function MyClass.hello at 0x0000012CBBEFE550>
MyClass.hello()  # Hello

# the hello() function will be a method bound to the object instances.
obj.hello        # <bound method MyClass.hello of <__main__.MyClass object at 0x0000021>>
# obj.hello()    # TypeError: missing argument


# could we create a function in a class that will always be bound to the class itself
# and never be bound to the object instances?
# we want the hello() function to be a method bound to the class (MyClass).
# hello() function will still being a method bound to object instances of MyClass as well.

# for that, we require to use @classmethod.
class MyClass:
	@classmethod
	def hello(cls):
		return f'hello from {cls}'

MyClass.hello   # <bound method MyClass.hello of <class '__main__.MyClass'>>
# no longer a regular function, it is also a method bound to the MyClass object.

obj = MyClass()
# still being a method bound to the object instance
obj.hello       # <bound method MyClass.hello of <class '__main__.MyClass'>>

#___________________________________________________________________________________________
# Static methods

# we can define a function inside a class that will never be bound to 
# any object when called. to do that, we require to use the @staticmethod.

# these static methods will act like a regular function at class level and at
# object instance level.
class Circle:
	@staticmethod
	def help():
		return 'help avaiable'

Circle.help   # <function Circle.help at 0x000001A63B9AE670>   regular function

obj = Circle()
obj.help      # <function Circle.help at 0x000001A63B9AE670>   regular function
# same for the object instance perspective.

# NOTE:
# static methods are not commonly used. also, some Python devs actually discourage
# using static methods. is better to use regular functions defined outside the class.

# sometimes can be useful, it wrapps everything together inside the class.
# even though we can import everything at module level, could be nice to import just
# a class and this class came with regular functions bundled
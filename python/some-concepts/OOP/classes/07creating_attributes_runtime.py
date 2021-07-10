# Setting function attributes in object instances at runtime

# we saw that we can add to an instance namespace directly at runtime by using
# setattr() or the dot notation.

class MyClass:
	language = 'Python'

obj = MyClass()

obj.__dict__   # {}
obj.version = '3.7'
obj.__dict__   # {'version': '3.7'}

# what happens if we create a new attribute whose value is a function?
obj.say_hello = lambda: 'hello world'

# as we saw before, it is a regular function type not a bound method.
obj.say_hello       # <function <lambda> at 0x000001F7A2CEE550>
type(obj.say_hello) # <class 'function'>
obj.say_hello()     # hello world

# the problem is that, the say_hello does not have access to the instance namespace

# how do we add a bound method to our instance object directly? without having to 
# define it in the class?
# because sometimes we want a bound method in a particular object instance only. 
# cause if we define say_hello inside the class, it will works, but every 
# object instance of that class is going to have that say_hello method.

# can we create and bind a method to an instancel at runtime? sure.
# we just need to define a method that binds the function to the object instance
class MyClass:
	language = 'Python'

obj = MyClass()
obj.__dict__     # {}

from types import MethodType
# MethodType(function, instance_object)
# the function we want to bind
# the object to bind to

obj.say_hello = MethodType(lambda self: f'hello {self.language}!', obj)
#                                   function                   instance obj

# so now, say_hello is a method bound to the object instance (obj)

obj.__dict__
# {'say_hello': <bound method <lambda> of <__main__.MyClass object at 0x000001F17844CD90>>}

obj.say_hello() # hello Python!

# only the object instance (obj) has been affected. no other object instances 
# have that method.

#___________________________________________________________________________________________












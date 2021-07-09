# Function Attributes (classes and isntance context)

# when attributes are functions is different than data attribtues like str, int, etc.
class MyClass:
	def say_hello():
		print('hello world')

MyClass.say_hello   # <function MyClass.say_hello at 0x00000211FFA7E5E0>
MyClass.say_hello() # hello world

my_obj = MyClass()
my_obj.say_hello    # <bound method MyClass.say_hello of 
#                        <__main__.MyClass object at 0x00000211FFA7E5E0>

# my_obj.say_hello() # TypeError: say_hello() takes 0 arguments but 1 was given

# why we got error? bound method? what is a method?

#___________________________________________________________________________________
# Methods
# is an actual object type in python. like a function, its also callable.
# but unlike a function, it is bound to some object.

# my_obj.say_hello() 
# 	say_hello is a method object. it is bound to the object instance. 

# when my_obj.say_hello is called, the bound object (my_obj) is injected
# as the first parameter to the method say_hello. 

# Python essentially does it for us:
# MyClass.say_hello(my_obj)  TypeError: say_hello() takes 0 arguments but 1 was given

# one advantage of this is that,
# the say_hello function that we defined in the class, actually has a handle
# to the object that it was bounded to. so now we can actually looks what is inside
# that object namespace.


# Methods are objects that combine: instance object of some class and function.
# and like any object, it has attributes. 
# Python automatically provides some attributes for us, 
# in particular __self__ and __func__ attributes

# __self__ is actually the object instance which the method is bound to.
# __func__ is the original function that was defined in the class.

# whenever we call obj.method(args) it is basicly doing it:
# method.__func__(method.__self__, args)
#  original func  (object instance bounded   +    arguments)
#                  injected as 1st parameter

class Person:
	def hello(self): # self = p
		pass

p = Person()

p.hello.__self__ # <__main__.Person object at 0x0000028520F39E50>
p                # <__main__.Person object at 0x0000028520F39E50>

p.hello.__func__ # <function Person.hello at 0x000001A8F98EE700>
Person.hello     # <function Person.hello at 0x000001A8F98EE700>

#____________________________________________________________________________________
# means we have to account for that "extra" argument when we define functions in our
# classes. otherwise, we cant use them as methods bound to our instances.

# these functions are usually called instance methods.

# when we define a function inside a class, we usually always have the 1st argument
# being the bounded instance object, we commonly use (self) as convention.

# otherwise, we would never be able to use 'say_hello' from an instance object.
# only being able to use 'say_hello' from the class itself.


class MyClass:
	def say_hello(self):  # self = my_obj (instance object)
		print('hello world')

# whenever this code is compiled, the say_hello isnt a method object yet. as we saw
# before, it stills being a function inside MyClass that takes a single argument.
MyClass.say_hello 
# <function MyClass.say_hello at 0x00000219F845E700>

my_obj = MyClass()
# now we created an instance object of MyClass. and now if we look at
# my_obj.say_hello, at this point its a method object, and is bound to my_obj instance object.
my_obj.say_hello
# <bound method MyClass.say_hello of <__main__.MyClass object at 0x000001C23AEBCC70>>

# now we have an instance method
my_obj.say_hello() # hello world

#____________________________________________________________________________________
# of course functions in our classes can have their own parameters
# when we call the corresponding instance method with arguments, those arguments
# are passed to the methods as well. and the method still receives the 
# instance object reference as the 1st argument. it will ALWAYS be the 1st argument

class MyClass:
	language = 'Python'

    # say_hello function have access to whatever object instance it was called from
	def say_hello(self, name): # self = my_obj
		return f'hello {name}! i am {self.language}'
# that is very useful cause now we can start looking at attributes inside the instances
# not only the attributes inside the class object.

my_obj = MyClass()
my_obj.say_hello('fabio') # hello fabio! i am Python

# Python essentially did:
MyClass.say_hello(my_obj, 'fabio') # hello fabio! i am Python
# 'say_hello' tryed to find the 'language' attribute inside the instance object namespace
# and did not find it, then it looked at the class namespace and found.

# adding language attribute to the object instance namespace
my_obj.__dict__ # {}
my_obj.language = 'Perl'
my_obj.__dict__ # {'language': 'Perl'}

my_obj.say_hello('fabio') # hello fabio! i am Perl
# 'say_hello' looked at the object instance namespace and found the 'language' attribute

# Python essentially did:
MyClass.say_hello(my_obj, 'fabio') # hello fabio! i am Perl

#____________________________________________________________________________________









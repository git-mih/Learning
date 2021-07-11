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
from types import MethodType

class Person:
	def __init__(self, name):
		self.name = name

p1 = Person('fabio')  # p1.__dict__   {'name': 'fabio'}
p2 = Person('joel')   # p2.__dict__   {'name': 'joel'}

# 
p1.say_hello = MethodType(lambda self: f'{self.name} says hello', p2)
# we are pointint to the instance object (p2). it is essentialy doing:
# p1.say_hello(p2)
# where self = p2  and  p2.name = 'joel'

p1.say_hello() # joel says hello
#___________________________________________________________________________________________
class Person:
	def __init__(self, name):
		self.name = name

	def register_do_work(self, fn):
		# registring the method into the instance object
		self.work = MethodType(fn, self) 
		# math_teacher.work = MethodType(work_of_math, math_teacher)

	def do_work(self):
		# getting the work attribute in the object instance
		do_work_method = getattr(self, 'work', None) # if not avaiable, set to None

		if do_work_method: # if avaiable, call the method 
			return do_work_method() # math_teacher.work()
		else:              # if 'work' attribute not found, we should register one.
			raise AttributeError('must first register a do_work method.')

math_teacher = Person('Eric')
english_teacher = Person('John')

math_teacher.__dict__    # {'name': 'Eric'}
english_teacher.__dict__ # {'name': 'John'}

# math_teacher.do_work()   # AttributeError: must first register a work method
# Eric doesnt have the: 'work': <bound method>  attribute.

# function we gonna register as a method into the math_teacher namespace 
def work_of_math(self):
	return f'{self.name} will teach geometry today.'

# calling the register function:  
math_teacher.register_do_work(work_of_math)
# Python essentially doing:
Person.register_do_work(math_teacher, work_of_math)

math_teacher.__dict__
# {'name': 'Eric', 
#  'work': <bound method work_of_math of <__main__.Person object at 0x000001FE3F1CFB80>>}

# now we can call
math_teacher.do_work()   # Eric will teach geometry today.

#__________________________________________________________________________________________
def work_of_english(self):
	return f'{self.name} will analyze Hamlet today.'

english_teacher.register_do_work(work_of_english)

english_teacher.do_work() # John will analyze Hamlet today.

# we are registring different functionalities by calling the same say. the plugins
# are different but they are called the same way.
teachers = [math_teacher, english_teacher]
for t in teachers:
	t.do_work()

# Eric will teach geometry today.
# John will analyze Hamlet today.

# we could implement it with inheritence and metaclass concept. but this approach
# is clean and simpler.
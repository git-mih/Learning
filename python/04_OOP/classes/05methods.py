# Callable attributes (function and methods):

class MyClass:
	def say_hello():
		return 'hey'

MyClass.say_hello # <function MyClass.say_hello at 0x01>

o = MyClass()
o.say_hello       # <bound method MyClass.say_hello of <__main__.MyClass object at 0x01>

# o.say_hello()     # TypeError: say_hello() takes 0 arguments but 1 was given

#______________________________________________________________________________________________
# methods:

# is another callable Python object, a function like object. but unlike a function object, 
# an method is a function that is bound to some object.

# any object instance have its own namespace, therefore, we can have different attribute values
# for each object instance of the same class. and methods allow us to look for attributes that
# is inside the instances, not only inside the class namespace.

class Person:
	def say_hello():
		return 'hey'

Person.say_hello # <function Person.say_hello at 0x04>

p = Person()     # <__main__.Person object at 0x01>

# by default, Python will bound callable attributes to object instances:
p.say_hello      # <bound method Person.say_hello of <__main__.Person object at 0x03>>

# Python will essentially creates a new method object, creates a reference to the original
# function object, and bound that method object to the instance that was created.

# it means that, if we try to call that function from an instance, Python will essentially 
# pass that instance as first arguent to the function:
Person.say_hello(p)  # TypeError: say_hello() takes 0 positional arguments but 1 was given


#______________________________________________________________________________________________
# method instospection:

# methods are objects, and like any other object, it has attributes, in particular: 
#   - __self__: is a reference to the object instance that the function object is binding.
#   - __func__: is a referencee to the original function object that was defined in the class.

p = Person()         # <__main__.Person object at 0x01>
p.say_hello          # <bound method Person.say_hello of <__main__.Person object at 0x02>>

# getting original function object:
p.say_hello.__func__ # <function Person.say_hello at 0x04>
Person.say_hello     # <function Person.say_hello at 0x04>

# getting the object that the method is binding to:
p.say_hello.__self__ # <__main__.Person object at 0x01>

#____________________________________________________________________________________________________
# defining an instance method:

class Person:
	# receiving the instance as first argument:
	def say_hello(self):
		return 'hey'

p = Person()         # <__main__.Person object at 0x001>
p.say_hello          # <bound method Person.say_hello of <__main__.Person object at 0x02>>
p.say_hello.__self__ # <__main__.Person object at 0x001>

Person.say_hello     # <function Person.hello at 0x004>
p.say_hello.__func__ # <function Person.hello at 0x004>


# calling the bound method: (instance binding to the function object):
Person.say_hello(p)  # hey

#___________________________________________________________________________________________________
# self:

# if we want the class instances to be able to call its functions, we require to add that extra 
# argument when we defining functions inside our class. otherwise, we cant use them through 
# instances.

class MyClass:
	def say_hello(self):
		return 'hey'

# that function object will only be an method to the instances:
MyClass.say_hello # <function MyClass.say_hello at 0x001>

# once Python create a new object instance, that function is bound to that instance:
o = MyClass()
o.say_hello       # <bound method MyClass.say_hello of <__main__.MyClass object at 0x002>>


# passing arguments to instance methods:
class MyClass:
	language = 'Python'

	def say_hello(self, name):
		return f'hello {name} im {self.language}'

# it allow us to look for attributes inside instances, not only inside the class namespace.
o = MyClass()  # <__main__.MyClass object at 0x001>

# that instance method have access to whatever object instance it was called from:
MyClass.say_hello(o, 'fabio') # hello fabio, im Python
o.say_hello('fabio')          # hello fabio, im Python

# 'say_hello' first tries to find that symbol 'language' inside the instance namespace, then it 
# looks in the enclosing scope (class namespace), find that and use that attribute value.


# adding attribute inside the instance namespace:
o.__dict__ # {}
o.language = 'Perl'
o.__dict__ # {'language': 'Perl'}

o.say_hello('fabio')          # hello fabio, im Perl


# setting attributes through instance method:
class Person:
	def set_name(self, name_value):
	  	setattr(self, 'name', name_value)

p = Person()  # <__main__.Person object at 0x001>
p.__dict__    # {}

# setting attribute inside the object instance namespace
p.set_name('Amy')
p.__dict__    # {'name': 'Amy'}

# essentially:
Person.set_name(p, 'Amy')
p.__dict__    # {'name': 'Amy'}

#___________________________________________________________________________________________________
# adding new methods to instances by defining new function objects inside the class namespace:

class Person: pass

p1 = Person()  # <__main__.Person object at 0x001>
p2 = Person()  # <__main__.Person object at 0x002>

# defining a new class attribute (function) inside the class namespace:
Person.say_hello = lambda self: f'called from {self}'
Person.__dict__
# {..., 
#   'say_hello': <function <lambda> at 0x006>
# }

# that function object will be bound to existing instances:
p1.say_hello   # <bound method <lambda> of <__main__.Person object at 0x001>>
p2.say_hello   # <bound method <lambda> of <__main__.Person object at 0x002>>

p1.say_hello() # called from <__main__.Person object at 0x001>
p2.say_hello() # called from <__main__.Person object at 0x002>

#___________________________________________________________________________________________________
# defining instance attributes as bare function objects:

# when Python finds a function defined at class level being called from an instance, Python
# transform that function into a method bound to that instance as we saw.

# but we could define a function object directly inside the instance namespace:
# Python is going to treat that function as a regular function attribute.
class Person:
	def say_hello(self): pass

p = Person() # <__main__.Person object at 0x001>
p.say_hello  # <bound method Person.say_hello of <__main__.Person object at 0x001>>

# defining a function inside the object instance namespace directly
p.__dict__   # {}
p.say_bye = lambda: 'bye bye'

p.__dict__   # {'say_bye': <function <lambda> at 0x1234>}
p.say_bye()  # bye bye

# Overriding functionality

# when we inherit from another class, we inherit itss attributes, including all callables.
# we can choose to redefine an existing callable in the subclass

class Person:
	def say_hello(self):
		return 'hello!'

	def say_bye(self):
		return 'bye!'

class Student(Person):
	def say_hello(self): # overriding parent method
		return 'yoo!'

# when we create any class, we can override any method defined 
# in the parent class, including inherited ones, including those 
# defined in object class, such as __init__, __repr__, __eq__ etc...

#______________________________________________________________________________
# Tip
# __class__   # returns class of the object was created from
# __name__    # returns a string containing the name of the class

# to get the name of the class used to create an object:
class Person:
	pass

p = Person()
p.__class__.__name__ # Person  (string representation of class name)

# instead of hard code the __repr__ with the class name like:
# class Person:
# 	def __init__(self):
# 		self.name = name

# 	def __repr__(self):
# 		return f"Person(name='{self.name}')"  # like so

# we could do this way
class Person:
	def __init__(self, name):
		self.name = name
	
	def __repr__(self):
		return f"{self.__class__.__name__}(name='{self.name}')"

# and now, if we inherit from Person, we have this dynamic functionality
class Student(Person):
	pass

# we're going to inherit the __init__ and __repr__ from Person, and the remaining
# methods from object class

s = Student('fabio')
# print(s)      Student(name='fabio')

#______________________________________________________________________________


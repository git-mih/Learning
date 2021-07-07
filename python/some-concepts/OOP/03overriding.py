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
class Person:
	def __init__(self, name):
		self.name = name
	
	def eat(self):
		return 'eating'
	
	def work(self):
		return 'working'
	
	def sleep(self):
		return 'sleeping'
	
	def routine(self):
		self.eat()
		self.work() # its going to call s.work() method and not Person.work()
		self.sleep()

class Student(Person):
	def work(self):
		return 'studying'

s = Student('fabio')
s.eat()   # eating   -> calls Person.eat() method
s.work()  # studying -> calls s.work() method

s.routine() # eating, studying, sleeping
# Person.routine() -> Person.eat() -> s.work() -> Person.sleep()


# its the same mechanism that happens with __str__ or __repr__
class Person:
	def __repr__(self):
		return 'Person() with extra debugging info'

p = Person()

str(p)       # Person() with extra debugging info
p.__str__()  # Person() with extra debugging info

# we are not implementing __str__ method in Person, so it is going to call
# the object.__str__() method from object class. 
# object class would call object.__repr__() method but
# Person do have the __repr__ method implemented.
# so it is going to call it, is going to call p.__repr__() instead object.__repr__()

# str(p) -> p.__str__() -> object.__str__() -> p.__repr__()

#_________________________________________________________________________________-
# another exemple
class Person:
	def __str__(self):
		return self.__repr__() # calling s.__repr__() and not Person.__repr__()

	def __repr__(self): # not being used
		pass

class Student(Person):
	def __repr__(self):
		return 'Student.__repr__ called'

s = Student()

repr(s) # Student.__repr__ called
# calling s.__repr__() directly

str(s)  # Student.__repr__ called
# calling Person.__str__() -> s.__repr__()


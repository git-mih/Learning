# Delegating to parent

# often when overriding methods, we need to delegate back to the parent class
# the most commom example is the __init__ method

class Person:
	def __init__(self, name, age):
		self.name = name
		self.age = age

class Student(Person):
	def __init__(self, name, age, major): # getting name and age again?
		self.name = name                  # there has to be a better way.
		self.age = age
		self.major = major  # extending with major attribute

# a better way of doing it is by using the super() function.
# we can explicitly call a method from the parent class by using super()
# super() is going to delegate to parent class

# super().method()
# its going to call the method of ancestor, no matter if we overrided some method or not
# it is going to go back to the parent and ask to run this particular method
# but, of course, it will still be bounded to the instance its called from

class Person:
	def sing(self):
		return "I'm a lumberjack and I'm ok"

class Student(Person):
	pass

class MusicStudent(Student):
	def sing(self):
		return super().sing() + '\n I sleep all night and I work all day'

# delegation works its way up the inheritence hierarchy until it finds what it needs.

s = MusicStudent()
s.sing()  # I'm a lumberjack and I'm ok
#           I sleep all night and I work all day

#____________________________________________________________________________________
class Person:
	def __init__(self, name, age):
		self.name = name
		self.age = age

class Student(Person):
	def __init__(self, name, age, major): # we still have to capture name and age
		super().__init__(name, age) # delegate back to parent
		self.major = major          # and do some additional work

# when delegating, we dont have to delegate first
# we could assign self.major = major before the super().__init__() but its not very safe to do.

#____________________________________________________________________________________
# delegation and method binding

# when we call a method from an instance, the method is bound to the instance.
# when we delegate from an instance to parent method, the method is still bound to the
# instance it was called from

class Person:
	def hello(self):
		print('in Person class: ', self) # self = s

class Student(Person):
	def hello(self):
		print('in Student class: ', self)
		super().hello()  # is going to do call Person.hello(s)

p = Person()
p.hello() # in Person class:  <__main__.Person object at 0x00000227E34CFA00>
# self = p

s = Student()
s.hello()
# self = s
# in Student class:  <__main__.Student object at 0x00000259C7C9F9D0>
# in Person class:   <__main__.Student object at 0x00000259C7C9F9D0>

# since delegated method are bound to the calling instance, any method called
# from the parent class will use the calling instance 'version' of the method.

#____________________________________________________________________________________

class Person:
	def set_name(self, value):
		# Setting name using Person.set_name() method
		self.name = value  # storing into s.name  (self = s)

class Student(Person):
	def set_name(self, value):
		# Student class delegating back to parent and passing the value received
		super().set_name(value)

s = Student()
s.set_name('fabio')

s.__dict__   # {'name': 'fabio'}
# it get stored in the instance namespace, and not in the Person.__dict__

# its very handy that we can use this principle inside __init__ 
class Person:
	def __init__(self, name): 
		self.name = name       # self = s   // s.name = 'fabio'

class Student(Person):
	def __init__(self, name, student_number): 
		super().__init__(name) # parent __init__ expect the name arg only
		self.student_number = student_number    # s.student_number = 26

s = Student('fabio', 26)

s.__dict__  # {'name': 'fabio', 'student_number': 26}

# what if we only have the __init__ on parent class?
class Person:
	def __init__(self, name): # expecting 1 positional arg
		self.name = name

class Student(Person):
	pass

# s = Student()  # TypeError __init__() missing 1 required arg
s = Student('fabio')

s.__dict__  # {'name': 'fabio'}

# its like:
Person.__init__ is object.__init__  # True
p = Person()  # it works, cause it is going to use the parent __init__ method if
#               we dont pass any argument.
p = Person('python')  # now it is using the Person.__init__
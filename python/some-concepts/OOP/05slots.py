# Slots

# remember that instance attributes are normally stored in a local dict of class instances
class Point:
	def __init__(self, x, y):
		self.x = x
		self.y = y

p = Point(0, 0)

# as we know, there is a certain memory overhead with dictionaries
p.__dict__  # {'x': 0, 'y': 0}

# so what happens if we have thousands of instances of points? rip...
# Python3.3 introduced key sharing dictionaries to help alleviate this problem

# but, even better than that, is the Slots.
# We can tell python that a class will contain only certain pre-determined attributes
# python will then use internaly a more compact data structure to store attribute values.

class Point:
	__slots__ = ('x', 'y') # an iterable containing the attribute names we will use in our class
	def __init__(self, x, y):
		self.x = x
		self.y = y
# we're telling python that we are using slots and not the default dictionary and these
# are the instance attributes we are going to use 'x' and 'y'.	

p = Point(0, 0)
# p.__dict__   # AttributeError: Point object has no attribute __dict__
# vars(p)      # TypeError: vars() argument must have __dict__ attribute

dir(p) # [..., 'x', 'y']
p.x       # 0    
p.x = 100 
p.x       # 100

# memory savings, even compared to key sharing dicts, can be substantial.
# using slots results in generally faster operations (on avg)

# but we should not use slots all the time. why?
# if we use slots, then we cannot add attributes to our objects that are not defined in slots.
# we cant monkey patch anymore.
class Point:
	__slots__ = ('x', 'y')
	def __init__(self, x, y):
		self.x = x  # it is legal to do, cause 'x' and 'y' is defined on __slots__
		self.y = y
#       self.z = 100   # AttributeError: 'Point' object has no attribute 'z'

p = Point(0, 0)

# p.z = 100            # AttributeError: 'Point' object has no attribute 'z'
# setattr(p, 'z', 100) # AttributeError: 'Point' object has no attribute 'z'

# also can cause difficulties in multiple inheritance

#_____________________________________________________________________________________________
class Location:
	__slots__ = 'name', '_longitude', '_latitude'

	def __init__(self, name, longitude, latitude):
		self._longitude = longitude
		self._latitude = latitude
		self.name = name
	
	@property
	def longitude(self):
		return self._longitude

	@property
	def latitude(self):
		return self._latitude

Location.map_service = 'Google Maps'
# Slots doesnt lock class atributes, we still can create new class attributes.

l = Location('Mumbai', longitude=19.9768, latitude=72.8777)
# l.__dict__    AttributeError 'Locations' object has no attribute '__dict__'
# and the instance no longer have the __dict__ attribute.

# but it will lock the instance attributes. at run-time, we are no longer able to
# add attributes beside (name, _longitude, _latitude) that was defined in slots.

# l.map_link = 'https://...'  # AttributeError as well

# but we can still playing with these defined attributes
del l.name
l.name = 'London'
l._longitude = 30.1234



#_____________________________________________________________________________________________
# Slots and single inheritence
# what happens if we create a base class with slots and extend it? creating a subclass?
class Person:
	__slots__= 'name',

class Student(Person):
	pass

s = Student()

s.name = 'Alex'
s.__dict__  # {}  exists, now we also have an instance dict 
#                 but the name isnt stored in the __dict__ attribute.

# in fact, we could assign new attributes to the instance now. but, these attributes
# will be stored inside __dict__
s.age = 18
s.__dict__  # {'age': 18}

# so, subclasses will use slots from the parents (if present), and will also use an
# instace dict.

# what if we want our subclass to also just use slots?
# we just require to specify __slots__ in the subclass, only specifying the additional ones.
class Person:
	__slots__ = 'name',

class Student(Person): 
	__slots__ = 'age', # Students will now use slots for both name and age.


# we can also define slots but inherits from a parent that does not have slots
class Person:
	pass

class Student(Person):
	__slots__ = 'name', 'age'  # Student will use slots for name and age

s = Student()

s.name = 'fabio'  # stored in slots
s.age = 26        # stored in slots

s.__dict__   # {}
# but an instance dictionary will always be present too.

#________________________________________________________________________________________________
# how are slotted attributes different from properties?
# a slotted attribute isnt stored in an instance dictionary
# properties are also not in an instance dictionary
class Useless:
	@property
	def useless(self):
		return 'useless!'
	
	@useless.setter
	def useless(self, value):
		pass

obj = Useless()

obj.useless     # 'useless!'
obj.useless = 'something else'

obj.__dict__    # {} 
# we can see we do have an instance dict, but doesnt contain the useless property on it.

# they are not different. in fact, both use data descriptors.
# in both cases, the attributes are present in the class dictionary dir(),
# but with slots it essentially create properties (getters, setters, deleters 
# and storage) for us.

# the best of both worlds
# slots        -> faster attribute access, less memory
# intance dict -> can add attributes arbitrarily at run-time

# we can specify __dict__ as a slot an get both working togheter.
class Person:
	__slots__ = 'name', '__dict__'

# now we still can add attributes at run-time, these new attributes will be stored 
# inside the instance dictionary (__dict__)
p = Person()
p.name = 'Fabio' # slot
p.age = 26       # p.__dict__  {'age': 26}

#_____________________________________________________________________________________________
class Person:
	def __init__(self, name): # self = s
		self.name = name      # s.name = 'fabio'

class Student(Person):
	pass

p = Person('john')
p.__dict__   # {..., 'name': 'john'} 

s = Student('fabio')
s.__dict__   # {'name': 'fabio'}

class Person:
	__slots__ = 'name',   # Person.__dict__ no longer avaiable.

	def __init__(self, name):
		self.name = name

class Student(Person):
	pass

p = Person('john')
# p.__dict__   AttributeError 'Person' object has no attribute '__dict__'

s = Student('fabio')
s.__dict__   # {}

# to make subclasses mimic this behavior we could provide an slot with empty tuple
class Person:
	def __init__(self, name): # self = s
		self.name = name      # s.name = 'fabio'

class Student(Person):
	__slots__ = tuple()  # not useful

s = Student('fabio')
# s.__dict__   AttributeError 'Student' object has no attribute '__dict__'

class Person:
	__slots__ = 'name', '__dict__'  # we will be able to add new attributes at run-time

	def __init__(self, name):
		self.name = name

p = Person('john')
p.__dict__  # {}
p.age = 76
p.__dict__  # {'age': 76}

# another way
class Person:
	__slots__ = 'name', '__dict__'

	def __init__(self, name, age):
		self.name = name
		self.age = age   # age isnt defined on slots. it is going to be added to __dict__

p = Person('fabio', 26)
p.__dict__    # {'age': 26}
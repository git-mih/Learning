# The hash value is calculated based on the object ID's (mem address).
# it means, if we have different objects that points to a same object, all these
# objects will have the same hash value. Also known as a Collision.

t1 = (1, 2, 3)
t2 = (1, 2, 3)
# t1 is t2   False, they are different objects

d = {t1: 100} # dict key is based on hash value only
# d[(1, 2, 3)]  100
# d[t1]         100
# d[t2]         100  also works, both t1 and t2 have the same hash values
# hash(t1) 529344067295497451 
# hash(t2) 529344067295497451

#__________________________________________________________________________________
# By default, python automatically calculate a hash to our custom objects based on their ID's
# but we can disable it by specifying:  __hash__ = None
class Person:
	__hash__ = None

	def __init__(self, name, age):
		self.name = name
		self.age = age
p1 = Person('jhon', 78)  # hash(p1)   TypeError: unhashable type: 'Person'

#__________________________________________________________________________________
class Person:
	def __init__(self, name, age):
		self.name = name
		self.age = age

	def __repr__(self):
		return f'Person(name={self.name}, age={self.age})'

p1 = Person('jhon', 78) # p1 is p2  False
p2 = Person('jhon', 78) # p1 == p2  False we arent specifying __eq__
# hash(p1) 110502808793 // id(p1) 0x001
# hash(p2) 110502808787 // id(p2) 0x004
# python by default automaticaly provide hash to our custom objects
# 	based on their memory location

# they being hashables, we can use these objects as keys
p1 = Person('jhon', 78)
p2 = Person('eric', 73)

d = {p1: 'jhon obj', p2: 'eric obj'}
# d[p1]   Person(name=jhon, age=78)

# d[Person('jhon', 78)]   KeyError  
# 	they are not equal (==) p1 and Person('jhon', 78). therefore, we cant
#   access the key value by doing this way.

#__________________________________________________________________________________
# To be able to pass any instance of the Person class that have equality
# we should define what equality means to that Class by implementing __eq__ method.
class Person:
	def __init__(self, name, age):
		self.name = name
		self.age = age

	def __repr__(self):
		return f'Person(name={self.name}, age={self.age})'

	def __eq__(self, other):
		if isinstance(other, Person):
			return self.name == other.name and other.name == other.age
		else:
			return False

p1 = Person('jhon', 78) # p1 is p2   False
p2 = Person('jhon', 78) # p1 == p2   True    both are equal now, but...

# once we defined the __eq__ method, python is no longer avaiable to provide
# hash values automaticaly. Now we have to implement the __hash__ to calculate a hash value
# based on our requirements

# d = {p1:'jhon obj'}    TypeError: unhashable type: 'Person'

#__________________________________________________________________________________
class Person:
	def __init__(self, name, age):
		self.name = name
		self.age = age

	def __repr__(self):
		return f'Person(name={self.name}, age={self.age})'

	def __eq__(self, other):
		if isinstance(other, Person):
			return self.name == other.name and other.name == other.age
		else:
			return False
	
	def __hash__(self): # providing a constant hash.
		return 100      # lot of collisions are going to happen (dont do it)
	
p1 = Person('jhon', 78)  # hash(p1)   100
p2 = Person('eric', 73)  # hash(p2)   100
p3 = Person('ada', 62)   # hash(p3)   100

#__________________________________________________________________________________
class Person:
	def __init__(self, name, age):
		self.name = name
		self.age = age

	def __repr__(self):
		return f'Person(name={self.name}, age={self.age})'

	def __eq__(self, other):
		if isinstance(other, Person):
			return self.name == other.name and self.age == other.age
		else:
			return False
	
	def __hash__(self): # hashing a tuple ('jhon', 78)
		return hash((self.name, self.age))

p1 = Person('jhon', 78)  # hash(p1)   -5293842464448105660 
p2 = Person('jhon', 78)  # hash(p2)   -5293842464448105660 
# p1 == Person('jhon', 78)   True    it means, both have the same hash value
# p1 == p2   True
# p1 is p2   False

d = {p1: 'jhon obj'} 
# d[p1]   				'jhon obj'
# d[p2]   				'jhon obj'
# d[Person('jhon', 78)] 'jhon obj'

# NOTE:
# p1 was inserted inside the dict with this hash -5293842464448105660.
# if we modify p1.name, a new hash value is going to be calculated to p1.

# hash(p1)  -5293842464448105660.
# d[p1]     'jhon obj'

# p1.name = 'jane'

# hash(p1)   3241729229019408166
# d[p1]      KeyError

# p1 hash value was changed but, the hash stored inside the
# dict was the old p1 hash value. we cant access it anymore.

#__________________________________________________________________________________
# Tweaking the Class to allow us to mutate some properties of the object
# without changing the hash value.
class Person:
	def __init__(self, ID, name, age): 
		self._ID = ID
		self.name = name
		self.age = age

	def __repr__(self):
		return f'Person(id={self._ID}, name={self.name}, age={self.age})'

	def __eq__(self, other):
		if isinstance(other, Person):
			return self._ID == other._ID
		else:
			return False
	
	def __hash__(self): # calculating the hash based on the ID value now
		return hash(self._ID)

p1 = Person('1','jhon', 78)  # hash(p1)    1675986645556078305

d = {p1: 'jhon obj'}

# d[p1]                        'jhon obj'
# d[Person('1', 'jhon', 78)]   'jhon obj'

# p1.name = 'fabio'    mutating the p1 object
# p1.age = 26

# d[p1]      				   'jhon obj' 
# d[Person('1', 'jhon', 78)]   'jhon obj'   still can access it

# now the hash value stills the same. it was calculated based on the hash('1') value
# the ID. Not p1.name or p1.age anymore.

# hash(p1)    1675986645556078305

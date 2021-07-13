# Special methods: Hashing and equality

# if __eq__ method is implemented, __hash__ will be implicitly set to None unless we
# have implemented the __hash__ manually.

# by default when an override isnt specified like, we did not implemented the
# __eq__ method. the __hash__ will uses the ID of the object to create the hash value.

# and by default, if we dont implement the __eq__ method, the __eq__ will uses
# the identity comparasion (is) keyword. 

class Person:
	pass

p1 = Person() # hash(p1)  111111111111
p2 = Person() # hash(p2)  777777777777
p3 = p1       # hash(p3)  111111111111  
# p3 has same hash as p1, since the default __hash__ uses the memory address to 
# calculate the hash value.  

p1 == p2  # False
p1 is p2  # False
p1 is p3  # True   # same memory address


# if we think about the relationship between equality and hash, then if two objects
# are equal (==) they will have the same hash. and that is true in this case, because
# p1 is equal to p2 if they have the same memory address only. and if they do have
# the same memory address, both would have the same hash value.

class Person:
	def __init__(self, name):
		self.name = name

	def __eq__(self, other):
		return isinstance(other, Person) and self.name == other.name # True/False

	def __repr__(self):
		return f"Person(name='{self.name}')"

p1 = Person('Fabio')
p2 = Person('Fabio')
p3 = Person('Eric')

p1 == p2   # True  
# no longer comparing equality based on the memory address.
p1 is p2   # False

p1 == p3   # False
# we're comparing equality based in the object type and 'name' attribute.

# but now we have lost hashing, if we try to hash p1 we will get TypeError:

# hash(p1) # TypeError: unhashable type: 'Person'


# we now have to implement our own __hash__ implementation to be able to use it as
# a dict key. right now we cant do it, like:

# d = {p1: 'Fabio'}    # TypeError: unhashable type: 'Person'

# if we look at p1 hash value:
p1.__hash__            # None

#_____________________________________________________________________________________
# in many object instances we want things to be hashable.
class Person:
	def __init__(self, name):
		self.name = name

	def __eq__(self, other):
		return isinstance(other, Person) and self.name == other.name # True/False

	def __hash__(self):
    # the hash value will be based on the 'name' attribute of each object instance
		return hash(self.name) 

	def __repr__(self):
		return f"Person(name='{self.name}')"

p1 = Person('Fabio')
p2 = Person('Fabio')

p1 == p1 # True

# the hash value is calculated based on the self.name now:
hash(p1) # 6052455116896250540  p1.name = 'Fabio'
hash(p2) # 6052455116896250540  p1.name = 'Fabio' as well

# now we are able to use it inside our dict as keys, like:
d = {p1: 'Fabio object'}
d = {Person('John'): 'John object'}

# also set
s = {Person('Fabio')} # {Person('fabio')}
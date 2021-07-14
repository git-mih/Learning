# Special methods: boolean

# every object in Python has an associated truth (boolean) value.
# for exemple, any non-zero number is considered Truthy.
# and the number is Falsy iff the number value is equal to 0.

# an empty collection is consider as Falsy as well. whenever we have a collection
# where the len() returns 0, it will be a False value.


# By default, any custom object also has a truth value. and we can override this by
# defining the __bool__ method. it must return either True or False.
class MyList:
	def __init__(self, x):
		self.x = x

	def __bool__(self):
		# return self.x != 0
		return bool(self.x)
	
	def __len__(self):
		return self.x

l1 = MyList(0)  # bool(l1)  False
l2 = MyList(7)  # bool(l2)  True



# if the __bool__ isnt defined, by defaut Python will looks for the __len__ method.
# and if the __len__ method exists and it returns 0, it will be False. anything else
# will be True.
class MyList:
	def __init__(self, x):
		self.x = x
	
 # as long we dont have the __bool__ defined, Python will then look to the __len__
	def __len__(self):
		return self.x

l1 = MyList(0)  # bool(l1)  False
l2 = MyList(7)  # bool(l2)  True



# if neither is present (__bool__ or __len__), the object will always return True. 
# By default, the truthyness of any object instance is True.
class Person:
	pass

p = Person()
bool(p)   # True
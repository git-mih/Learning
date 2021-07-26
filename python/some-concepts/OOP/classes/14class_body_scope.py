# Nested scopes in Class definitions

#------------------------------------------- module scope
class Python:
	#-------------------------- class body scope
	kingdom = 'animalia'
	phylum = 'chordata'
	family = 'pythonidae'

	def __init__(self, species):
		self.species = species
	
	def say_hello(self):
		return 'sssss...'
	#--------------------------

p = Python('monty')
#-------------------------------------------

# this module has its own (global) scope containing: 
# the symbol 'Python' which points to the class object. and 'p' which points to the
# object instance of that class.

# now inside the class we also have another scope going on. 
# it is really important to understand that the class body has its own scope.
# the Python class body has its own scope containing:
# kingdom, phylum, family, __init__ and say_hello.


# but what about the body scope of functions defined in the body of a class?
# like the __init__ and say_hello? __init__ and say_hello are just symbols present
# in the class namespace. these symbol itself points to some function objects.

# turns out that they are not inside the class body scope (namespace).
# just symbols (__init__, say_hello) are present in the class namespace. 

# the functions themselves are nested in the class's containing scope, in this case,
# the module scope.

# we can think about it this way:
#------------------------------------------- module scope
def callable_1(self, species):
	self.species = species

def callable_2(self):
	return 'sssss...'

class Python:
	#-------------------------- class body scope
	kingdom = 'animalia'
	phylum = 'chordata'
	family = 'pythonidae'

# when Python looks for a symbol in a function, it will never use the class body scope
	__init__  = callable_1
	say_hello = callable_2
	#--------------------------

p = Python('monty')

p.say_hello()     # sssss...
callable_2(p)     # sssss...
#-------------------------------------------


# in practical terms, it means:
class Account:
	COMP_FREQ = 12
	APR = 0.02   # 2%
	APY = (1 + APR/COMP_FREQ) ** COMP_FREQ - 1 # works because APR and COMP_FREQ
#                                        are symbols in the class body (namespace)
	def __init__(self, balance):
		self.balance = balance

	# this also works because we're telling Python where it have to go and looks for APY.
	def monthly_interest(self):
		return self.balance * self.APY 
	
	@classmethod
	# works cause we are referencing the class where the function needs to get the APY.
	def monthly_interest_2(cls, amount): 
		return amount * cls.APY

	@staticmethod
	# same
	def monthly_interest_3(amount): 
		return amount * Account.APY

	# def monthly_interest_4(self):
	# 	return self.amount * APY

	# this wont work, the function is defined at module level, once we call the function
	# Python will start looking in the module namespace for APY. APY isnt defined
	# at module level. we will get Error.



#__________________________________________________________________________________________
class Language:
	MAJOR = 3
	MINOR = 7
	REVISION = 4
	FULL = '{}.{}.{}'.format(MAJOR, MINOR, REVISION)
	# it will works, cause MAJOR, MINOR, REVISION are inside the class namespace.
	# we are not required to tell Python where it should go find MAJOR, MINOR etc.
	# we dont have to say self.MAJOR or Language.Major
Language.FULL    # 3.7.4


# now with functions inside the class body scope, if the attribute is pointing to a
# function, the function scope is not nested within the class body scope. we would
# require to specify self.attribute or cls.attribute or ClassName.attribute.

# we cant reference class attributes that are inside the functions 
# without telling Python that it have to look at an particular class namespace for it.
class Language:
	MAJOR = 3
	MINOR = 7
	REVISION = 4

	@property
	def version(self):
		return '{}.{}.{}'.format(self.MAJOR, self.MINOR, self.REVISION) 

l = Language()
l.version        # 3.7.4
# the version() function saw the self.MAJOR/MINOR and knew it should go
# and look for it inside the Language class. 

#_______________________________________________________________________________________
class Language:
	MAJOR = 3
	MINOR = 7
	REVISION = 4

	@property
	def version(self):
		return '{}.{}.{}'.format(self.MAJOR, self.MINOR, self.REVISION) 

	@classmethod
	def cls_version(cls):
		return '{}.{}.{}'.format(cls.MAJOR, cls.MINOR, cls.REVISION) 

	@staticmethod
	def static_version():
		return '{}.{}.{}'.format(Language.MAJOR, Language.MINOR, Language.REVISION) 

l = Language()

l.version                 # 3.7.4
Language.cls_version()    # 3.7.4
Language.static_version() # 3.7.4

# these functions knows where to find these class attributes MAJOR, MINOR, REVISION.
# cause we are telling python to go and looks into the 'Language.' namespace.

#_______________________________________________________________________________________
# Python is essentially doing it:
class Language:
	MAJOR = 3
	MINOR = 7
	REVISION = 4

def full_version():
	return '{}.{}.{}'.format(Language.MAJOR, Language.MINOR, Language.REVISION) 
# we could create the function outside the class namespace without problem. But
# we have to address the class namespace inside the function if we want to
# use the class attributes.

full_version()   # 3.7.4

#_______________________________________________________________________________________
# another way to visualize it:
class Language:
	MAJOR = 3
	MINOR = 7
	REVISION = 4
	version = full_version # pointer to the function object

def full_version():
	return '{}.{}.{}'.format(Language.MAJOR, Language.MINOR, Language.REVISION) 

Language.version()  # 3.7.4

Language.version is full_version  # True
#_______________________________________________________________________________________
MAJOR = 0
MINOR = 0
REVISION = 1

def gen_class():
	# gen_class namespace {'Language': <class>, 'MAJOR': 0, 'MINOR': 4, 'REVISION': 2}
	MAJOR = 0
	MINOR = 4
	REVISION = 2

	class Language:
		# Language namespace {'MAJOR': 3, 'MINOR': 7, 'REVISION': 4}
		MAJOR = 3
		MINOR = 7
		REVISION = 4

		@classmethod
		def version(cls):
			# this functions is containing in the gen_class() namespace.
			# it will 1st start looking for MAJOR, MINOR in the gen_class namespace,
			# it will happen cause we are not referencing where it should look for.
			return '{}.{}.{}'.format(MAJOR, MINOR, REVISION)

	return Language

cls = gen_class() # returns Language: <class '__main__.gen_class.<locals>.Language'>

cls.version()     # 0.4.2

#_______________________________________________________________________________________
MAJOR = 0
MINOR = 0
REVISION = 1

def gen_class():
	# gen_class namespace {'Language': <class>}
	class Language:
		MAJOR = 3
		MINOR = 7
		REVISION = 4

		@classmethod
		def version(cls):
			# now we dont have MAJOR, MINOR in the gen_class() body scope anymore.
			# Python will then search these values in the enclosing scope (module)
			return '{}.{}.{}'.format(MAJOR, MINOR, REVISION)

	return Language

cls = gen_class() 

cls.version()     # 0.0.1
#_______________________________________________________________________________________
name = 'Python'

class MyClass:
	name = 'Perl'
	list_1 = [name] * 3
	list_2 = [name for i in range(3)]  # list comprehension acts like a function

MyClass.list_1 # ['Perl', 'Perl', 'Perl']

MyClass.list_2 # ['Python', 'Python', 'Python']

# the list comprehension doesnt know it should look inside the MyClass namespace to
# get the value. it will look inside his own scope (module) and find the 'name' in there
# then will use it. 


name = 'Python'
class MyClass:
	name = 'Perl'
	list_1 = [name] * 3
	list_2 = [MyClass.name for i in range(3)]  # list comprehension acts like a function

MyClass.list_1 # ['Perl', 'Perl', 'Perl']

MyClass.list_2 # ['Perl', 'Perl', 'Perl']
#_______________________________________________________________________________________
# Properties
# we saw that we can define "bare" attributes in classes and instances
class MyClass:
	def __init__(self, language):
		self.language = language

obj = MyClass('Python')

# we can have direct access to the 'language' attribute.
obj.language # Python
obj.language = 'Java'

# in many languages direct access to attributes is highly discouraged. the convention
# is to make the attribute private and create a public getter and setter method.

# but in Python we dont have private attribtues. but we could write in this way:
class MyClass:
	def __init__(self, language):
      # the convention is to use _ that means it is supposed to be a "private" variable
		self._language = language   

	def get_language(self):        # getter
		return self._language

	def set_language(self, value): # setter
		self._language = value

obj = MyClass('Python')
obj._language # works in python. but we should not get it directly.

# to access the _language attribute we would have to call the method directly
obj.get_language() # Python

# or to set a new value to _language attribute:
obj.set_language('Java')

# would be nice if we could still accessing that "private" variable by using the
# shorthand dot notation. to do this, we use properties.

#_______________________________________________________________________________________________
class MyClass:
	def __init__(self, language):
		self._language = language   

	def get_language(self):        # getter
		return self._language

	def set_language(self, value): # setter
		self._language = value

# in this case, 'language' is considered an instance property. but this property is
# only accessible via the get_language and set_language methods.

# we call the 'language' an property, simple because they arent "bare" attributes 
# anymore, they are going through these methods now.

# technically we can get it from his "private" _language, but we should not touch in that. 


# there are some good reasons why we might want to approach attributes using this
# programming style. it provides control on how an attribute value is set and returned.

# if we start with a class that provides direct access to the language attribute,
# and later need to change it to use accessor methods, we will change the interface
# of the class.
# eg:
#   obj.language = 'Python'   accessing directly the attribute

# but later on we decide we want to provide some validation while setting a value,
# and for that, we require to use a method:

#   obj.set_language('Python')

#_______________________________________________________________________________________________
# we can use the property class to define properties in a class:
class MyClass:
	def __init__(self, language):
		self._language = language  # instance namespace
	
	def get_language(self):
		return self._language

	def set_language(self, value):
		self._language = value

	language = property(fget=get_language, fset=set_language) # class namespace

# we created an instance of property class and assigned to language. language is a
# class property now.

MyClass.__dict__ # {<'language': <property object at 0x0000026AE65E8950>, ...}

obj = MyClass('Python')
obj.__dict__     # {'_language': 'Python'}   doesnt have the 'language' attribute.


obj.language     # Python
# we dont have 'language' in the object instance (obj) namespace. but how do it work?

# Python see that language isnt defined at obj namespace, then it goes up the chain
# at the class level and find the 'language' attribute defined. 
# the language attribute is actually a property object.

# then Python will see that it should call the get_language() method. and this method 
# is going to return the '_language' attribute which is defined inside the 
# object instance (obj) namespace.


# same will happens if we try to set a new value like:
obj.language = 'Java'

# Python will see that the MyClass have the 'language' attribute which is a property
# and will see that has a set_language() method defined, and then will call it 
# whenever we try to set a value to 'language'.

# essentially python is calling: MyClass.set_language(obj, 'Java')
# it will then re-assign the '_language' value of the object instance (obj)
obj.language     # Java


# of course, we still able to access directly the object instance attribute '_language'
# but it wont pass through the get_language() method. 
obj._language    # Java

# same to set_language() method if we assign the attribute directly like:
obj._language = 'Perl'


# we had the same code as before. we did not had changed the interface by using the
# property class object. now we are able to access the object's instance attributes
# through methods without having to call the methods explicitly, we can call then
# implicitly by using the shorthand dot notation approach.
# the property object will be responsible to call then properly, based on the
# functions we defined as arguments: fget, fset. (function getter, setter)


#____________________________________________________________________________________________
class Person:
	def __init__(self, name):
#       will call the setter when the object instance get initialized
		self.set_name(name)
	
	def get_name(self):
		return self._name

	def set_name(self, value):
		if isinstance(value, str) and len(value.strip()) > 0:
			self._name = value.strip()
		else:
			raise ValueError('name must be a non-empty string')

# p = Person('')    ValueError: name must be a non-empty string
# p = Person(100)   ValueError: name must be a non-empty string

p = Person('Fabio')
p.__dict__        # {'_name': 'Fabio'}

# of course we could bypass the getter and setter by accessing the _name directly now
# but we shouldt do it.
p._name = 100
p.get_name()      # 100
#____________________________________________________________________________________________
class Person:
	def __init__(self, name):
		self._name = name
	
	def get_name(self):
		return self._name

	def set_name(self, value):
		if isinstance(value, str) and len(value.strip()) > 0:
			self._name = value.strip()
		else:
			raise ValueError('name must be a non-empty string')

	name = property(fget=get_name, fset=set_name)

# class namespace
Person.__dict__   # {'name': <property object at 0x000001E4ED9278B0>, ...}


p = Person('Fabio')

# object instance namespace
p.__dict__        # {'_name': 'Fabio'}

# what if we add the 'name' attribute directly in the object instance namespace?
p.__dict__['name'] = 'John'

p.__dict__        # {'_name': 'Fabio', 'name': 'John'}

# what Python will do when we try to access the 'name' attribute now?
p.name             # Fabio 
getattr(p, 'name') # Fabio

# even though we have a object instance attribute that have the same symbol ('name')
# of the property that we defined in the class level, Python will still 
# use the property that we defined in the class namespace to get and set the values.
#____________________________________________________________________________________________
# defining the deleter and the docstring of the property object
class Person:
	def __init__(self, name):
		self._name = name
	
	def get_name(self):
		return self._name

	def set_name(self, value):
		if isinstance(value, str) and len(value.strip()) > 0:
			self._name = value.strip()
		else:
			raise ValueError('name must be a non-empty string')

	def del_name(self):
		print('deleter called...')
		del self._name

	name = property(fget=get_name, fset=set_name, fdel=del_name, doc='some doc')

p = Person('Fabio')
p.__dict__  # {'_name': 'Fabio'}

del p.name  # deleter called...

p.__dict__  # {}


help(Person.name)
# Help on property:
#     some doc

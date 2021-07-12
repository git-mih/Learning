# Property decorators

def get_x():
	pass
def set_x():
	pass

# the property class can be instantiated in different ways:

# as we saw before:
x = property(fget=get_x, fset=get_x) 


# but the property class itself defines default methods such as getter, setter, deleter.
# and these methods can take a callable as an argument and returns 
# the instance with the appropriated method now set

# we could create it this way instead: 
x = property()  # <property object at 0x0000013223C30450>

# now we can use the getter method of the property object (x) to specify what to use
# to the get. 
x = x.getter(get_x) # x = property(fget=get_x)

# and now that we have a getter, we can specify a setter:
x = x.setter(set_x) # x = property(fget=get_x, fset=set_x)


# we could also create the property with the getter defined and later on define the set:
x = property(fget=get_x)
x = x.setter(set_x)

#________________________________________________________________________________________
class MyClass:
	def __init__(self, language):
		self._language = language

	def language(self):
		return self._language

	language = property(language) # we dont have to use fget=. we can use positional args
#   we now have a class level property object with a getter method defined.

MyClass.__dict__  # {'language': <property object at 0x000001B98AE774F0>, ...}

p = MyClass('Python')
p.language        # Python


# note that we are decorating the language function basicly. instead, we could write:
class MyClass:
	def __init__(self, language):
		self._language = language
	
	@property     # language = property(language)
	def language(self):
		return self._language

MyClass.__dict__  # {'language': <property object at 0x000001B98AE774F0>, ...}

p = MyClass('Python')
p.language        # Python



# next, we may want to define a setter method as well:
class MyClass:
	def __init__(self, language):
		self._language = language
	
	@property     
	def language(self):
		return self._language
#   at this point, 'language' is a property object inside the class namespace
#   MyClass.__dict__ {'language': <property object at 0x000001B98AE774F0>, ...}

#   now we are able to define the setter method of the property object as well:
	def set_language(self, value):
		self._language = value

#   assigning the set_language method into the class level property object:
	language = language.setter(set_language)

MyClass.__dict__  # {'language': <property object at 0x000001B98AE774F0>, ...}

p = MyClass('Python')
p.language = 'Perl'
p.language        # Perl


# but again, we can rewrite this using the decorator syntax
class MyClass:
	def __init__(self, language):
		self._language = language
	
	@property     
	def language(self):
		return self._language

	@language.setter    # language = language.setter(language)
	def language(self, value):
		self._language = value

p = MyClass('Python')

p.language = 'Perl'

p.language  # Perl

#_____________________________________________________________________________________
# if you find this a bit confusing, think of doing it this way first:
# Python is doing it essentially, when we use the decorator approach:
# @language.setter

class MyClass:
	def __init__(self, language):
		self._language = language
	
	@property                    # language = property(language)
	def language(self):          # type(MyClass.language)   property
		return self._language
	
#   creating a pointer to the 'language' attribute which is an property object
	lang_prop = language         # type(MyClass.lang_prop)  property

#   now we redefine whatever the attribute 'language' was before.
	def language(self, value):   # type(MyClass.language)   function (class level)
		self._language = value   #                          method   (object instance level)

#   assigning the setter method to the property object with the language function
	language = lang_prop.setter(language)
#                                # type(MyClass.language)   function/method again

# language started as a property, became a function/method and now we are reassign it
# to be a property object again.
# now at this point, 'language' is a attribute in our class that is a property object.

# we no longer need the lang_prop attribute in the class namespace anymore
	del lang_prop

#_____________________________________________________________________________________
# at the end of the day, we just need to learn the pattern of how we use these
# decorators to create property types
# just keep in mind, all it is is creating a object instance of the property class

# and assigning this property object instance into an attribute in the class level 
# we also define the getter, setter, deleter and docstring to that property object.

class MyClass:
	def __init__(self, language):
		self._language = language

	@property # the function name defines the property object instance name (symbol)
	def language(self): #       type(MyClass.language)  property
		return self._language

# once we have the property object instance: type(MyClass.language)  property
# next, in order to define the setter method we have to use whatever symbol is storing
# the property object instance. in this case, the attribute 'language' stores it.
	@language.setter 
	def language(self, value):
		self._language = value


#_____________________________________________________________________________________
def get_prop():
	pass

def set_pro():
	pass

def del_prop():
	pass

p = property(get_prop)
# property objects doesnt use the regular dict to store the attributes, it uses slots
# p.__dict__   # AttributeError: 'property' object has no attribute '__dict__'

dir(p)   # [..., 'getter', 'setter', 'deleter', 'fget', 'fset', 'fdel', ...]


p.fget   # <function get_prop at 0x0000019AB471E670>
p.getter # <built-in method getter of property object at 0x0000019AB4727A90>

p.fset   # None
p.fdel   # None

# there is no way of set the setter by using fset now. we have to instantiate a new
# property object from the current 'p' property object that already have a fget/getter
# method defined.

p1 = p.setter(set_pro)

p1 is p  # False

# but we still have the same getter
p1.fget is p.fget  # True

# and now we also have a setter
p1.fset  # <function set_pro at 0x0000026F69D60040>


# we dont have to assign to p1, we should reassign to p
p = property(get_prop)
p = p.setter(set_pro)

#_____________________________________________________________________________________
def name(self):
	return 'getter'

# 'name' points to a function object
name        # <function name at 0x000001>

name = property(name)

# 'name' points to a property object now
name        # <property object at 0x000007>

# just because we renamed the symbol for the function, doesnt mean the function
# desapeared. it still exists as an object in memory. 
# and now the property object has a reference to it in his fget attribute
name.fget   # <function name at 0x000001>


# storing the property object 'name' into a temporary variable.
name_prop = name  # <property object at 0x000007>

# now we gonna redefine the function 'name'
def name(self, value):
	return 'setter'

name       # <function name at 0x000002>

name = name_prop.setter(name)
name       # <property object at 0x000009> brand new object, isnt the same
#                                          property object we had before.

# we still have a reference to that first function 'name' we defined, the getter
name.fget  # <function name at 0x000001>

# and we also still have reference to the redefined function 'name'. the setter
name.fset  # <function name at 0x000002>

#_____________________________________________________________________________________
# we can also define the docstring of the property object inside the getter
class Person:
	def __init__(self, name):
		self._name = name

	@property
	def name(self):
		'''the person's name''' # <<<<<<<<<<<<<<<<
		return self._name
	
	@name.setter
	def name(self, value):
		self._name = value

help(Person.name) 
# Help on property:
# 	  the person's name

#_____________________________________________________________________________________
# we can define a write only property. where we only define the setter method.
# this way, we cant read an attribute directly.

class Person:
	def prop_set(self, value):
		print('setter called')
	
	name = property(fset=prop_set)

p = Person()
p.name = 'fabio'  # setter called

# p.name          # AttributeError: unreadable attribute

# another way of doing it
class Person:
	name = property(doc='write-only attribute')

	@name.setter
	def name(self, value):
		print('setter called')

p = Person()
p.name = 'fabio'  # setter called

# p.name          # AttributeError: unreadable attribute

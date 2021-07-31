# Properties and decorators

from numbers import Integral

# __________________________________________________________________________________________________
# property object: using decorator syntax:
class Person:
    @property
    def age(self):
        return getattr(self, '_age')

    @age.setter
    def age(self, value):
        if not isinstance(value, Integral):
            raise ValueError('age: must be an integer.')
        if value < 0:
            raise ValueError('age: must be a non-negative integer.')
        self._age = value

Person.age   # <property object at 0x000001>  descriptor instance

# Properties are actually data descriptors and these methods will always be there:
hasattr(Person.age, '__get__')     # True
hasattr(Person.age, '__set__')     # True
hasattr(Person.age, '__delete__')  # True

p = Person() # {}

p.age = 26
p.__dict__   # {'_age': 26}


# property object: without decorator syntax:
class Person:
    # fget will points to this method:
    def get_fn(self):
        return getattr(self, '_age')
    
    # fset points to this method:
    def set_fn(self, value):
        if not isinstance(value, Integral):
            raise ValueError('age: must be an integer.')
        if value < 0:
            raise ValueError('age: must be a non-negative integer.')
        # creating the '_age' entry in the object instance namespace:
        self._age = value

    age = property(fget=get_fn)
    age = age.setter(set_fn)
    # we could also create the property in a single line:
    # age = property(fget=get_fn, fset=set_fn)

# no matter if we specify the fget/fset or not, these methods will always be there:
hasattr(Person.age, '__get__')     # True
hasattr(Person.age, '__set__')     # True
hasattr(Person.age, '__delete__')  # True

p = Person()
p.age = 10
p.age # 10


class TimeUTC:
    @property
    def current_time(self):
        return 'current time...'

hasattr(TimeUTC.current_time, '__get__') # True

# we are not specifiing the fset:
hasattr(TimeUTC.current_time, '__set__') # True

t = TimeUTC()

# __get__ will works properly:
t.current_time  # current time...

# if  we try to set the 'current_time' to other value like:
# t.current_time = 100     AttributeError: can't set attribute

# that is not because the __set__ does not exists. it does. we got this error message cause
# the property doesnot have the fset defined.

# what is happening is that, the __set__ is trying to call the fset method in our class 
# and we did not defined the fset=. 


#________________________________________________________________________________________________
# creating our own class that create Properties

class MakeProperty:
    # receive the getter and setter methods we want to use:
    def __init__(self, fget=None, fset=None):
        self.fget = fget   # Person.name.fget = get_name_fn
        self.fset = fset   # Person.name.fset = set_name_fn

    def __set_name__(self, owner_class, property_name):
        self.property_name = property_name

    def __set__(self, instance, value):
        print(f'__set__ called... ')
        if self.fset is None:
            raise AttributeError('cant set attribute')
        # after some validation, we call the setter function:
        self.fset(instance, value)   
        # Essentyally:
        # Person.name.set_name_fn(p, 'Fabio')
        # Person.name._name = 'Fabio'   or   setattr(Person.name, '_name', 'Fabio')

    def __get__(self, instance, owner_class):
        print(f'__get__ called...')
        if instance is None:
            return self
        if self.fget is None:
            raise AttributeError('not readable')
        return self.fget(instance)   
        # Essentyally:
        # Person.name.get_name_fn(p)
        # getattr(Person.name, '_name')  # Fabio

class Person:
    # defining our getter function that will be called from inside the descriptor whenever 
    # we try to access the 'name' property:
    def get_name_fn(self):
        return getattr(self, '_name')

    def set_name_fn(self, value):
    # after some validation the descriptor will call it from there and add the '_name' entry
    # inside the object instance namespace:
        self._name = value

    # now lets make our Property by using our data descriptor (MakeProperty):
    name = MakeProperty(fget=get_name_fn, fset=set_name_fn)
    # whenever we try to get or set the 'name' property, it will automatically call the
    # descriptor get/set method which will then call these functions.

Person.name.__dict__  
# __get__ called... calling get_name_fn(<descriptor_instance_name>, None)

# {'fget': <function Person.get_name_fn at 0x0000011>, 
#  'fset': <function Person.set_name_fn at 0x0000022>, 'property_name': 'name'}


p = Person()

p.name = 'Fabio'   # __set__ called...

# Essentyally:
# MakeProperty.__set__(Person.name, p, 'Fabio')

# then the descriptor calls the set_name_fn:
# Person.set_name_fn(p, 'Fabio')  # self=p, value='Fabio'

# which will creates the '_name' entry inside the object instance namespace:
# setattr(p, '_name', 'Fabio')

p.__dict__ # {'_name': 'Fabio'}

p.name # Fabio
# MakeProperty.__get__(Person.name, p, Person)

# the descriptor will calls the get_name_fn from there:
# getattr(p, '_name')    # Fabio

#________________________________________________________________________________________________
# we can also use the decorator approach as well, we dont require to change anything tho:
class MakeProperty:
    def __init__(self, fget=None, fset=None):
        self.fget = fget
        self.fset = fset

    def __set_name__(self, owner_class, property_name):
        self.property_name = property_name

    def __set__(self, instance, value):
        if self.fset is None:
            raise AttributeError('cant set attribute')
        self.fset(instance, value)   

    def __get__(self, instance, owner_class):
        if instance is None:
            return self
        if self.fget is None:
            raise AttributeError('not readable')
        return self.fget(instance)   

class Person:
    @MakeProperty
    def age(self):
        return 26
    # essentially, Python will do it:
    # age = MakeProperty(age)    where the 1st argument is the fget=

Person.age # <__main__.MakeProperty object at 0x000001>   descriptor instance.

p = Person()
p.age  # 26


# to be able to use the `@age.setter` syntax, we have to define the 'setter' method inside 
# the descriptor:
class MakeProperty:
    def __init__(self, fget=None, fset=None):
        self.fget = fget
        self.fset = fset

    def __set_name__(self, owner_class, property_name):
        self.property_name = property_name

    def __set__(self, instance, value):
        if self.fset is None:
            raise AttributeError('cant set attribute')
        self.fset(instance, value)   

    def __get__(self, instance, owner_class):
        if instance is None:
            return self
        if self.fget is None:
            raise AttributeError('not readable')
        return self.fget(instance)   

    # appending the setter method to be able to use the @property.setter syntax:
    def setter(self, fset):
        self.fset = fset
        # returning a new property object with the setter on it:
        return self

class Person:
    @MakeProperty
    def age(self):
        return getattr(self, '_age')
    # age = <__main__.MakeProperty object at 0x000001>

    @age.setter
    def age(self, value):
        self._age = value

    # essentially: 
    # age = age.setter(p, 10)      -> <__main__.MakeProperty object at 0x000002> (self)

    # now we have a bare new property object that have the old getter and the setter:
    # age = <__main__.MakeProperty object at 0x000002>

p = Person()
p.age = 10
p.age    # 10

# Property value lookup resolution

# now we know that, if we have a object instance attribute 'x' and if we have a 
# class attribute 'x' then the object instance is going to shadow the class attribute 'x'.

# it will use the object instance entry or will use the descriptor get/set methods?

#________________________________________________________________________________________________
# Data descriptors     (both __get__ and __set__ are defined)

# by default it will always ignore the object instance dictionary. so whenever we do:  
# obj.x 

# it will look at the descriptor __get__ and ignore the object instance entry if defined.

class DataDescriptor:
    def __set__(self, instance, value):
        pass

    def __get__(self, instance, owner_class):
        return '__get__ called'

class MyClass:
    prop = DataDescriptor()

obj = MyClass()

obj.prop = 'value_1'
DataDescriptor.__set__(MyClass.__dict__['prop'], obj, 'value_1') # essentially

obj.prop   # __get__ called  /// value_1


# storing a new entry directly in the object instance namespace:
obj.__dict__['prop'] = 'value_2'


obj.prop   # __get__ called  /// value_1
# still calling the __get__ and just ignoring the object instance namespace.


# but if we call the __set__, it will modifies the property value:
obj.prop = 'value_3'
DataDescriptor.__set__(MyClass.__dict__['prop'], obj, 'value_3') # essentially

# the object instance namespace stills the same:
obj.__dict__  # {'prop': 'value_2'}


obj.prop   # __get__ called  /// value_3


#________________________________________________________________________________________________
# Non-data descriptors    (only __get__ or __set_name__ is defined)
# in the other hand, if we have a non-data descriptor, it will always look inside the 
# object instance namespace first. 

# but, if the entry isnt present, it goes up and use the descriptor __get__ method.

class NonDataDescriptor:
    def __get__(self, instance, owner_class):
        return 10

class MyClass:
    prop = NonDataDescriptor()

obj = MyClass()
# the 'prop' attribute isnt inside the object instance namespace:
obj.__dict__   # {}

# so if we try to access the 'prop' attribute, it goes up in the class property 'prop' and
# then calls the descriptor __get__ method:
obj.prop   # 10


# if we do add a 'prop' entry inside the object instance namespace:
obj.prop = 999
# dont have to use obj.__dict__['prop']=999 cause the descriptor isnt implementing __set__.

obj.__dict__   # {'prop': 999}

# if we try to access it now, the object instance namespace will shadow the class property:
obj.prop       # 999

#________________________________________________________________________________________________
# that is the main reason that we have to differentiate data descriptors of non-data descriptors

# now we can safely goes back and store a entry in the object instance namespace with the 
# same class property name knowing how it will works. 
# it will always call the get/set methods of the descriptor even though if the object 
# instance have an attribute with the same name of the property:

class ValidString:
    def __init__(self, min_length=None):
        self.min_length = min_length

    def __set_name__(self, owner_class, property_name):
        self.property_name = property_name

    def __set__(self, instance, value):
        if not isinstance(value, str):
            raise ValueError(f'{self.property_name} must be a string')
        if self.min_length is None and value < self.min_length:
            raise ValueError(f'{self.property_name} not long enough')
        instance.__dict__[self.property_name] = value

    def __get__(self, instance, owner_class):
        if instance is None:
            return self
        return instance.__dict__[self.property_name]

class Person:
    first_name = ValidString(1)
    last_name = ValidString(2)

# descriptor instances namespaces:
Person.first_name.__dict__ # {'min_length': 1, 'property_name': 'first_name'}
Person.last_name.__dict__  # {'min_length': 2, 'property_name': 'last_name'}

p = Person()

# storing value inside the object instance namespaces by accessing the property 'first_name'
# which will then call the __set__ method of the data descriptor:
p.first_name = 'Fabio'

# object instance namespace:
p.__dict__   # {'first_name': 'Fabio'}

# we are dealing with a Data descriptor so, it will ignores the object instance namespace 
# and then call the descriptor __get__ method whenever we try to access the 'first_name' 
# property.
p.first_name # Fabio

# essentially:
ValidString.__get__(Person.first_name, p, Person) 
p.__dict__['first_name']  # Fabio

# Attribute read accessors

# Attribute accessors is a combination of __getattribute__ and __getattr__ method.
# these are the two methods used for access attributes on objects.


# how does Python access attributes inside an object?
# whenever we write code like this:   p.name    or we use    getattr(p, 'name') ,
# Python has to go and lookup for that `name` attribute somehow.

# we are essentially trying to get an attribute value from that `p` object, as we know, 
# that attribute could be living in any number of places like: instance dictionary, 
# class attribute, parent class, descriptors, etc.
# and Python is doing this look up work for us.

#_______________________________________________________________________________________________________
# __getattribute__ method:
# this is actually what gets called when we lookup for a attribute. 
# whenever we try to access an attribute like: p.name/getattr(p, 'name') , Python is actually 
# calling the __getattribute__ method with our object, so it is a bound method essentially.


# Python provides a __getattribute__ default implementation for that does a lot of work.

# we can override it by implementing the  __getattribute__(self, name) method in our class.
# if we do it, we often delegate it back to the parent class do the actual work, cause there is 
# a lot of work behind the scenes. 
# in practice, we call:  super().__getattribute__(name) to do the look up work for us.

# is important to remember that, even calling a method instead of getting a plain attribute, 
# it first needs to get the method from the object as well, it needs to lookup for that particular
# method inside the object. and for that, the __getattribute__ method is called to do the work.


# if we call the  super().__getattribute__ , this is a attribute lookup as well. 
# but Python handle special dunder methods differently than our own custom attributes. 
# therefore, nothing here will actually be applied to dunder methods.

#_______________________________________________________________________________________________________
# __getattr__ method:
# if __getattribute__ method cannot find the requested attribute, then it raises an  AttributeError. 
# Python automatically catches that exception and then call the __getattr__ method to tries to
# find the requested attribute. 
# if the __getattr__ method doesnt find that attribute also, by default it re-raise the 
# AttributeError exception.

# we can override the __getattr__ method to return a default value if the __getattribute__ method
# doesnt find the requested attribute. in general, is easier to override the __getattr__ method 
# than override the __getattribute__ which does a lot of work.


# default attribute look up flow:   obj.age
#                                      |
#                          obj.__getattribute__('age')
#                                      |
#   the attribute 'age' is inside the class namespace? including parent classes namespace?
#               |                                                          |
#              YES                                                        NOP
#               |                                                          |
#     is it a data descriptor?                                 is it inside the 
#      |                   |                                   object instance namespace?
#     YES                 NOP                                      |                 |
#      |                   |                                      YES               NOP
# call __get__ and    is it inside the                             |                 |
# return the value    object instance namespace?               return it           raise
#                      |                  |                                    AttributeError
#                     YES                NOP                                         |
#                      |                  |                                          |
#                 return it      is it a non-data descriptor?            calls __getattr__ method
#                                   |                  |                             |
#                                  YES                NOP                 may return a value or
#                                   |                  |                  propagates back the
#                            call __get__ and     return the              AttributeError exception
#                            return the value     class attribute.


# a word of caution is that, is very easy to get into infinite recursion bugs while manipulating 
# these methods. for exemple, if we are overriding the __getattribute__ method and inside there 
# we are trying to look up for another attribute by using the dot notation, it will essentially 
# use our overridden __getattribute__ method.

# we just require to use the super().__getattribute__ to bypass our own overrides. this way, 
# we will call the parent class __getattribute__ method, and we are not calling ourselves again.



#_______________________________________________________________________________________________________
# __getattr__ method
# lets first take a look at the __getattr__ method:
class Person:
    pass

p = Person()

try:
    # trying to access an attribute that doesnt exist:
    p.name
except AttributeError as ex:
    print('AttributeError:', ex)  # AttributeError: 'Person' object has no attribute 'name'


# overriding the __getattr__ method:
class Person:
    # if __getattribute__ doesnt find an attribute, it calls the __getattr__ method now:
    def __getattr__(self, name):
        print(f'__getattribute__ method did not find: {name}')
        return '__getattr__ method called...'

p = Person()
p.age 
# __getattribute__ method did not find: age
# __getattr__ method called...


# we have to be careful with infinite recursion cause, for every attribute look up that doesnt 
# exist, the __getattr__ method will be called:
class Person:
    def __getattr__(self, name):       # name = age
        alternative_name = '_' + name  # _+age  // _+_age // _+__age // _+___age ...
        if getattr(self, alternative_name):
            # p._age? None // p.__age? None // p.___age? None ...
            return getattr(self, alternative_name)

p = Person()
# p.age    RecursionError: maximum recursion depth exceeded while calling a Python object

# essentially, the __getattribute__ method was called and looke up for the `age` attribute, 
# it did not found it anywhere, then Python calls the __getattr__ method, which will tries to 
# find for an alternative attribute name `_age`. 
# it also didnt find that, then Python calls the overriden __getattr__ method, which will end up
# raising an RecursionError exception.



# there is two ways that we could try to fix this issue. 
# we could try to reach in the __dict__ property of the object, like:  p.__dict__ 
# but we know that not everything is stored in there.

# we want to use the __getattribute__ method, but we dont want it to call the __getattr__ method.

# we could use the default implementation of the  __getattribute__ method that Python provides.
# is usefull cause it goes and look up in all kind of places for that attribute.

# we want to go back to the default __getattribute__ method that doesnt call the __getattr__.

# we just require to delegate the look up back to the __getattribute__ method in the parent class:
class Person:
    def __getattr__(self, name):
        alternative_name = '_' + name
        print(f'__getattr__ method could not find: {name}')
        print(f'__getattribute__ method trying to find: {alternative_name}')
        try:
            return super().__getattribute__(alternative_name)
    # the __getattribute__ will look up for the alternative attribute name now and will not call 
    # the __getattr__ method again.
        except AttributeError:
            raise AttributeError(f'__getattribute__ method could not find: {alternative_name} as well')

p = Person()
try:
    p.age
except AttributeError as ex:
    print(f'{type(ex).__name__}: {ex}')

# __getattr__ method could not find: age
# __getattribute__ method trying to find: _age
# AttributeError: __getattribute__ method could not find: _age


# but if we do have the _age attribute:
class Person:
    def __init__(self, age):
        self._age = age

    def __getattr__(self, name):
        alternative_name = '_' + name
        try:
            return super().__getattribute__(alternative_name)
        except AttributeError:
            raise AttributeError(f'Could not find {name} or {alternative_name}')

p = Person(26)

# we dont have the `age` attribute inside the object instance namespace:
p.__dict__  # {'_age': 26}

# but if we try to get it:
p.age       # 26

# it calls the __getattribute__ method, doesnt find it, then it calls our __getattr__ method that
# will replace the `age` to `_age`, then it delegates back to the __getattribute__ do the look up 
# for the alternative attribute name `_age`.



# making a class that behaves like default dict.
class DefaultClass:
    def __init__(self, attribute_default=None):
        self._attribute_default = attribute_default  # default attribute value

    def __getattr__(self, name):
        print(f'{name} not found, creating and setting it to default...')
        setattr(self, name, self._attribute_default)
        return self._attribute_default

d = DefaultClass('NotAvaiable')  
d.test  
# test not found, creating and setting it to default...
# NotAvaiable

# we injected that `test` attribute inside the object instance namespace, with the default value:
d.__dict__ # {'_attribute_default': 'NotAvaiable', 'test': 'NotAvaiable'}

d.age
# age not found, creating and setting it to default...
# NotAvaiable

d.__dict__ # {'_attribute_default': 'NotAvaiable', 'test': 'NotAvaiable', 'age': 'NotAvaiable'}


# next time we request the `age` or `test` attribute, the __getattr__ method will just return it:
d.test # NotAvaiable
d.age  # NotAvaiable


# we can provide this functionality to other classes via inheritence:
class Person(DefaultClass):
    def __init__(self, name):
        super().__init__('N/A')
        self.name = name

p = Person('Fabio')
p.name     # Fabio

p.age
# age not found, creating and setting it to default...
# N/A

p.__dict__ # {'_attribute_default': 'N/A', 'name': 'Fabio', 'age': 'N/A'}
p.age      # N/A



# logging that a non existent attribute was requested:
class AttributeNotFoundLogger:
    def __getattr__(self, name):
        err_msg = f'{type(self).__name__} object has no attribute: {name}'
        print(f'log: {err_msg}')
        raise AttributeError(err_msg)

class Person(AttributeNotFoundLogger):
    def __init__(self, name):
        self.name = name

p = Person('Fabio')
p.name  # Fabio

try:
    p.age
except AttributeError as ex:
    pass   # log: Person object has no attribute: age


#_______________________________________________________________________________________________________
# __getattribute__ method
# it is called for every attribute look up in any object. 

# stoping access to "private" attributes in our class:
class Person:
    def __init__(self, name, age):
        # "private" attributes:
        self._name = name
        self._age = age
    
    def __getattribute__(self, name):
        if name.startswith('_'):
            raise AttributeError(f'forbidden access to: {name}')
        return super().__getattribute__(name)
# we should always use super() whenever we actually try to access an attribute that is outside:

p = Person('Fabio', 26)
try:
    p._name
except AttributeError as ex:
    print(ex)   # forbidden access to _name



# but what can we do to actually get the `name` now?
# we could try to look up at the object instance namespace, but:
# p.__dict__      # AttributeError: forbidden access to __dict__

# Python will use the __getattribute__ method to find the __dict__ attribute as well. 
# therefore, we dont even have access to the object instance dictionary (namespace) anymore.

# we just want to make sure that it doesnt starts with double underscores to fix it:
class Person:
    def __init__(self, name, age):
        self._name = name
        self._age = age
    
    def __getattribute__(self, name):
        if name.startswith('_') and not name.startswith('__'):
            raise AttributeError(f'forbidden access to: {name}')
        return super().__getattribute__(name)

p = Person('Fabio', 26)
        
p.__dict__          # {'_name': 'Fabio', '_age': 26}
p.__dict__['_name'] # Fabio



# lets try to access the attributes via properties:
class Person:
    def __init__(self, name, age):
        self._name = name
        self._age = age
    
    def __getattribute__(self, name):
        if name.startswith('_') and not name.startswith('__'):
            raise AttributeError(f'forbidden access to: {name}')
        return super().__getattribute__(name)

    @property
    def name(self):
        return self._name

    @property
    def age(self):
        return self._age

p = Person('Fabio', 26)

# that is not gonna work cause the properties is going to use our __getattribute__ method:
try:
    p.name
except AttributeError as ex:
    print(ex)   # forbidden access to: _name
        

# we just require to call super() to fix that issue:
class Person:
    def __init__(self, name, age):
        self._name = name
        self._age = age
    
    def __getattribute__(self, name):
        if name.startswith('_') and not name.startswith('__'):
            raise AttributeError(f'forbidden access to {name}')
        return super().__getattribute__(name)

    @property
    def name(self):
        return super().__getattribute__('_name')
# calling the default __getattribute__ method. this one doesnt care about private attributes.

    @property
    def age(self):
        return super().__getattribute__('_age')

p = Person('Fabio', 26)

p.name   # Fabio
p.age    # 26



# mixin it with the DefaultClass that we make:
class DefaultClass:
    def __init__(self, attribute_default=None):
        self._attribute_default = attribute_default

    # called if the __getattribute__ method doesnt find the requested attribute:
    def __getattr__(self, name):
        print(f'{name} not found, creating and setting it to default...')
        default_value = super().__getattribute__('_attribute_default') # Python __getattribute__
        setattr(self, name, default_value)
        return default_value

class Person(DefaultClass):
    def __init__(self, name, age):
        super().__init__('Not avaiable') # injecting _attribute_default inside the obj instance.
        self._name = name
        self._age = age
    
    # calling it everytime we try to access an attribute:
    def __getattribute__(self, name):
        if name.startswith('_') and not name.startswith('__'):
            raise AttributeError(f'forbidden access to {name}')
        return super().__getattribute__(name)

    @property
    def name(self):
        return super().__getattribute__('_name')

    @property
    def age(self):
        return super().__getattribute__('_age')

# now we have a class that stop us from reading "private" attributes directly, and if we try to
# ask for a property that doesnt exists, it will add it inside the object instance.

p = Person('Fabio', 26)
p.name   # Fabio
p.age    # 26

p.language
# language not found, creating and setting it to default...
# Not avaiable

p.__dict__ # {'_attribute_default': 'Not avaiable', '_name': 'Fabio', '_age': 26, 'language': 'Not avaiable'}



# so far we have been overriding these accessors at instance level in our class.
# in other words, we have been overriding the access to the instances, like:   p.name, p.age

# but what about a classes? 
# how can we override the accessors __getattr__ and __getattribute__ for our class attributes?

# we know that, in order to override the accessors of the instances attributes, we have to define
# the __getattribute__ or the __getattr__ inside the class that we are instantiating from.

# therefore, if we want to override the access of class attributes, we require to modify the 
# metaclass essentially:
class MetaLogger(type):
    def __getattribute__(self, name):
        print(f'__getattribute__ called...')
        return super().__getattribute__(name) # default Python __getattribute__ method.

    def __getattr__(self, name):
        print('__getattr__ called...')
        return 'not found'

class Account(metaclass=MetaLogger):
    apr = 10

# whenever we try to access class attributes now, it will use the metaclass __getattribute__ method:
Account.apr
# __getattribute__ called...
# 10


# if we try to access something that doesnt exists, it calls the __getattribute__ method which
# doesnt find it, then it calls the __getattr__ method:
Account.age
# __getattribute__ called...
# __getattr__ called...
# not found


# apart of the fact that we have defined these methods in a metaclass, everything works the same.
# it just depends if we want to override accessors at the instance level or at class level. 
# at class level, we need to use the metaclass. at instance level, we just override it in the class.


# these accessors __getattribute__ and __getattr__ gets called even for methods, and it can lead
# to issues:
class MyClass:
    def __getattribute__(self, name):
        print(f'__getattribute__ called for {name}...')
        return super().__getattribute__(name)

    def __getattr__(self, name):
        print(f'__getattr__ called for {name}...')
        raise AttributeError(f'{name} not found')

    def say_hello(self):
        return 'hello'

m = MyClass()

# in order to call a method, Python have to find it somewhere. and for that, it calls the 
# __getattribute__ method as well, is the exactly same flow:
m.say_hello()
# __getattribute__ called for say_hello...
# hello


# trying to access something that doesnt exist will call the both methods:
# m.other()   
# __getattribute__ called for other...
# __getattr__ called for other...
#  AttributeError: other not found



# this is basicly how we can override attribute accessors. accessors gets called whenever we try 
# to access something. we had modified the way that the dot (.) operator works essentially.

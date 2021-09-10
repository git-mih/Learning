# The __set_name__ method

# is a very handy method that gets called (once) when the descriptor is instantiated.
# is pretty useful to use whenever we want the __set__ to have some validation whenever it
# gets called.


#______________________________________________________________________________________________
# lets go back to where we can use the object instances namespace to store the data. 

# preveously, we had this approach to store data inside the descriptor namespace:
class IntegerValue:
    def __init__(self, name):
        self.storage_name = '_' + name

    def __set__(self, instance, value):
        setattr(instance, self.storage_name, value)

    def __get__(self, instance, owner_cass):
        if instance is None:
            return self
        return getattr(instance, self.storage_name, None)

class Point2D:
    # we had to specify the class property name/symbol inside the __init__ twice:
    x = IntegerValue('x') 
    y = IntegerValue('y') 

Point2D.x.__dict__  # {'storage_name': '_x'}
Point2D.x.storage_name # _x

Point2D.y.__dict__  # {'storage_name': '_y'}
Point2D.y.storage_name # _y


# that works but the __set_name__ method can be used to get the name/symbol of the class
# properties that we used to represent each descriptor instance object.
class ValidString:
    def __set_name__(self, owner_class, property_name):
        # this allow us to recover the class property name that we defined:
        # owner_class   = <class '__main__.Person'>   //  (Person class)
        # property_name = 'xyz'

        # we can store the property name 'xyz' inside the descriptor instance namespace:
        self.prop = property_name

    def __get__(self, instance, owner_class):
        if instance is None:
            return self
        return f'__get__ called for property: {self.prop}'

class Person:
    # whenever the Person class gets compiled, it will call the __set_name__ method:
    xyz = ValidString()
    # passing the name/symbol 'xyz' to the __set_name__ method.

    # essentially, Python will do it:
    # ValidString.__set_name__(Person.xyz, Person, 'xyz')

    # then assign a new entry inside the descriptor instance namespace:
    # Person.xyz.prop = 'xyz'


# __set_name__ created an attribute called 'prop' inside the descriptor instance namespace:
Person.__dict__['xyz'].__dict__ # {'prop': 'xyz'}
Person.xyz.prop  # xyz


# important to know that, the __set_name__ will be called for each descriptor instance:
class Person:
    first_name = ValidString() # descriptor instance
    # ValidString.__set_name__(Person.first_name, Person, 'first_name')
    # Person.first_name.prop = 'first_name'

    last_name = ValidString()  # descriptor instance
    # ValidString.__set_name__(Person.last_name, Person, 'last_name')
    # Person.last_name.prop = 'last_name'


# each descriptor instance will have in its own namespace a specific 'prop' attribute based
# on the class property symbol that was used to reference the descriptor instance object:
Person.first_name.__dict__  # {'prop': 'first_name'}
Person.first_name.prop  # first_name

Person.last_name.__dict__   # {'prop': 'last_name'}
Person.last_name.prop   # last_name


# we can access that descriptor instance namespace by using the object instances:
p = Person()
p.first_name # __get__ called for property: first_name

# essentyally, Python will do it:
ValidString.__get__(Person.first_name, p, Person) 
             # __get__ called for property: first_name

#______________________________________________________________________________________________
# lets store the class property name inside the descriptor instances namespace and add a
# new entry inside the object instances namespace using the respective property names:

class ValidString:
    def __init__(self, min_length):
        self.min_length = min_length

    def __set_name__(self, owner_class, property_name):
        # storing the property name inside the descriptor instance namespace:
        self.property_name = property_name

    def __set__(self, instance, value):
        if not isinstance(value, str):
            raise ValueError(f'{self.property_name} must be a string.')
        if self.min_length is not None and len(value) < self.min_length:
            raise ValueError(f'{self.property_name} must be at least {self.min_length} characters')
        # getting the property name inside the descriptor instance namespace and
        # adding a new entry inside the object instance namespace with that same name:
        key = '_' + self.property_name
        setattr(instance, key, value)   # p['_'+'first_name'] = 'Fabio'
        # notice that we can be overwriting some object instance attribute by doing it.

    def __get__(self, instance, owner_class):
        if instance is None:
            return self
        key = '_' + self.property_name
        return getattr(instance, key)   # p._first_name  essentially.

# we have to assume that the class is not going to be using slots:
class Person:
    first_name = ValidString(1)
    last_name = ValidString(2)

p = Person()
# now we have the attribute name that raised the exception:
# p.first_name = 1    ValueError: first_name must be a string.


p = Person()
# the object instance namespace is currently empty:
p.__dict__   # {}

# by calling the __set__ method, it will add a new entry to the object instance namespace:
p.first_name = 'Fabio'

# essentially Python will do it:
ValidString.__set__(Person.first_name, p, 'fabio')

# it will lookup the descriptor instance namespace and access the 'property_name' value:
setattr(p, '_' + 'first_name', 'fabio')

# now it have a new entry inside its namespace:
p.__dict__ # {'_first_name': 'fabio'}


p.last_name = 'machado'
ValidString.__set__(Person.first_name, p, 'fabio')
setattr(p, '_' + 'last_name', 'machado')

# two entries inside the object instance namespace now:
p.__dict__   # {'_first_name': 'Fabio', '_last_name': 'machado'}


# but we could have a _first_name attribute already there and end up overwriting that entry:
p = Person()
p._first_name = 'some data previously stored'
p.__dict__    # {'_first_name': 'some data previously stored'}

# calling __set__ method and overwrite that:
p.first_name = 'Fabio'
p.__dict__    # {'_first_name': 'Fabio'}


#______________________________________________________________________________________________
# what about storing the value in the object instance using the same property name? like,
# the class property name is 'x' and we add an 'x' entry inside the object instance 
# namespace.

# by doing that, we could possibly shadow the class attribute like:
class BankAccount:
    apr = 10

# class attribute 'apr':
BankAccount.__dict__  # {'apr': 10, ...}

b = BankAccount()

# the object instance doesnt have the 'apr' attribute entry inside its namespace:
b.__dict__  # {}

# whenever we try to access the 'apr' from the object instance, it doesnt have 'apr' entry,
# so it will goes up in the chain and access the class attribute 'apr':
b.apr   # 10

# the shadow happens when we create a entry inside the object instance with the same
# class attribute name ('apr'):
b.apr = 777
b.__dict__  # {'apr': 777}

# whenever we try to access the 'apr' entry, it will start looking in its own namespaces first:
b.apr  # 777

# essentially:
b.__dict__['apr'] # 777

# the object instance attribute 'apr' is 'Shadowing' the class attribute 'apr'.

# we know that, if we have a object instance attribute 'x' and if we have a 
# class attribute 'x', then the object instance is going to shadow the class attribute 'x'.
# essentially.

# but it will not necessarily happen. it will depends on what kind of descriptor we're 
# dealing with: is it a Data descriptor or Non-data descriptor?

class ValidString:
    def __init__(self, min_length):
        self.min_length = min_length

    def __set_name__(self, owner_class, property_name):
        self.property_name = property_name

    def __set__(self, instance, value):
        if not isinstance(value, str):
            raise ValueError(f'{self.property_name} must be a string.')
        if self.min_length is not None and len(value) < self.min_length:
            raise ValueError(f'{self.property_name} must be at least {self.min_length} characters')
        # adding a entry inside the object instance namespace using the same property name:
        instance.__dict__[self.property_name] = value
        # setattr(instance, self.property_name, value) would call the __set__ recursively:
        # instance[property_name] = value

    def __get__(self, instance, owner_class):
        if instance is None:
            return self
        print(f'__get__ called to: {instance}')
        return instance.__dict__.get(self.property_name)
        # getattr(instance, self.property_name) would call __get__ recursively:
        # instance.property_name

class Person:
    first_name = ValidString(1)
    last_name = ValidString(2)

p = Person()

# adding a new entry with the same property name inside the object instance namespace:
p.__dict__['first_name'] = 'Fabio'
p.__dict__   # {'first_name': 'Fabio'}

# the question was, how does it will works with descriptors? what will happens 
# when we do this:
p.first_name = 'Fabio'
p.first_name
# does it use the object instance namespace or will use the descriptor get/set methods?

# well, if we access 'first_name' from the object instance namespace direcly:
p.__dict__['first_name'] # Fabio
# it will just return the value.

# but if do it:
p.first_name  # Fabio  //  __get__ called to: <__main__.Person object at 0x000001>
# it will not even look at the object instance namespace, it will call the __get__ method.



# take a look at the property value lookup resolution to know how this concept works.

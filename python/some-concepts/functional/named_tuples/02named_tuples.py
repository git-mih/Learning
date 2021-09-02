# Named tuples

# we have seen how we interpreted tuples as data structures by giving meaning to the element
# position contained in the tuple. for exemple, we could represent a 2D coordinate as:
pt = (10, 20)
x, y = pt

# to calculate the distance of two points, we could write it:
from math import sqrt
sqrt(pt[0] ** 2 + pt[1] ** 2)

# but this isnt transparent. if someone see that, they have to know that pt[0] means x-coordinate 
# and pt[1] means the y-coordinate.


# the real drawback of using tuple as data structures is that, we require to know what the 
# elements position mean and remember of them.

# if we ever need to change the structure of our tuple in our code like, inserting a new value 
# that we forgot, most likely our code will break:
fabio = ('Fabio', 26)
name, age = fabio

# later on we realize that, we forgot to add the `city` field:
fabio = ('Fabio', 26, 'POA')

# things will broke if we try to unpack that tuple object again:
# name, age = fabio    ValueError: too many values to unpack (expected 2)



# at that point, in order to make things cleaner, we could use a class approach instead:
class Point2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __repr__(self):
        return f'Point2D(x={self.x}, y={self.y})'
    
    def __eq__(self, other):
        if isinstance(other, Point2D):
            return self.x == other.x and self.y == other.y
        return False

pt = Point2D(10, 20)   # Point2D(x=10, y=20)
isinstance(pt, tuple)  # False

# that works. but at very least, we should implement the __repr__ method and potentially the
# __eq__ method as well.

# calculating the distance now will make more sense:
sqrt(pt.x ** 2 + pt.y ** 2)


# the main point of seeking for another approach is that, we cound mutate that object.
# and sometimes we may not want to be able to mutate our objects:
pt.x = 777   # Point2D(x=777, y=20)


# what if we could somehow combine these two approaches? where we create tuples that we can 
# give meaningful names to the elements based on their positions.
# that is where we can use namedtuples.

#_________________________________________________________________________________________________
# namedtuple is a class factory function, it generates new class objects essentially. 
# and these generated classes inherits from the tuple object. therefore, they have all 
# tuple properties as well:
from collections import namedtuple

# generating named tuple classes:

# we have to understand that, namedtuple is a class factory. whenever we want to use that, we 
# are essentially going to create a new class object. and for that, we require:
#     - the class name we want to use;
#     - a sequence of field names (strings), the only thing is that, the field names have to 
#       be passed to the namedtuple in the same order in which the values is gonna be stored;
#     - the field names can be any valid identifier. except, that they cannot start with: _;
#     - the return value of the namedtuple function will be a class object, with the given
#       name that we passed in.


# we have many ways that we can provide the field names to the namedtuple function:
# we can use a list or tuple of strings:
namedtuple('Person', ['name', 'age'])
namedtuple('Person', ('name', 'age'))

# or we can use a single string with the field names separated by whitespaces or commas:
namedtuple('Person', 'name age')
namedtuple('Person', 'name, age')


# we require to assign that returned class object to a variable name in our code. 
# so we are able to use that to construct object instances of that class later on:
C = namedtuple('Point2D', ['x', 'y'])         # <class '__main__.Point2D'>


# the variable name that we use to assign to the returned class object is arbitrary. but in 
# general, we assign the same class name that we passed in in order to generate the class:
Point2D = namedtuple('Point2D', ['x', 'y'])   # <class '__main__.Point2D'>

# it is essentially just creating aliases, the namedtuple creates the class object, like:
class Point2D(tuple):  # <class object '__main__.Point2D at 0x0001'>
    pass

# then we assign some symbol to reference that class object at 0x0001:
C = Point2D        # <class object '__main__.Point2D at 0x0001'>
Point2D = Point2D  # <class object '__main__.Point2D at 0x0001'>

#__________________________________________________________________________________________________
# instantiating named tuples:

# after the namedtuple function generates a new class object, we can instantiate objects from 
# that, just like any other class:
Person = namedtuple('Person', 'first_name age city')  # <class '__main__.Person'>

# we can use positional arguments or even keyword arguments:
p = Person('Fabio', 26, 'POA')          # Person(first_name='Fabio', age=26, city='POA')
p = Person('Fabio', age=26, city='POA') # Person(first_name='Fabio', age=26, city='POA')

#__________________________________________________________________________________________________
# accessing data inside namedtuples:

# since namedtuples inherits from the tuple class, we can still handle them just like any other 
# tuple object by using indexing, slicing or iterating over:
Person = namedtuple('Person', 'first_name age city')
isinstance(Person, type) # True

# accessing by index:
p = Person('Fabio', 26, 'POA')
p[0] # Fabio
p[1] # 26
p[2] # POA

# by iterating through:
for e in p:
    print(e) # Fabio  //  26  //  POA 

# by unpacking (extended upacking also works):
name, age, city = p
name # Fabio
age  # 26
city # POA


# but in addition, we can also access the data using the field names:
p.first_name # Fabio
p.age  # 26
p.city # POA


# since the namedtuple function returns a class object that inherit from tuple, all object 
# instances of that namedtuple object will inherit from the tuple as well. and therefore,
# they will be immutables:
isinstance(p, tuple) # True
# p.age = 777          AttributeError: can't set attribute

#________________________________________________________________________________________________
# the `rename` keyword-only argument of namedtuples:

# remember that, field names for namedtuples must be valid identifiers, but them cannot start
# with underscore:
# Person = namedtuple('Person', 'name _age')  ValueError: Field names cannot start with an: _.


# namedtuple has a keyword-only argument that will automatically rename any invalid field name.

# by default, the `rename` argument is set to False, and if we set it to True, it will change 
# the invalid field name based on its position (index):
Person = namedtuple('Person', 'name city _age', rename=True)
Person._fields             # ('name', 'city', '_2')

p = Person('amy', 'UK', 26)
p._2   # 26

#________________________________________________________________________________________________
# coverting namedtuple values into an dictionary object:

# there is a way where we can easily extract the field names of an namedtuple and its value 
# and convert that into an dict object:
Person = namedtuple('Person', 'first_name age city')

Person('Fabio', 26, 'POA')._asdict()  # {'first_name': 'Fabio', 'age': 26, 'city': 'POA'}

# we can also perform the reverse proccess.


#________________________________________________________________________________________________
# modifying values of namedtuples:

# namedtuples are immutable objects, it means that, whenever we try to modify/extend it, it
# will create a new namedtuple object essentially.
Person = namedtuple('Person', 'name age')
p = Person('Fabio', 26)  # Person(name='Fabio', age=26)   0x000001

# later on we decide to "change" one or more values inside that tuple:
p = Person(p.name, 777)  # Person(name='Fabio', age=777)  0x000005

# we are essentially creating a new Person object instance and that variable name `p` is
# referencing that new object now.


# this simple approach works well, but it has a drawback that, what if we have a large tuple:
Person = namedtuple('Person', 'first last age country city height role')
p = Person('Fabio', 'machado', 26, 'Brazil', 'POA', 1.79, 'Enginner')

# suppose that we only want to change the `city` field:
p = Person(p.first, p.last, p.age, p.country, 'Gramado', p.height, p.role)
# Person(first='Fabio', last='machado', age=26, country='Brazil', city='Gramado', height=1.79, role='Enginner')

# that works, but its a painful to write that...


# maybe we could use slicing:
p = Person('Fabio', 'machado', 26, 'Brazil', 'POA', 1.79, 'Enginner')
first_values = p[:4]  # ('Fabio', 'machado', 26, 'Brazil')
last_values = p[5:]   # (1.79, 'Enginner')

p = Person(*first_values, 'Gramado', *last_values)
# Person(first='Fabio', last='machado', age=26, country='Brazil', city='Gramado', height=1.79, role='Enginner')

# or unpacking:
p = Person('Fabio', 'machado', 26, 'Brazil', 'POA', 1.79, 'Enginner')
*values, _, heigth, role = p

args = values + ['Gramado', heigth, role] # ['Fabio', 'machado', 26, 'Brazil', 'Gramado', 1.79, 'Enginner']

p = Person(*args)
# Person(first='Fabio', last='machado', age=26, country='Brazil', city='Gramado', height=1.79, role='Enginner')



# the _replace instance method:

# namedtuples provides this handy method that allow us to copy an namedtuple object into a new 
# namedtuple object where we can replace the values that we want to.
# for that, we require to provide keyword arguments which will represent the corresponding
# field names of the tuple and its respective values.

# suppose that we want to change the `country`, `city` and `role` now:
p = Person('Fabio', 'machado', 26, 'Brazil', 'POA', 1.79, 'Enginner')
p._replace # <bound method Person._replace of Person(...)>

# is important to know that, the keyword name must match an existing field name:
p = p._replace(country='UK', city='London', role='DevOps')
# Person(first='Fabio', last='machado', age=26, country='UK', city='London', height=1.79, role='DevOps')

#_______________________________________________________________________________________________________________
# extending a namedtuple:

# sometimes we want to create a namedtuple that can extends another namedtuples by appending
# one or more fields, like:
Person = namedtuple('Person', 'first last age country city height role') # 0x01
Person = namedtuple('Person', 'first last age country city height role car model') # 0x02

# we could use the _fields propertie instead:
Person = namedtuple('Person', 'first last age country city height role') # 0x01
fields = Person._fields + ('car', 'model')

Person = namedtuple('Person', fields)
Person._fields # ('first', 'last', 'age', 'country', 'city', 'height', 'role', 'car', 'model')


# we can also easily use an existing object instance to create a new with object instance with
# the new field name that was created:
Person = namedtuple('Person', 'first last age country city height role')
p = Person('Fabio', 'machado', 26, 'Brazil', 'POA', 1.79, 'Enginner')

# later on we decide to extend the Person tuple fields:
Person = namedtuple('Person', Person._fields + ('car', 'model'))

# we can update that Person instance `p`, with the new values by unpacking the old tuple
# into a new Person instance + new fields:
p = Person(*p, 'Hyundai', 'Hb20')
# Person(first='Fabio', last='machado', age=26, country='Brazil', city='POA', height=1.79, 
#        role='Enginner', car='Hyundai', model='Hb20')


#_______________________________________________________________________________________________________________
# default values for namedtuples:

# namedtuple class object doesnt provide a way to define default values. 
# for that, we could create an object instance of the namedtuple with default values, we are
# essentially creating a prototype.

Person = namedtuple('Person', 'first last age country city height role')
proto_person = Person(None, None, None, 'Brazil', 'POA', None, 'N/A')
# Person(first=None, last=None, age=None, country='Brazil', city='POA', height=None, role='N/A')

# after we define default values for that prototype, we can create object instances of that 
# prototype class object using the _replace method:
fabio = proto_person._replace(first='Fabio', last='machado', age=26)
# Person(first='Fabio', last='machado', age=26, country='Brazil', city='POA', height=None, role='N/A')

giu = proto_person._replace(first='Giulianna', last='Sonnenstrahl', city='NH')
# Person(first='Giulianna', last='Sonnenstrahl', age=None, country='Brazil', city='NH', height=None, role='N/A')

# the only thing is that, we now require to use keyword arguments with this approach.



# we can also provide default values by hardcoding values inside the __defaults__ attribute
# that is avaiable inside the namedtuple class constructor:
Person = namedtuple('Person', 'first last age country city height role')

# hardcoding default values:
Person.__new__.__defaults__ = ('Brazil', 'POA', None, 'N/A')

# is important to know that, the __defaults__ store that into a tuple based on their positions:
def f(a, b, c=20, d=30, e=40): pass
f.__defaults__  # (20, 30, 40)


fabio = Person('Fabio', 'machado', 26, height=1.79)
# Person(first='Fabio', last='machado', age=26, country='Brazil', city='POA', height=1.79, role='N/A')

giu = Person('Giulianna', 'Sonnenstrahl', 24)
# Person(first='Giulianna', last='Sonnenstrahl', age=24, country='Brazil', city='POA', height=None, role='N/A')

# by using this approach, we are no longer required to use keyword-only arguments.

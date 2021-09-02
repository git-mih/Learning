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

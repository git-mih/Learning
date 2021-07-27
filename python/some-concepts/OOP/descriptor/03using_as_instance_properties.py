# Using as instance properties  (storing data inside Descriptor instance namespace)

# the question was, where are we going to store the attribute values?

# _______________________________________________________________________________ 1
# cold we maybe store it in the object instance namespace? (dictionary)
# in most of the cases, yes. that is the best and easiest approach tho.

# that will work most of the time, but we might get issues when dealing with slots. cause
# we cant store anything we want, there is no __dict__ anymore when we implement __slots__.

# and even if we were dealing with __dict__, what symbol should we use? 
# we may overwrite an existing class attribute as well...

class IntegerValue:
    def __set__(self, instance, value):
        # storing the value inside the object instance namespace:
        instance.stored_value = int(value)

    def __get__(self, instance, owner_cass):
        if instance is None:
            return self
        return getattr(instance, 'stored_value', None)

class Point1D:
    x = IntegerValue()

p1 = Point1D() # <__main__.Point1D object at 0x000001>
p2 = Point1D() # <__main__.Point1D object at 0x000002>

p1.x = 10      # p1.__dict__ {'stored_value': 10}

# Essentially, Python will do it:
IntegerValue.__set__(Point1D.x, p1, 10)      # p1.stored_value = int(10)

# and when we try to retrieve that value:
p1.x  # 10
IntegerValue.__get__(Point1D.x, p1, Point1D) # getattr(p1, 'stored_value) || p1['stored_value']


# it will works, but the problem is that, the key 'stored_value' is hardcoded inside the 
# object instances namespace:
p2.x = 20      
p2.__dict__   # {'stored_value': 20}


# this approach will works with multiple object instances cause we are using a single
# descriptor instance.
# but if we try to use multiple descriptor instances, it wont work properly cause all 
# descriptor instances will share the same __set__ method:
class Point2D:
    x = IntegerValue() # <__main__.IntegerValue object at 0x000001>
    y = IntegerValue() # <__main__.IntegerValue object at 0x000002>
    # we have 2 different descriptor instances now. that means, 
    # whenever we call the __set__ passing 'x' or 'y' it will call the same __set__, and
    # in both cases we gonna use the same key 'stored_value' to store the value.

p = Point2D()
p.x = 33      # p.__dict__ {'stored_value': 33}
p.y = 77      # p.__dict__ {'stored_value': 77} seems to work, but it will overwrite the
#                                               previous 'stored_value' value.

# if we inspect the object instance namespace, we can see that we have a single key/value:
p.__dict__    # {'stored_value': 77}


# somehow we need to have an distinct storage name for each property, 'x' and 'y'.


#______________________________________________________________________________________________
# instead, we could create a new attribute inside the Descriptor instance namespace.
# by adding the __init__, we can create attributes inside the Descriptor instance namespace:
class IntegerValue:
    def __init__(self, name):
        # self = Point2D.x | <__main__.IntegerValue object at 0x000001 | Descriptor instance
        self.storage_name = '_' + name

    def __set__(self, instance, value):
        setattr(instance, self.storage_name, value)

    def __get__(self, instance, owner_cass):
        if instance is None:
            return self
        return getattr(instance, self.storage_name, None)

class Point2D:
    x = IntegerValue('x') 
    # Descriptor instance namespace before the __init__:
    # Point2D.x.__dict__  # {} 

    # Python creates the descriptor instances: <__main__.IntegerValue object at 0x000001>
    # and then call the __init__ on it: 
    # IntegerValue.__init__(x, 'x')

    # it will creates the 'storage_name' attribute inside the descriptor instance namespace:
    # and then set the value based on the 'name' parameter we passed to the __init__:
    # Point2D.x.storage_name = '_x'

    # Descriptor instance namespace after the __init__:
    # Point2D.x.__dict__  # {'storage_name': '_x'}

    y = IntegerValue('y') 

# __init__ creates the 'storage_name' attribute on each descriptor instances namespace:
Point2D.x.__dict__  # {'storage_name': '_x'}
Point2D.x.storage_name # _x

Point2D.y.__dict__  # {'storage_name': '_y'}
Point2D.y.storage_name # _y


p1 = Point2D()
p1.__dict__    # {}
p1.x = 10     

# essentially Python is doing it:
IntegerValue.__set__(Point2D.x, p1, 10)
setattr(p1, Point2D.x.storage_name, 10)
# it will then store inside p1 namespace the key: '_x' and the value: 10 like:
p1._x = 10

# we now have a dynamic key for each property:
p1.__dict__    # {'_x': 10}

p1.y = 20      
p1.__dict__    # {'_x': 10, '_y': 20}


# whenever we try to access that 'x' attribute, the __get__ will be called:
p1.x  # 10
IntegerValue.__get__(Point2D.x, p1, Point2D)
getattr(p1, Point2D.x) 
# which will essentially do it:
p1._x # 10


p2 = Point2D() 
p2.__dict__    # {}
p2.x = 100
IntegerValue.__set__(Point2D.x, p2, 100)
setattr(p2, Point2D.x.storage_name, 100)
p2._x = 100

p2.y = 200     
IntegerValue.__set__(Point2D.y, p2, 200)
setattr(p2, Point2D.y.storage_name, 200)
p2._y = 200

p2.__dict__    # {'_x': 100, '_y': 200}


# this approach may works very well, but there is some drawbacks like, specifing the
# parameter 'name': IntegerValue('x') and IntegerValue('y') twice. 

# another drawback is that, we are assuming that, '_x' and '_y' are not already defined as 
# class attribute inside Point2D class. 
# we may already have it, and overwrite then by setting a new '_x' or '_y' with __set__:
p1 = Point2D()

# creating a bare attribute '_x' inside the p1 namespace:
p1._x = 10
p1.__dict__ # {'_x': 10}


# now we call the __set__ method and end up overwriting it:
p1.x = 999
p1.__dict__ # {'_x': 999}

# the last major point is that, what happen if we're using slots?  __dict__  will no longer
# be avaiable to store '_x' or '_y' inside the object instances namespaces.


#__________________________________________________________________________________________________
# we could use a regular dictionary inside the descriptor instance to store all attributes.

# by using the descriptor instances namespace to store the values for us, we are not going 
# to use the object instances anymore.


# we will create a dictionary inside each descriptor instance by using __init__.
# whenever __set__ method is called, we will store the data inside the descriptor instance
# namespace now and we will use the object instance as the key.

# when __get__ gets called, it will lookup for the value based on the object instance that 
# called the __get__. 
# if the object instance is a entry inside the descriptor instance namespace, it will then 
# return the specific value.

# NOTE: we have to assume that our objects are hashables. we could do it this way:

class IntegerValue:
    def __init__(self):
        # regular dictionary for each descriptor instance:
        self.stored_data = {}

    def __set__(self, instance, value):
        # using the object instance as key:
        self.stored_data[instance] = int(value)

    def __get__(self, instance, owner_cass):
        if instance is None:
            return self
        # looks for the object instance entry inside the descriptor instance namespace.
        # if is there, return its value associated:
        return self.stored_data[instance]

class Point2D:
    x = IntegerValue() # <__main__.IntegerValue object at 0x000001> descriptor instance
    # __init__ will creates 'stored_data' dict inside the descriptor instance namespace:
    # x.stored_data = {}

    y = IntegerValue() # <__main__.IntegerValue object at 0x000002> descriptor instance
    # y.stored_data = {}

# each descriptor instances will have its own dictionary called 'stored_data':
Point2D.x.__dict__     # {'stored_data': {}}
Point2D.x.stored_data  # {}

Point2D.y.__dict__     # {'stored_data': {}}
Point2D.y.stored_data  # {}


# each descriptor instances will use the object instances of Point2D to store values inside
# the 'stored_data' dictionary:
p1 = Point2D()         #  <__main__.Point2D object at 0x000003>

p1.x = 10   
# when we call the __set__ method, it will happen essentially:
IntegerValue.__set__(Point2D.x, p1, 10)
Point2D.x.stored_data[p1] = 10

# p1 was added as a key inside the descriptor instance (x) namespace:
Point2D.x.stored_data # {<__main__.Point2D object at 0x000003>: 10}


p1.y = 20
IntegerValue.__set__(Point2D.y, p1, 10)
Point2D.y.stored_data[p1] = 10

# p1 is a entry inside the descriptor instance (y) namespace now:
Point2D.y.stored_data # {<__main__.Point2D object at 0x000003>: 20}


# adding a new entry inside the descriptor instance namespace (x):
p2 = Point2D()  #  <__main__.Point2D object at 0x000004>
p2.x = 999

# descriptor instance (x) namespace after we add two entries:
Point2D.x.stored_data
# {<__main__.Point2D object at 0x000003>: 10,     
#  <__main__.Point2D object at 0x000004>: 999}

# a descriptor instance is able to store multiple entries just by using the 
# object instances as key in the dictionary. each object instance have its unique value.
# they just require to be hashables.


# retrieving the value:
p1 # <__main__.Point2D object at 0x000003>
p1.x  # 10

# Python will then call the __get__:
IntegerValue.__get__(Point2D.x, p1, Point2D)
# will search for the key: <__main__.Point2D object at 0x000003> and returns the value
# associated with that key:
Point2D.x.stored_data[p1]  # 10




# we can now store data that is basicly diferentiated by object instances, even though 
# is the same descriptor instance.

# we are no longer overwriting anything in the object instances namespace.
# and now we could potentialy deal with objects that uses slots, because we are not trying 
# to store data inside the object instances namespace anymore. 
# we are storing it inside descriptor instances namespace now.

# everything that we need is to make the object instances being hashable objects to be able
# to store then as keys inside the descriptor instance dictionary.


# it seems to solve all problems, but not realy...
# we actualy have a potential memory leak with this approach.
# if we try to destroy p1, we gonna still have a reference to that p1 object inside the 
# descriptor instance namespace:

import ctypes
def ref_count(address):
    return ctypes.c_long.from_address(address).value

# first we store the memory address of the object p1:
id_p1 = id(p1)    # id_p1 = 0x000003

'p1' in globals() # True
ref_count(id_p1)  # 2

# now we try to destroy that p1 object:
del p1

'p1' in globals() # False 
# we think it was actually gone but if we look at the reference count, we still have it
ref_count(id_p1) # 1

# look at the descriptor instance namespace:
Point2D.x.stored_data
# {<__main__.Point2D object at 0x000003>: 10,   <<<<<<   still there...
#  <__main__.Point2D object at 0x000004>: 999}    


# that object is really there, we could even get that object and assign to p1 again:
p1 = list(Point2D.x.stored_data.keys())[0]

p1   # <__main__.Point2D object at 0x000003>
p1.x # 10


# we require to use weak references to deal with it.

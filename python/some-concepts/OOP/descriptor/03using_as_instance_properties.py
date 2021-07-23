# Using as instance properties

# the question was, where are we going to store the attribute values?

# cold we maybe store it in the object instance namespace? (dictionary)
# in most of the cases, yes. that is the best and easiest approach. 

# that will work most of the time, but we might get issues when dealing with slots. cause
# we cant store anything we want, there is no __dict__ anymore when we implement __slots__.

# and even if we were dealing with __dict__, what symbol should we use? 
# we may overwrite an existing class attribute as well...

class IntegerValue:
    def __set__(self, instance, value):
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
p2.x = 20      # p2.__dict__ {'stored_value': 20}

# it will works, but the problem is that, the descriptor is hardcoded to use the same key
# inside the object instances dictionaries. ('stored_value')


# this approach will works with multiple object instances of the Point1D class, but look:
class Point2D:
    x = IntegerValue()
    y = IntegerValue()
    # x and y are different object instances of the same descriptor class (IntegerValue)
    # that means, whenever we call the __set__ of x or y it will call the same __set__, and
    # in both cases we gonna store in the same 'stored_value' key.

p = Point2D()
p1.x = 33      # p1.__dict__ {'stored_value': 33}
p1.y = 77      # p1.__dict__ {'stored_value': 77} seems to work, but...

# now if we look at p.__dict__ again
p1.__dict__    # {'stored_value': 77}


# somehow we would need to have an distinct storage name for each property.

#______________________________________________________________________________________________
# we could add the __init__ and then create a new attribute inside the Descriptor object 
# instance namespace:

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
    x = IntegerValue('x') # Point2D.__dict__['x'].__dict__   {} namespace before __init__()
    # Python will create the descriptor object instances x and then call the __init__ on it:
    # IntegerValue.__init__(x, 'x')
    # Point2D.x.storage_name = '_x'

    # same to y:
    y = IntegerValue('y') # Point2D.__dict__['y'].__dict__   {} namespace before __init__()
    # IntegerValue.__init__(y, 'y')
    # Point2d.y.storage_name = '_y'

# __init__ will creates the 'storage_name' property on each descriptor instances namespace. 

# descriptor instances namespace after the __init__ call:
Point2D.x.__dict__  # {'storage_name': '_x'}
Point2D.y.__dict__  # {'storage_name': '_y'}


p1 = Point2D()
p1.__dict__    # {}
p1.x = 10      # p1.__dict__ {'_x': 10}
p1.y = 20      # p1.__dict__ {'_x': 10, '_y': 20}

# essentially Python is doing it:
IntegerValue.__set__(Point2D.x, p1, 10) # (self, instance, value)
setattr(p1, Point2D.x.storage_name, 10)

IntegerValue.__set__(Point2D.y, p1, 20)
setattr(p1, Point2D.y.storage_name, 20)


p2 = Point2D() 
p2.__dict__    # {}
p2.x = 100
IntegerValue.__set__(Point2D.x, p2, 100)
setattr(p2, Point2D.x.storage_name, 100)

p2.y = 200     # p2.__dict__ {'_x': 100, '_y': 200}
IntegerValue.__set__(Point2D.y, p2, 200)
setattr(p2, Point2D.y.storage_name, 200)

#________________________________________________________________________________________________
# the approach above may works very well, but there is some drawbacks like, specifing the
# parameter 'name': IntegerValue('x') and IntegerValue('y') twice. 

# another drawback is that, we are assuming that, '_x' and '_y' are not already defined 
# as class attribute in the Point2D class. 
# we may already have it, and then overwrite then by setting a new '_x' or '_y' with __set__:
p1 = Point2D()

# creating a bare attribute '_x' inside the p1 namespace:
p1._x = 10
p1.__dict__ # {'_x': 10}

# __set__ method overwriting it:
p1.x = 999
p1.__dict__ # {'_x': 999}

# the last major point is that, what happen if we're using slots?  __dict__  will no longer
# be avaiable to store 'storage_name' inside the object instances namespaces.


#__________________________________________________________________________________________________
# maybe we could use a dictionary thats local to the data descriptor object instance?

# we are not going to use the object instances dictionary anymore,
# we can use the descriptor instances namespace (dictionary) to store the values for us.

# so, assuming our objects are hashables. we could do it this way:

# we could create a dictionary inside each descriptor object instance by using __init__.
# and whenever we use the __set__ method, we can save the value inside the descriptor instance
# dictionary by using the object instance as the key.

# and when we use the __get__ we can lookup the value based on the object instance key 
# we are using and then return the corresponing value.

class IntegerValue:
    def __init__(self):
        # distinct dictionary for each descriptor instance.
        self.stored_data = {}

    def __set__(self, instance, value):
        # using the object instance as key.
        self.stored_data[instance] = int(value)

    def __get__(self, instance, owner_cass):
        if instance is None:
            return self
        # accessing the a value based on the object instance
        return self.stored_data[instance]

class Point2D:
    x = IntegerValue() # <__main__.IntegerValue object at 0x000001>  x.stored_data = {}
    y = IntegerValue() # <__main__.IntegerValue object at 0x000002>  y.stored_data = {}

# each descriptor instances will have its own dictionary called 'stored_data':
Point2D.x.__dict__     # {'stored_data': {}}
Point2D.y.__dict__     # {'stored_data': {}}


# each of those descriptor instances will store value based on the object instances of the 
# Point2D class:
p1 = Point2D()         #  <__main__.Point2D object at 0x000003>

p1.x = 10   
# when we call the __set__ method, it will happen essentially:
IntegerValue.__set__(Point2D.x, p1, 10)
Point2D.x.stored_data[p1] = 10

# p1 was added as key in 'stored_data' that is inside the descriptor instance (x) namespace:
Point2D.x.stored_data # {<__main__.Point2D object at 0x000003>: 10}

p1.y = 20
IntegerValue.__set__(Point2D.x, p1, 10)
Point2D.x.stored_data[p1] = 10

# p1 was added inside the descriptor instance (y) namespace now:
Point2D.y.stored_data # {<__main__.Point2D object at 0x000003>: 20}


p2 = Point2D()  #  <__main__.Point2D object at 0x000004>
p2.x = 999

# now lets see the descriptor instance (x) namespace:
Point2D.x.stored_data
# {<__main__.Point2D object at 0x000003>: 10,     
#  <__main__.Point2D object at 0x000004>: 999}

# basicly the same descriptor instance was able to store inside itself, many values for 
# multiple object instances just by using the object instances as key in the dictionary.


# we can retrieve it based on the same key.
p1.x  # 10
# Python will call the __get__:
IntegerValue.__get__(Point2D.x, p1, Point2D)
Point2D.x.stored_data[p1] # 10

p1.y  # 20
IntegerValue.__get__(Point2D.y, p1, Point2D)
Point2D.y.stored_data[p1] # 20

p2.x  # 999
IntegerValue.__get__(Point2D.x, p2, Point2D)
Point2D.x.stored_data[p1] # 999

#__________________________________________________________________________________________________
# we can now store data that is basicly diferentiated by object instances, even though 
# is the same descriptor instance.

# we are no longer overwriting anything in the object instance dictionaries. 
# and now we could potentialy deal with objects that uses slots, because we are not trying 
# to store data inside the object instances namespace anymore. 
# we are storing it inside descriptor instances namespace now.

# everything that we need is to make the object instances being hashable objects to be able
# to store then as keys inside the descriptor instance dictionary.


# it seems to solve all problems, but not realy...
# we actualy have a potential memory leak with this approach.
# if we try to destroy p1, we gonna still have a reference to that p1 object inside the 
# descriptor instance namespace.

import ctypes
def ref_count(address):
    return ctypes.c_long.from_address(address).value

# first we store the memory address of the object p1:
id_p1 = id(p1)    # id_p1 = 0x000003

'p1' in globals() # True
ref_count(id_p1)  # 2

# now we try to destroy p1 object:
del p1

'p1' in globals() # False 

# we think it was actually destroyed but if we look at the reference count, we still have it
ref_count(id_p1) # 1

# now lets look at the descriptor instance namespace:
Point2D.x.stored_data
# {<__main__.Point2D object at 0x000003>: 10,  <<<<<<   still's there
#  <__main__.Point2D object at 0x000004>: 999}    


# we could get that object and assign to p1 again, like:
p1 = list(Point2D.x.stored_data.keys())[0]

p1   # <__main__.Point2D object at 0x000003>
p1.x # 10


# we could deal with it by using weak references.

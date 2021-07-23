# Using as instance properties

# how we can use our data descriptor as object instance properties.

# the question was, where are we going to store the attribute value?
# we know the object instance we are dealing with in both __get__ and __set__ cause we pass
# it in the `instance` argument. 


# cold we maybe store it in the object instance namespace? (dictionary)
# in most of the cases, yes. that is the best and easiest approach. 

# that will work most of the time, but we might get issues when dealing with __slots__. cause
# we cant store anything we want cause there is no __dict__ anymore.

# and even if we were dealing with __dict__, what symbol should we use? 
# we might overwrite an existing attribute as well...


# so, maybe we could use a dictionary thats local to the data descriptor object instance?
# we are not going to use the instances data dictionary, we are going to use our own
# dictionary inside the descriptor object instance. 

# we might use the key to be the descriptor object instance essentially. but the problem is
# if the descriptor object instance isnt hashable.
# and we could set the value to be the attribute value that we want to store and whenever we
# want to get it we just returns the value. and with the values, we can store anything we want,
# doesnt have to be hashable objects. 

# so, assuming our objects are hashables. we could do it this way:
# we could create a dictionary in the descriptor object instance. 
# e.g: in IntegerValue instance we create a dictionary.
# now, if we use this IntegerValue object instance for multiple instances, they will share
# the same descriptor object instance, the same dictionary.

# when we use the __set__ method, we can save the value in the dictionary using the instance
# as the key.
# and then when we use the __get__, we can lookup the value based on the instance inside the
# dictionary and then return the corresponing value.
class IntegerValue:
    def __init__(self):
        # creating a empty dictionary in the object instances of this IntegerValue class.
        self.data = {}

    def __set__(self, instance, value):
        # storing the value in the dictionary 'data' under the key 'instance'
        self.data[instance] = int(value)

    def __get__(self, instance, owner_class):
        if not instance:
            return self
        # getting the value based on the key that is an object 'instance' inside the dictionary
        return self.data.get(instance)
        #      self.data['instance']

class Point2D:
    x = IntegerValue()
    y = IntegerValue()
    # this is going to work, but...

p = Point2D() # reference count is 1 now

p.x = 100     # p is now a key in self.data, we have a 2nd reference to that Point2D object instance

# now if we try to delete p, it wont actually be destroyed. cause the dictionary of the
# descriptor object instance has a strong reference to that Point2D object instance.
del p

# still have a reference count to that object. it wont be garbage collected.

#_______________________________________________________________________________________________________
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
# we could do this, adding the __init__ and then create a new attribute inside the Descriptor
# object instance namespace:
class IntegerValue:
    def __init__(self, name):
        self.storage_name = '_' + name   # Point2D.__dict__['x'].storage_name = '_x'

    def __set__(self, instance, value):
        setattr(instance, self.storage_name, value)

    def __get__(self, instance, owner_cass):
        if instance is None:
            return self
        return getattr(instance, self.storage_name, None)


class Point2D:
    # creates the descriptor object instances x and y first and then call the __init__ on it
    x = IntegerValue('x') # Point2D.__dict__['x'].__dict__   {} namespace before __init__()
    # IntegerValue.__init__(x, 'x')
        # Point2d.__dict__['x'].storage_name = '_x'

    y = IntegerValue('y') # Point2D.__dict__['y'].__dict__   {} namespace before __init__()
    # IntegerValue.__init__(y, 'y')
        # Point2d.y.storage_name = '_y'

# it will creates the 'storage_name' attribute on each descriptor instances namespace. 


# descriptor instances namespace after the __init__ call:
Point2D.__dict__['x'].__dict__ # {'storage_name': '_x'}
Point2D.y.__dict__             # {'storage_name': '_y'}


p1 = Point2D()
p1.__dict__    # {}
p1.x = 10      # p1.__dict__ {'_x': 10}
p1.y = 20      # p1.__dict__ {'_x': 10, '_y': 20}

# essentially Python is doing it:
IntegerValue.__set__(Point2D.__dict__['x'], p1, 10) # (self, instance, value) -> p1._x = 10
IntegerValue.__set__(Point2D.y, p1, 20)

p2 = Point2D() 
p2.__dict__    # {}
p2.x = 100
p2.y = 200     # p2.__dict__ {'_x': 100, '_y': 200}

#________________________________________________________________________________________________
# the approach above may works very well, but there is some drawbacks like, specifing the
# parameter 'name': IntegerValue('x') and IntegerValue('y') twice. 

# another drawback is that, we are assuming that, '_x' and '_y' are not already defined 
# as class attribute in the Point2D class. 
# we may already have it, and then overwrite then by setting a new '_x' or '_y' with __set__
p1 = Point2D()

# creating a bare attribute '_x' inside the p1 namespace:
p1._x = 10      # p1.__dict__ {'_x': 10}

# __set__ method overwriting it:
p1.x = 999      # pq.__dict__ {'_x': 999}


# the last major point is that, what happen if we're using slots?  __dict__  will no longer
# be avaiable to store 'storage_name' inside the object instances namespaces.

#__________________________________________________________________________________________________
# there is a different number of ways that we could fix it

# lets assume that our class is using slots. and lets assume that the class is hashable.

# So, what we might do instead of storing the value inside the object instance namespace, 
# is basicly create an storage mechanism inside the Descriptor namespace itself.

# we have to be careful tho, because it have to be unique by instance
class IntegerValue:
    def __init__(self):
        self.value = {}

    def __set__(self, instance, value):
        setattr(instance, self.storage_name, value)

    def __get__(self, instance, owner_cass):
        if instance is None:
            return self
        return getattr(instance, self.storage_name, None)





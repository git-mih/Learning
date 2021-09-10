# Descriptors

# the underpinning mechanism for properties, methods, slots, and even functions.

# Suppose we want a Point2D class whose coordinates must always be integers. but plain
# attributes for x and y cannot guarantee this. instead, we can use a property with 
# getter and setter methods:

class Point2d:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, value):
        self._x = value

    # ok, now we do the same thing for y:
    @property
    def y(self):
        return self._y

    @y.setter
    def y(self, value):
        self._y = value
    # this solves the problem, but is tedious and repetitive boiler plate code.

#_________________________________________________________________________________________
# what if we could write a separate class like this:
class IntegerValue:
    def __init__(self, value=None):
        if value:
            self.set(value)

    def get(self):
        return self._value

    def set(self, value):
        self._value = int(value)


# and somehow we use it in our class in this way:
class Point2D:
    x = IntegerValue(3) # <__main__.IntegerValue object at 0x000001>
    y = IntegerValue(7) # <__main__.IntegerValue object at 0x000002>
    # x, y are class attributes of Point2D that is storing object instances of IntegerValue.
    # these class attributes are bound to the Point2D class, not the instances. 

p = Point2D()
p.x.__dict__     # {'_value': 3}

p.x.get()        # 3
# even if we use the get and set methods ourselves, we are still dealing with IntegerValue 
# instances that are bound to the class Point2D.


# we need to be able to tell Python two things:
#   x needs to be an object instance of IntegerValue. 
#   and it should also be bound to instances at run-time. 

# so when we say `p.x` it calls the get/set methods of the IntegerValue object instance 
# automatically.


# this is where the Descriptor protocol comes in. We have 4 main methods that make up the
# descriptor protocol. but they are not all required.

# __get__ is used to get an attribute value like:  p.x
# __set__ is uset to set an attribute value like:  p.x = 100
# __delete__ used to delete an attribute value:    del p.x
# __set_name__

# this is very similar to what we have with getter/setter/deleter for properties. And in fact,
# property uses this Descriptor protocol. The property class is just a convenience way to get
# access to descriptors, but we dont have to use properties, we can create our own descriptor.


# we have two categories of descriptors: 
#   implement __get__ method only. those are called:               non-data descriptors.
#   implement __set__ and/or __delete__ method. those are called:  data descriptors.

# this distinction is important cause, it changes the way Python access the data when we have a
# non-data descriptor vs a data descriptor.


#_________________________________________________________________________________________
# using a Descriptor class
# we first define a class that implements the __get__ method only (non-data descriptor)
from datetime import datetime

class TimeUTC:
    def __get__(self, instance, owner_class):
        # __get__ called...
        return datetime.utcnow().isoformat()

# next, we creates an descriptor instance and store it as a class attribute:
class Logger:
    current_time = TimeUTC()
    # class attribute that points to an object instance of the non-data descriptor. 
    # therefore, what Python will do automatically for us is call the __get__ method when we
    # try to access the descriptor instance attribute, like: `l.current_time`.

l = Logger()
l.current_time   
# __get__ called...
# 2021-07-20T23:30:30.684140


#_________________________________________________________________________________________
from random import choice
class Choices:
    def __init__(self, *choices):
        self.choices = choices

    def __get__(self, instance, owner_class):
        return choice(self.choices)

class Deck:
    suit = Choices('Spade', 'Heart', 'Diamond', 'Club')
    card = Choices(*'23456789JQKA' + '10')

d = Deck()
for _ in range(5):
    print(d.card, d.suit)

# 9 Club
# 4 Spade
# Q Heart
# 9 Club
# 4 Diamond

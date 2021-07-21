# Getters and setters

# __get__ method:
from datetime import datetime
class TimeUTC:
    def __get__(self, instance, owner_class):
        return datetime.utcnow().isoformat()

class Logger:
    current_time = TimeUTC()

# its realy important to understand how the __get__ is being called.

# Logger class defines an object instance of TimeUTC as a class attribute. 

# and because TimeUTC implements the __get__ method, Python will use that method when 
# retrieving the object instance value.

# we can access the current_time attribute from the Logger class itself:
Logger.current_time   # 2021-07-21T00:23:21.460992

# and we can also access from the object instance of Logger class:
l = Logger()
l.current_time        # 2021-07-21T00:28:19.533460

# Python pass different arguments values when dealing with object instances calls vs directly class call.
# so, when __get__ is called, we may want to know:
#   which class owns the TimeUTC object instance? (Logger in this case)
#   which instances was used? (if any)

# this is why we have that signature:   (self, instance, owner_class)


# for exemple, if we call `current_time` class attribute directly from the class like:
Logger.current_time 
# the `instance` value will be set to None. 

# but if we call the `current_time` class attribute from the instance like:
l.current_time 
# the `instance` value will be the `l` object. 

# the `owner_class` will be the Logger object in both cases.

#______________________________________________________________________________________________
# so we can return different values from __get__ depending if it was called directly 
# from a class or called from a object instance of that class.
class TimeUTC:
    def __get__(self, instance, owner_class):
        # iff we call __get__ from the class object like: Logger.current_time
        if not instance:  
            return self  # <__main__.TimeUTC object at 0x000001>
        return datetime.utcnow().isoformat()

# very often, we choose to return the descriptor object instance when called from
# the class itself (Logger in this case). 
# this gives us an easy handle to the descriptor object instance.
Logger.current_time      # <__main__.TimeUTC object at 0x000001>
# will return a pointer to the TimeUTC object instance

# and we commonly return the class attribute value when we call from an object instance of 
# that particular class. 
# like calling the `current_time` from an object instance of Logger (l.current_time).
l1 = Logger()            # <__main__.Logger object at 0x000002>
l1.current_time          # 2021-07-21T19:39:04.111544


#_______________________________________________________________________________________________
# the arguments that are received from the __get__ method changes, depends whether it is
# called from the class or was called from an object instance of that class.
class TimeUTC:
    def __get__(self, instance, owner_class):
        return (f'__get__ called: self = {self}, \
                                  instance = {instance}, \
                                  owner_class = {owner_class}')

class Logger1:                # <class '__main__.Logger1>
    current_time = TimeUTC()

Logger1.__dict__['current_time'] # <__main__.TimeUTC object at 0x000001> Descriptor pointer
Logger1.current_time
# __get__ called: self =           <__main__.TimeUTC object at 0x000001>,
#                 instance = None, 
#                 owner_class = <class '__main__.Logger1'>

# Python essentially is doing it under the hood:
TimeUTC.__get__(Logger1.__dict__['current_time'], None, Logger1)


class Logger2:                # <class '__main__.Logger2>
    current_time = TimeUTC()

getattr(Logger2, 'current_time')
# __get__ called: self =     <__main__.TimeUTC object at 0x000001>,
#                 instance = None, 
#                 owner_class = <class '__main__.Logger2'>


# lets create object instances of this Logger class now:
l1 = Logger1()             # <__main__.Logger1 object at 0x000003>,

l1.current_time
# __get__ called: self =     <__main__.TimeUTC object at 0x000001>, Logger1.__dict__['c_time']
#                 instance = <__main__.Logger1 object at 0x000003>, l1
#                 owner_class = <class '__main__.Logger1'>          Logger1

# essentially:
TimeUTC.__get__(Logger1.__dict__['current_time'], l1, Logger1)


l2 = Logger1()             # <__main__.Logger1 object at 0x000004>,
#                             2nd object instance of Logger1 class
getattr(l2, 'current_time')
# __get__ called: self =     <__main__.TimeUTC object at 0x000001>, Logger1.__dict__['c_time']
#                 instance = <__main__.Logger1 object at 0x000004>, l2
#                 owner_class = <class '__main__.Logger1'>          Logger1


l3 = Logger2()             # <__main__.Logger2 object at 0x000005>
l3.current_time
# __get__ called: self =     <__main__.TimeUTC object at 0x000001>,  Logger2.__dict__['c_time']
#                 instance = <__main__.Logger2 object at 0x000005>,  l3
#                 owner_class = <class '__main__.Logger2'>           Logger2


# we can diferentiate inside our __get__ method wheter the descriptor was accessed via class
# or via the object instance of the class.
class TimeUTC:
    def __get__(self, instance, owner_class):
        if not instance:  
            return self  
        return datetime.utcnow().isoformat()

class Logger:
    current_time = TimeUTC()

Logger.current_time   # <__main__.TimeUTC object at 0x000001>  Logger.__dict__['c_time']
# now, whenever we call the 'current_time' class attribute directly from the class 
# we can get the descriptor pointer. 

# otherwise, we would have to use the __dict__ like:
Logger.__dict__['current_time'] # <__main__.TimeUTC object at 0x000001>
# and then get the handler to the descriptor object.

# but if we call the class attribute 'current_time' from an object instance, it will then 
# returns a value defined in the __get__ method.
l1 = Logger()
l1.current_time       # 2021-07-21T18:58:19.297061


# and it is consistent with the way properties work:
class Logger:
    @property
    def current_time(self):
        return datetime.utcnow().isoformat()

Logger.current_time             # <property object at 0x000001>
Logger.__dict__['current_time'] # <property object at 0x000001>

l1 = Logger()
l1.current_time       # 2021-07-21T19:03:01.566900


# but there is a subtle point that we have to understand. 
# when we create multiple object instances of a class that uses a descriptor, since the 
# descriptor is assigned to a class attribute, all object instances of the class will share
# the same descriptor instance.
class TimeUTC:
    def __get__(self, instance, owner_class):
        if not instance:  
            return self  
        return f'__get__ called in {self}'

class Logger:
    current_time = TimeUTC()

Logger.current_time               # <__main__.TimeUTC object at 0x000007>

l1 = Logger() # <__main__.Logger object at 0x000001>
l1.current_time # __get__ called in <__main__.TimeUTC object at 0x000007>

l2 = Logger() # <__main__.Logger object at 0x000002>
l2.current_time # __get__ called in <__main__.TimeUTC object at 0x000007>

# in the above case it doesnt matter, but take a look:
class Countdown:
    def __init__(self, start):
        self.start = start + 1

    def __get__(self, instance, owner):
        if instance is None:
            return self
        self.start -= 1
        return self.start

class Rocket:
    countdown = Countdown(10)

rocket1 = Rocket()
rocket2 = Rocket()

rocket1.countdown # 10
rocket1.countdown # 9

rocket2.countdown # 8

#_______________________________________________________________________________________________
# __set__ method

# __set__ signature:  (self, instance, value) 

# descriptors are meant to be used for object instances.
# setters and deleters are always called from instances. there is no real need to have 
# the class reference cause we have the instance and is in there that we want to store the value. 


# there is one really important caveat with __set__ and __delete__ method.
class Logger:
    current_time = TimeUTC()
    # notice that we have only created a single object instance of the descriptor.

l1 = Logger()
l2 = Logger()
# so what happens when we have two object instances of the Logger class?
# well, any object instance of Logger will be referencing the same instance of TimeUTC. So
# the same object instance of TimeUTC (descriptor) is shared by all object instances of Logger.

# whenever we have to store and get data from the object instances, it will be a issue.
class IntegerValue:
    def __set__(self, instance, value):
        print(f'__set__ called: instance = {instance}, value = {value}')

    def __get__(self, instance, owner):
        if instance is None:
            return self
        return f'__get__ called: instance = {instance}, owner = {owner}'

class Point2D:
    x = IntegerValue() # x = <__main__.IntegerValue object at 0x000001>
    y = IntegerValue() # y = <__main__.IntegerValue object at 0x000002>

p = Point2D()
p.x       # __get__ called: instance = <__main__.Point2D object at 0x000001>, 
#                           owner    = <class '__main__.Point2D'>

p.x = 100 # __set__ called: instance = <__main__.Point2D object at 0x000001>, value = 100


# but where should we store the values for x and y?

# a wrong way would be storing it directly inside the Descriptor instance namespace, like:
class IntegerValue:
    def __set__(self, instance, value):
        self._value = value

    def __get__(self, instance, owner):
        if instance is None:
            return self
        return self._value

class Point2D:
    x = IntegerValue() # x = <__main__.IntegerValue object at 0x000001>
    y = IntegerValue() # y = <__main__.IntegerValue object at 0x000002>
    # two different descriptor instances.

p1 = Point2D()  # p1.__dict__   {}
p1.x = 3
p1.y = 7

Point2D.__dict__['x'] # <__main__.IntegerValue object at 0x000001>
Point2D.__dict__['y'] # <__main__.IntegerValue object at 0x000002>
# references to the descriptor object instance.

# values get stored inside the descriptor object instance namespace.
Point2D.__dict__['x'].__dict__ # {'_value': 3}
Point2D.__dict__['y'].__dict__ # {'_value': 7}


# every object instance of this Point2D class is going to share the same Descriptor instances.
p2 = Point2D()
Point2D.__dict__['x'] # <__main__.IntegerValue object at 0x000001>
Point2D.__dict__['y'] # <__main__.IntegerValue object at 0x000002>

Point2D.__dict__['x'].__dict__ # {'_value': 3}
Point2D.__dict__['y'].__dict__ # {'_value': 7}

p2.x, p1.y    # 3  7

# if we try to set the p2.x value now, it will affect p1.x, cause both object instances 
# are sharing the same descriptor instance.
p2.x = 999

Point2D.__dict__['x'].__dict__ # {'_value': 999}
Point2D.x.__dict__             # {'_value': 999}
p1.x  # 999

# wheter we call __set__ from p1 or p2, the same __set__ method will called. the only 
# difference between the two calls is that the `instance` value is going to be different.

# NOTE: this approach will work properly only with a single object instance.

# this is why both, __get__ and __set__ needs to know the instances that we are working with.
# because we are going to have to store or get a value for each specific object instance.


# we have to make our code in our Descriptor class be instance specific in somehow.

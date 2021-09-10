# Inheriting from the type class

# we saw how to use type to create new types (classes) by using:  type(name, bases, dict)

# type is an object and like any other objects it inherits from the object class as well:
isinstance(type, object)  # True

# by default it also inherits dunder methods like __new__ and __init__:
hasattr(type, '__new__')  # True
hasattr(type, '__init__') # True


# type is a class. therefore, it is callable. calling it creates a new type instance.
# its just like calling any other class, it calls the __new__ method.

# we can create an instance of type by using the callable approach:
type('Person', (), {})  # <class '__main__.Person'>

# and we could create an instance of type by calling the __new__ method directly as well:
type.__new__(type, 'Person', (), {}) # <class '__main__.Person'>

# both cases it returns an type instance.

#______________________________________________________________________________________________
# inheriting from type:
# in fact, we can use the type class as a base class for a custom class:
class T(type):
    pass

# since type is a class, we can subclass it. and once we do that, we can overwrite the 
# __new__ method inside our custom classes. it allow us to tweak things. 

# but is important to know that, eventually it delegates back to the type class to actually 
# do the creation of the type object instance (class object).

# it just gives a "hook", so we can modify things in there before the type class creates an 
# new instance (class).


# essentially, we can create custom types by inheriting from type. and with our custom type class, 
# we can create new types (classes):
class T(type):
    pass

MyClass = T('Person', (), {})
# it will call the __new__ method, do some stuffs, delegate back the creation of the instance
# to the type class, then it returns the new type (class) object:

MyClass       # <class '__main__.Person'>

# our custom type class (T), is subclass of type. in fact, it stills an instance of type:
isinstance(T, type) # True

type(MyClass) # <class '__main__.T'>

# now we are able to intercept the creation of the type instance (class).


#____________________________________________________________________________________________________
# we usually inherit from type to maybe overwrite some behaviors, like the __new__ method.

# instead of calling the type class directly:
type('Person', (), {})


# what we can do is call it through our own custom type class to do the same thing essentially,
# create a new type instance (class object).

# but we can intercept it and inject code inside the instance before it gets returned, like:
import math
class CustomType(type):
    def __new__(cls, name, bases, dict):
        class_instance = super().__new__(cls, name, bases, dict)
        # delegating the creation of the instance to the type class itself creates. 
        # it will call the type.__new__ method essentially.

        # inject a method inside the instance after its creation:
        class_instance.circunference = lambda self: 2 * math.pi * self.r
        return class_instance

# we will create instance of our custom type class by doing it manually first, so we can 
# understand how Metaclass works under the hood later:
class_body = """
def __init__(self, x, y, r):
    self.x = x
    self.y = y
    self.r = r

def area(self):
    return math.pi * self.r ** 2
"""
class_dict = {}

# populating the class namespace (dictionary) with the class body code:
exec(class_body, globals(), class_dict)


# now we can create an new instance (class) of our custom type:
Circle = CustomType('Circle', (), class_dict)  # <class '__main__.Circle'>


# and once we have that class object, we can create instances of:
c = Circle(0, 0, 1)  # type(c)  <class '__main__.Circle'>
c.area() # 3.141592653589793
c.circunference() # 6.283185307179586



Circle.__dict__ # {..., 'circunference': <function CustomType.__new__.<locals>.<lambda> at 0x1>}

# we injected that method after we create the type instance (class object). but we can also
# inject things before we create the instance. we just require to inject that method inside the 
# class namespace (dictionary) that we passed to the __new__ method:
class CustomType(type):
    def __new__(cls, name, bases, dict):
        dict['circunference'] = lambda self: 2 * math.pi * self.r # before instance creation.
        class_instance = super().__new__(cls, name, bases, dict)
        return class_instance

class_body = """
def __init__(self, x, y, r):
    self.x = x
    self.y = y
    self.r = r

def area(self):
    return math.pi * self.r ** 2
"""
class_dict = {}
exec(class_body, globals(), class_dict)

Circle = CustomType('Circle', (), class_dict)  # <class '__main__.Circle'>

c = Circle(0, 0, 1)
c.circunference() # 6.283185307179586    work as well.

#___________________________________________________________________________________________________
# this is the Metaclass concept. and this is how we use it, essentially.

# but its kinda painful right, nobody wants to write code like this, where we have to do all 
# steps manually, since compiling the class body inside a blob of text, creating a empty dict,
# populating that block of code inside the dict, and so on.

# Python does a lot of work for us when we write code like this:
class Test:
    pass

# when Python encounter the class keyword, it does all that work that we just did, like deal 
# with the body class, name, bases, dict, exec and more.

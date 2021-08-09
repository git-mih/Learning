# How classes are created

# classes gets created when Python reaches the class keyword during compilation of our code.
# a new symbol for exemple, Person is created in the current namespace, and that symbol is a 
# reference to the class Person object (an type object instance essentially). 

# classes are actually just objects as well. they all are object instances of the type class.
# the type class itself is a object that inherits from the object class.


# so how does Python creates that class?  it creates classes by using the type class.
# for exemple, if we have an class called Person, then we can create instances of that Person class. 
# the classes itself are just object instances of type, that is why a class is also called a type.

# type is a class and type is also a callable. in fact, a type itself is also a class, and also
# inherits from the object class. the only difference is that, it is used to create other classes.

#_____________________________________________________________________________________________________
# the inner mechanics of class creation:
# lets say that we have this Person class and it sits in the module level:

class Person(object): # class_name(class_base, )
    ############################################## class_body
    planet = 'Earth'
    name = property(fget=lambda self: self._name)

    def __init__(self, name):
        self._name = name
    #############################################

# we have 3 things going on there. the class name, class base(s) and the class body which is really 
# just a blob of text.


# what happens when Python encounters this code inside our module is:
# 1 - the class body is extracted. Python takes that block of text and doesnt do anything just yet.
# 2 - it creates an new empty dictionary. this dictionary will be the namespace of the new class.
# 3 - it takes that extracted code now and executes it inside the dictionary. it will essentially 
#     populates that namespace with data, attributes, functions, properties, etc.
# 4 - a new instance of the type class is created with the class_name, base_class(es) and the
#     now populated dictionary, the class namespace essentially.

# in practice, type is used this way:  type(name, bases, dict)


#________________________________________________________________________________________________________
import math
class Circle(object):
    def __init__(self, x, y, r):
        self.x = x
        self.y = y
        self.r = r

    def area(self):
        return math.pi * self.r ** 2

# at this point, the Circle object was created. the symbol 'Circle' is in the module namespace:
'Circle' in globals()   # True

# Circle is an object instance of the type class:
type(Circle)   # <class 'type'>

# and its name is Circle:
Circle         # <class '__main__.Circle'>


# as we saw, whenever we are creating instances of some class, Python calls the __new__ and maybe
# the __init__ method as well.

# we are doing the same thing here, but now we are creating an object instance of the type class.
# the syntax here is slightly different. we are using the `class` keyword which calls the type,
# and creates the Circle object (the type instance).


# when Python encounter the class keyword, it gets the name of the class, gets the classes that we 
# want to inherit from, and it also gets all code inside the Circle class.

# then using these things, Python creates a new instance of type.

#________________________________________________________________________________________________________
# lets do all of these steps manually:
# the class body scope is extracted, think of it as a blob of text that contains valid code.

# in order to be able to mimic the creation of a class, we require to use the `exec` function.
# it allow us to work with block of code as text:
namespace = {}
exec('''
a = 10
b = 20

def __init__(self):
    pass

''', globals(), namespace)
# we require to provide access to our module namespace by passing the globals() dictionary, and 
# also an empty dictionary where the exec function will runs that block of code in. 

# we will esssentially runs that block of code inside the `namespace` dictionary and then it will 
# gets populated with content:
namespace  # {'a': 10, 'b': 20, '__init__': <function __init__ at 0x000001>}


# if we had executed that block of code directly in our module, like:
a = 10
b = 20

def __init__(self):
    pass

# we would obviously had our module namespace populated:
globals()   # {...,  'a': 10, 'b': 20, '__init__': <function __init__ at 0x000001>}

# exec basicly does this execution/compilation of the code, but using that dictionary as namespace:
d = {}
exec('''
def add(a, b):
    return a + b

def mul(a, b):
    return a * b
''', globals(), d)

d  # {'add': <function add at 0x000001>, 'mul': <function mul at 0x000002>}
d['add'](10, 20)   # 30
d['mul'](10, 20)   # 200

#________________________________________________________________________________________________________
# creating classes manually by instantiating from type class:

# the type class has different ways that we can call it. 

# we can call it by passing just some object, and it will returns the object type itself:
type(Circle)     # <class 'type'>


# and we can also call the type by passing the class name, class bases and the dictionary. 
# when Python encounter the class keyword, it will essentially calls the type this second way.

# essentially, it does it under the hood: 
class_name = 'Circle'
class_bases = ()   # (object, )
class_namespace = {}

class_body = '''
def __init__(self, x, y, r):
    self.x = x
    self.y = y
    self.r = r

def area(self):
    return math.pi * self.r ** 2
'''

# Python will executes that class_body code but using the class_dictionary as namespace:
exec(class_body, globals(), class_namespace)

# after that, the class_dictionary gets populated with data:
class_namespace  # {'__init__': <function __init__ at 0x000001>, 'area': <function area at 0x000002>}


# now we can create an object instance of the type class, the class object itself:
Circle = type(class_name, class_bases, class_namespace)

type(Circle) # <class 'type'>
Circle       # <class '__main__.Circle'>


# if we look at the Circle object namespace, it gives us back an mapping proxy with extra stuffs,
# but it includes the __init__ and the area that we provided when we called type:
Circle.__dict__ 
# {'__init__': <function __init__ at 0x000001>, 'area': <function area at 0x000002>, ...}

Circle.__name__ # Circle    that is the class_name argument that we passed in.


# the type object instance returned something that we can use now as a class, it is a class. 
# we can create object instances of this class now:
c = Circle(0, 0, 1)
c.__dict__ # {'x': 0, 'y': 0, 'r': 1}

type(c)    # <class '__main__.Circle'>

c.area()   # 3.141592653589793

# as we can see, we use the type class to create new type object instances, new classes essentially.
# and this is why we call the type, a metaclass, cause it is a class that is used to construct other
# classes.

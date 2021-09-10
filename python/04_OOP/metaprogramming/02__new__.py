# The __new__ method

# is used when we are constructing instances of a class. and how do we do that? 
# classes are actually callables, we just need to call the class. for exemple: Person('Fabio')

# this is the first step, and what happens is that, the new class instance is created, and maybe
# it gets initialized in some ways. for exemple the name of that class is added to it, maybe 
# documentation strings is also added and so on.

# then the __init__ method is called, which is bound to the new object instance.

# it happens after the object instance has been created. and gives us a "hook" to customize the 
# initialization of the object instance the way that we want to.

#______________________________________________________________________________________________________
# the question is how that new object instance is actually created? how does it happen?

# essentially, with the __new__ method. the `object` class implements the __new__ method. 
# and it is actually the default implementation of the __new__ that we use to create new objects.

# is used in the creation of object instances of any class data type. so whenever we creates a 
# instances of a given class, the __new__ method gets called.

# we dont usualy write the __new__ in our classes but, all classes inherit from the object class, 
# so we will essentially inherit the __new__ method that is in the object class as well. 
# therefore, whenever we instantiate an object, it will gets called, independent of the class type.
class Person:
    def __init__(self, name):
        print('__init__ called...')
        self.name = name

# we can create a new object instance of the Person class by calling the __new__ method of the
# object class directly just passing the class that we want to instantiate from, like:
p = object.__new__(Person)
type(p)   # __main__.Person

# we got a new Person object, but the __init__ method has not been called. 

# essentially because we are calling the __new__ method directly, that is all that will happen.
# but when we call the class, where Python does some other stuffs, it does call the __new__ method
# and also calls the __init__ method in sequence, under some circunstances.

# but not in this case that we would have to do it explicitly:
p.__init__('Fabio')   # __init__ called...

#______________________________________________________________________________________________________
# __new__ method:
# it works this way in the object class implementation:  object.__new__(cls, *args, **kwargs)

# it requires the first argument to be the class, the class that we want to create an instance of.
# and then it will accept any number of postional and keyword only arguments. 
# but essentially, it doest not do anything with those arguments.

# the __new__ method is a static method. isnt bound to anything. the class is the symbol for the
# class that we want to instantiate from. it accepts *args, **kwargs but doesnt not use them. 

# the only thing is that, if we are going to invoke the class directly, whatever arguments names we
# defined in the __init__, we will need to match the arg names in the __new__ method as well. 

# whatever arguments between the __new__ and __init__, if we implement both methods in our class, 
# those arguments needs to match.


# what the __new__ method does essentially, is returning a new object of the class type we specified. 
# maybe of the type Person, Circle, int, dict, etc...

# just like we can overwrite the __init__, we can overwrite the __new__ method in our own classes. 

# __init__ is present in the object class, and if we dont overwrite that in our classes, we will 
# inherit the default implementation from the object class. 

# we can do it with the __new__ method as well. we just need to to returns a new object instance.

# we usually returns an instance of the same class. like, if we want to create a instance of Person, 
# the __new__ method should returns an object instance of type Person.

# but it doesnt have to. therefore, if we are writing a __new__ method in our class we doesnt 
# return an object instance of the class itself, Python will not call the __init__ method for us.

#______________________________________________________________________________________________________
# Overriding the __new__ method:
# tipically what we do when overwriting the __new__ method, is by doing something before and after
# creating the new instance. 
# we usually delegates the actual creation of the instance to the __new__ method of the object class. 

# in practice when dealing with inheritence, we use the super().__new__ instead of object.__new__ .

# it happens because if we are inheriting from a class that itself implements the __new__ method,
# we dont want to bypass that by calling directly the __new__ of the object class. if we do that,
# we will not call the __new__ method of the parent class that is already implemented.


#______________________________________________________________________________________________________
# the __new__ method will be called whenever we call the class. when we say Person('Fabio'), 
# Python will essentially calls: __new__(Person, 'Fabio') and it will returns a new Person instance.

# if we return an object which the type is the same, Person in this case, Python will calls the 
# __init__ method bound to that new Person instance and calls it with the same arguments, like: 
# new_object.__init__('Fabio')

# but if we dont return an instance of Person from our __new__ method, it doesnt calls the __init__.

# that makes sense, cause if we are returning a different object, how can we know that the 
# __init__ method of that other object takes the same arguments as our Person class? 

# in practice we dont return an different object instance.


#_______________________________________________________________________________________________________
class Point:
    pass

p = Point() # <__main__.Point object at 0x000001>

# what is essentially happening is:
class Point(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

p = object.__new__(Point) # <__main__.Point object at 0x000001>

# it had not called the __init__ method automatically cause we created the object manually:
p.__dict__  # {}

p.__init__(10, 20)
p.__dict__  # {'x': 10, 'y': 20}


# the __new__ method in the object class will allow us to pass any number of positional/keyword 
# only arguments, but will not do anything with them:
p = object.__new__(Point, 10, 20) # <__main__.Point object at 0x000001>

# we still have our object instance created, but nothing is happening with those argument:
p.__dict__  # {}


# that is why we can actually call the class by passing arguments, like:
p = Point(10, 20)

# what is happening behind the scenes is that, Python calls the __new__ passing 10 and 20, then
# the object class just ignores that and when the __new__ method returns a new object, Python calls 
# the __init__ method by passing the same arguments 10 and 20.

#_______________________________________________________________________________________________________
class Point:
    def __new__(cls, x, y): 
# in this case we are saying that we want our __new__ method to have 2 positional arguments and
# they are mandatory, we are overwriting the default __new__ method of the object class.
        print('Creating instance...', x, y)
        instance = object.__new__(cls)
        return instance
    # we are essentially modifying how the object instance gets created.

    def __init__(self, x, y):
        print('__init__ called...', x, y)
        self.x = x
        self.y = y

# now, whenever we creates an instance of Point, it will calls the __new__ method by passing
# the x and y positional arguments:
p = Point(10, 20)
# Creating instance... 10 20   # __new__ method just pass away the x and y values to the __init__.
# __init__ called...   10 20

#_______________________________________________________________________________________________________
# what is interesting about the __new__ method is that we can overwrite it, even when we inherit
# from the builtins data types, which often doesnt work with the __init__.

# for exemple, if we want to inherit from the builtin int class:
class Squared(int):
    def __new__(cls, x):
        return super().__new__(cls, x**2)
    # we are essentially calling the __new__ method of the int class and passing the x**2 argument.

# whenever we instantiate an Squared object, the __new__ method of the integer class will be called 
# with his value squared:
result = Squared(4)      # type(result)  __main__.Squared
result # 16

# we essentially delegated the creation of the instance to the builtin integer class. and by doing 
# that, we also got an instance of the type integer as well:
isinstance(result, int)  # True


# if we try to do this with the __init__ method, that will not work. and that is really just with 
# the builtins cause they are writen in C, they behave slightly different. 

# very often the __init__ method is never actually called or used with the builtins types:
class Squared(int):
    def __init__(self, x):
        print('__init__ called...')
        super().__init__(x**2)

# result = Squared(4)

# __init__ called...
# Traceback (most recent call last):
#   File "02__new__.py", line 207, in <module>
#     result = Squared(4)
#   File "02__new__.py", line 205, in __init__
#     super().__init__(x**2)
# TypeError: object.__init__() takes exactly one argument (the instance to initialize)

# the __init__ method of the int class doesnt take any arguments. so we cannot call this way,
# and there is no real way for us to modify the internal state of it by using the __init__ method.

#_______________________________________________________________________________________________________
# dealing with inheritence and the why we should use super().__new__ instead of object.__new__:
class Person:
    # Person is inheriting from the object class directly in this case.
    def __new__(cls, name):
        print(f'Person: instantiating {cls.__name__}...')
        instance = object.__new__(cls) # so its ok to call the __new__ method directly this way.
        return instance

    def __init__(self, name):
        print('Person: initializing instance...')
        self.name = name

p = Person('Fabio')
# Person: instantiating Person...
# Person: initializing instance...

p.__dict__   # {'name': 'Fabio'}

# the problem is, it doesnt work with inheritence:
class Student(Person):
    # Person class have its own __new__ method, and we want to call it.
    def __new__(cls, name, major):
        print(f'Student: instantiating {cls.__name__}...')
        instance = object.__new__(cls) # but it will not call the Person __new__ method this way.
        return instance

    def __init__(self, name, major):
        print('Student: initializing instance...')
        super().__init__(name)
        self.major = major

s = Student('John', "Major")
# Student: instantiating Student...
# Student: initializing instance...
# Person: initializing instance...

# notice that, the __new__ method of Person class was not called. that because we did that call 
# directly in the object class and it endup not calling the __new__ method of the Person class.

# so what we should really have done was:  super().__new__:
class Student(Person):
    def __new__(cls, name, major):
        print(f'Student: instantiating {cls.__name__}...')
        instance = super().__new__(cls, name) # calling the Person __new__ method now.
        return instance

    def __init__(self, name, major):
        print('Student: initializing instance...')
        super().__init__(name)
        self.major = major

s = Student('John', "Major")
# Student: instantiating Student...
# Person: instantiating Student...
# Student: initializing instance...
# Person: initializing instance...

#_______________________________________________________________________________________________________
# if we can handle the initialization of the class by using the __init__ method, why would we want
# to use the __new__ method to do the initialization?

# it basicly allow us to tweak how the class is created. with the __new__ method, we could 
# actually do everything that is done inside the __init__ method. 

# usually when we have the __new__ method defined we dont write the __init__ method. that is how the
# builtin works essentially.

# the initialization phase of instances is done right after the object instance gets created. 
# but we can do everything that we need during the object instace creation, we dont have to wait
# the initialization happens:
class Square:
    def __new__(cls, w, l):
        cls.area = lambda self: self.w * self.l
        # we are injecting this function in the Square class before we even initialize it.

        instance = super().__new__(cls)
        # we can also tweak the object instances before the initialization:
        instance.w = w
        instance.l = l
        return instance

s = Square(2, 3)   # s.__dict__   {'w': 2, 'l': 3}
s.area()  # 6

# keep in mind that __new__ is an static method, and we could also call it manually, we just need
# to remember to pass the class that we want to creates an instance of as the first argument:
s = Square.__new__(Square, 2, 3)
s.__dict__   # {'w': 2, 'l': 3}
s.area()     # 6

# by doing it manually, it will not call the __init__ method automatically. even if we had it.


# but in this case it doesnt matter, cause we are doing everything in the __new__ method.
# and this is why things like that also works with the builtins. they are essentially doing all 
# initialization in the __new__ method.

#_______________________________________________________________________________________________________
# in the other hand, whenever we call it by using the callable, like:   Square(3, 4)
# then the __init__ method does get called, in some cirscunstances:
class Square:
    def __new__(cls, w, l):
        cls.area = lambda self: self.w * self.l
        instance = super().__new__(cls)
        instance.w = w
        instance.l = l
        return instance  # we are returning an Square object. so it does call the __init__ method.

    def __init__(self, w, l):
        print('__init__ called...')

Square(3, 4)  # __init__ called...


# Python does it for us whenever we invoke the class. essentially Python calls the __new__ method 
# and if the __new__ method returns the same type (Square object), then Python calls the 
# __init__ method of that class automatically. otherwise, it dont:
class Person:
    def __new__(cls, name):
        print(f'Creating instance of {cls.__name__}... not really...')
        instance = str(name)  # type(instance)  <class 'str'>
        return instance 
    # does not return an Person object. the __init__ method wont get called automatically.

    def __init__(self, name):
        print('__init__ called? not really...')
        self.name = name

p = Person('Fabio')   # Creating instance of Person... not really...
p, type(p)   # Fabio <class 'str'>

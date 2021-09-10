# Metaprogramming

# is a programming technique in which computer programs have the ability to treat other programs
# as their data.
# it means that, a program can be designed to read, generate, analyze or transform other programs,
# and even modify itself while running.

# basicly we can use code to modify code at runtime. and it also keeps the code DRY. we want to
# write our code once and reuse it as many time as possible.

#________________________________________________________________________________________________________
# we already know some metaprogramming techniques.
# Decorators uses code to modify the behavior of another piece of code. we can use a function
# to modify how other functions behaves without actually modifying that function directly:
def debugger(fn):
    def wrapper(*args, **kwargs):
        print(f'{fn.__qualname__} ->', args, kwargs)
        return fn(*args, **kwargs)
    return wrapper

@debugger
def f1(*args, **kwargs):
    pass

f1(4, 2, name='Fabio')  # f1 -> (4, 2) {'name': 'Fabio'}

# if we want to modify how the debugger function works, we can do it by simple modifying that 
# specific function. we dont require to repite ourselves by copying and paste in the remaining 
# functions, we are essentially modifying them all during runtime execution with our decorator.


# Descriptors uses code to essentially modify the behavior of the dot (.) operator:
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

p = Point(10, 20)
p.__dict__  # {'x': 10, 'y': 20}

# by default, when we use the dot (.) operator, we are actually going into the instance namespace:
p.x   # 10

class IntegerField:
    def __set_name__(self, owne, property_name):
        self.property_name = property_name

    def __get__(self, instace, owner):
        print('__get__ called...')
        return instace.__dict__.get(self.property_name)

    def __set__(self, instance, value):
        print('__set__ called...')
        if not isinstance(value, int):
            raise TypeError('Must be integer')
        instance.__dict__[self.property_name] = value

class Point:
    x = IntegerField()
    y = IntegerField()

    def __init__(self, x, y):
        self.x = x 
        self.y = y
# whenever we use the dot operator now, we will actually call the __set__ method of the descriptor.

p = Point(10, 20)
# __set__ called...   p.x = 10
# __set__ called...   p.y = 20

p.x  
# __get__ called...   10

# we essentially modified how the dot (.) works. we are basicly injecting ourselves in that workflow.

# if we want to change something just like with the decorators, like, if we want to change how our
# IntegerField class behaves, we can do it, we can modify that code and that code will basicly 
# modify how the Point class will works, and how the dot operator works. but we dont actually have
# to modify the code inside the Point class at all, we just do it in the descriptor itself.

#________________________________________________________________________________________________________
# Metaclasses
# when it comes to metaprogramming, the very first thing that cames to everyones mind is Metaclasses.

# how they are used in the creation of classes (types).
# we can think of a metaclass as a class (type) factory. something that allow us to create classes.
# how we can use them to hook into the class creation cycle, not just the class instantiation, but
# the class creation like, when we creates a class by using the `class` keyword, something is 
# creating that object, that type object.

# metaclasses dont always play nicely with multiple inheritences.

#________________________________________________________________________________________________________
# word of caution
# "Metaclasses are deeper magic than 99% of users should ever worry about. if you wonder wheter
#  you need them, you dont. (the people who actually need them know with certainty that they
#  need them, and dont need an exxplanation about why)." - Tim Peters.

# the ideia is that, is very easy to abuse with metaclasses.
# superficially, metaclasses are not difficult to understand. but the details can get complicated.
# so knowing when to use a metaclass is not easy. unless you come across a problem where the use
# of a metaclass is obvious, dont use them. it makes code harder to read.

# just because you have a new hammer, doesnt mean everything is a nail.

# in general, if we're writing a library/framework, maybe we need to use metaclasses. but if 
# we're going to write an application code that is specific to solve a particular problem, we 
# probably dont need metaclasses.

# metaclasses provides an deeper insight into Python internal mechanics and how thing works.

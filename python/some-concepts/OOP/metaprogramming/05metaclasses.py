# Metaclasses

# at this point, metaclasses gets quite easy to understand.
# first, we saw how type class is used to create classes:   type(name, bases, dict)
type('Person', (), {}) # <class '__main__.Person'>

# we saw how we can customize the type by subclassing it and overriding the __new__ method.
class MyType(type):
    # overriding __new__ method...
    pass

MyType('Person', (), {})    # <class '__main__.Person'>

# but this approach was really painful, we had to get the class body code as text, create the
# class namespace (dictionary), we had to execute the code within that dictionary, we had to
# determine the bases, and later on call MyType.



# creating classes normally:
# when we create classes normally we usually use the class keyword only. we dont require to
# call the type() to do it:
class Person():
    pass
class Student(Person):
    pass

# Python somehow takes care of all that manual steps we were doing. Python itself is 
# responsible to call the type and pass the class name, base, dict, etc.


# but what if we have an custom type class for exemple:
class MyType(type):
    def __new__(cls, name, bases, dict):
        # do stuffs...
        pass

# and we want Python to do that automatic proccess after encounter the `class` keyword but 
# we want Python to call our custom type to create the class object instead type, 
# what could we do?

# this has a technical name, its called Metaclass. 
# for exemple, when we create the class Student, by default its metaclass is type.
# but instead, we just need to tell Python to use our custom type to create the type instance. 
# we dont want Python to use the default type class to do it.

#___________________________________________________________________________________________________
# Metaclass:
# to create a class, another class is used. and its tipically the type class.

# the class used to create a class is called the metaclass of that class. and by default,
# Python uses the type class as the metaclass.

# but we can override it, and all we need to do is to specify the metaclass keyword argument
# when we define some class:
class Person(metaclass=MyType):
    pass

# when we do that, Python will know it should use our custom type (MyType) to creates the 
# Person class object instead of using the default type class to do that.

# Python will do all that work that we were doing, the only thing now is that, instead of 
# calling type to create an instance of type (class object), it will call our custom type to
# create an instance of type (class object).

# by default, when we create some class by using the class keyword, Python do it essentially:
class Person(metaclass=type):
    # we could write it explicitly but Python does it under the hood by default.
    pass

# but if we want to customize that, then we should use the metaclass keyword argument and 
# specify which metaclass we want to use to create that class object.

#______________________________________________________________________________________________
# putting it together:
class MyType(type):
    def __new__(mcls, name, bases, class_dict): # mcls is the MyType class.
        # tweak...
        # create the class object by delegating it to the type class __new__ method:
        class_instance = super().__new__(mcls, name, bases, class_dict)
        # tweak...
        return class_instance  # then return the new class object.

# so now, when we create a class, like:
class Person(metaclass=MyType):
    def __init__(self, name):
        self.name = name

# Python it will creates that Person class object by using our custom type (MyType).
Person  # <class '__main__.Person'>


# essentially, Python will do it when it see the `class` keyword:
class_namespace = {}
class_body = """
def __init__(self, name):
    self.name = name
"""

exec(class_body, globals(), class_namespace)

Person = MyType.__new__(MyType, 'Person', (), class_namespace)

Person  # <class '__main__.Person'>


# its basicly the same thing that we have been doing, but now we have Python doing all the
# hard work for us.

#______________________________________________________________________________________________






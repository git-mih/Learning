# Metaclass parameters

# we saw how regular metaclasses are used, by creating a metaclass by inheriting from type and
# then we have the __new__ method where Python will pass in the metaclass, name, bases, cls_dict
# arguments automatically for us, then we do whatever we want and return that new class object:
class MetaClass(type):
    def __new__(mcls, name, bases, class_dict):
        return super().__new__(mcls, name, bases, class_dict) # <'.MetaClass' object at 0x0001>

# then we use it by specificing the metaclass keyword argument, like:
class MyClass(metaclass=MetaClass):
    pass


# so the question is, can we pass extra parameters to that __new__ method? how we can do that?

#____________________________________________________________________________________________________
# we just require to add any number of additional parameters inside the __new__ method:
class MetaClass(type):
    def __new__(mcls, name, bases, class_dict, arg1, arg2, arg3=None):
        return super().__new__(mcls, name, bases, class_dict) 


# now we need to specify these extra arguments when we define the custom class. but, these
# extra arguments must be assed as named arguments only:
class MyClass(metaclass=MetaClass, arg1=10, arg2=20, arg3=30):
    pass

# we require to pass named arguments cause, the positional arguments are intended to be the 
# classes that we are inheriting from. for exemple:
class MyClass(object, metaclass=MetaClass, arg1=10, arg2=20):
    pass

# notice that, we require to use the keyword argument `metaclass` as well, and any number of
# arguments that we pass in after it, is required to be keyword argument as well.

# we could also specify these extra arguments before the `metaclass` argument as well. we just
# require to use named arguments to differentiate them from positional arguments that are ment
# to be the classes that we want to inherit from:
class MyClass(object, arg1=10, arg2=20, arg3=30, metaclass=MetaClass):
    pass


#____________________________________________________________________________________________________
class AutoClassAttrib(type):
    # lets store these extra attributes inside a tuple, where the first value of the tuple is 
    # going to be the attribute name, and the second value will be the value itself.
    def __new__(mcls, name, bases, class_dict, extra_args=None):
        if extra_args:
            print(f'creating {name} class with extra attributes:', extra_args)
            for attr_name, value in extra_args: 
                class_dict[attr_name] = value
        return super().__new__(mcls, name, bases, class_dict)
    # we injected those extra arguments before the new class object gets created. we are
    # injecting it inside the class_dict (class namespace) essentially.
        
class Account(metaclass=AutoClassAttrib, extra_args=(('account_type', 'savings'), ('apr', 0.5))):
    pass

# when Account class object gets created:
# creating Account class with extra attributes: (('account_type', 'savings'), ('apr', 0.5))

Account.__dict__  # {'account_type': 'savings', 'apr': 0.5, ...}


# we could also inject these extra arguments after we create the class object:
class AutoClassAttrib(type):
    def __new__(mcls, name, bases, class_dict, extra_args=None):
        class_instance = super().__new__(mcls, name, bases, class_dict)
        if extra_args:
            print(f'creating {name} class with extra attributes:', extra_args)
            for attr_name, value in extra_args: 
                setattr(class_instance, attr_name, value)
        return class_instance
        
class Account(metaclass=AutoClassAttrib, extra_args=(('account_type', 'savings'), ('apr', 0.5))):
    pass
# creating Account class with extra attributes: (('account_type', 'savings'), ('apr', 0.5))

vars(Account)    # {..., 'account_type': 'savings', 'apr': 0.5}



# passing the extra arguments inside a tuple is kinda tedious, we could use **kwargs instead:
class AutoClassAttrib(type):
    def __new__(mcls, name, bases, class_dict, **kwargs): # kwargs = {'acc': '01', 'apr': 0.6}
        class_instance = super().__new__(mcls, name, bases, class_dict)
        if kwargs:
            for k, v in kwargs.items():  # dict_items([('acc', '01'), ('apr', 0.6)])
                setattr(class_instance, k, v)
        return class_instance
        
# now we can pass our extra attributes this way:
class Account(metaclass=AutoClassAttrib, acc='01', apr=0.6):
    pass

Account.__dict__  #  {..., 'acc': '01', 'apr': 0.6}


# or we could just update the class namespace (dictionary) with the dictionary that we passed 
# to the metaclass in extra arguments:
class AutoClassAttrib(type):
    def __new__(mcls, name, bases, class_dict, **extra_args):
        print(extra_args)
        class_dict.update(extra_args) 
        class_instance = super().__new__(mcls, name, bases, class_dict)
        return class_instance
        
class Person(metaclass=AutoClassAttrib, first_name='Fabio', age=26, city='POA'):
    pass

# we gonna update the class namespace (class_dict) with this extra_args dictionary:
# extra_args = {'first_name': 'Fabio', 'age': 26, 'city': 'POA'}

Person.__dict__   # {..., 'first_name': 'Fabio', 'age': 26, 'city': 'POA', ...}

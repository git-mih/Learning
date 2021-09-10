# The __prepare__ method

# recalling that, in a metaclass the __new__ method gets called by Python. and whenever a 
# metaclass is called, for exemple:  class MyClass(metaclass=MetaClass), Python will essentially 
# determine and sends to the __new__ method of the metaclass:
#   the metaclass used to create the class (mcls)
#   the name of the class object that we are creating (name)
#   it pass the classes that we are inheriting from (bases)
#   and a dictionary that is used to be the class namespace (class_dict)


# whenever a metaclass is called, it receives an dictionary, the `class_dict` essentially.
# that dict object is what become the class namespace:
class MyMeta(type):
    def __new__(mcls, name, bases, class_dict, **kwargs):
        print(f'calling: MyMeta.__new__({mcls.__name__}, {name}, {bases}, {class_dict}, {kwargs})')
        return super().__new__(mcls, name, bases, class_dict)
    
class MyClass(metaclass=MyMeta):
    pass

# calling: MyMeta.__new__(MyMeta, MyClass, (), {'__module__': '__main__', 
#                                               '__qualname__': 'MyClass'}, {})
# mcls: <class '__main__.MyMeta'> <class 'type'>
# name: MyClass                   <class 'str'>
# bases: ()                       <class 'tuple'>
# class_dict: {'__module__': '__main__', '__qualname__': 'MyClass'}  <class 'dict'>
# kwargs: {}                      <class 'dict'>


# the question is, where does that `class_dict` dict object come from? 
# essentially, Python is responsible to provide it for us. but we could actually intercept that 
# and inject data inside that dictionary even before the __new__ method gets called. 

# the __prepare__ method of the metaclass provide us that "hook". this method is what actually 
# creates the dictionary object that will be used as the class dictionary (namespace):


# the way that __prepare__ method works is that, before the __new__ method gets called,
# Python calls the __prepare__ method to creates the base dictionary that is going to be the 
# class namespace. then, it injects whatever it needs to, like __qualname__, __module__, etc. 
# and pass it along to the __new__ method. 

# if we dont override it, we get the default __prepare__ method implementation of type:
type.__prepare__() # {} empty dict.

# the type class implement the __prepare__ method, and its implementation just returns an empty 
# dictionary by default.

#________________________________________________________________________________________________________
# but we can override the default implementation of type __prepare__ method:
# its important to understand that, if extra arguments are passed to the metaclass, they require
# to be passed to the __prepare__ method as well, cause the __prepare__ method is called before
# the __new__:
class MyMeta(type):
# __prepare__ method is a static method, but we dont require to specify @staticmethod.
    def __prepare__(name, bases, **kwargs):
        print('__prepare__ called... creating the class object namespace (dictionary)')
        print(f'passing kwargs: {kwargs} to the __new__ method.')
        return {'a': 100, 'b': 200} # `class_dict` (namespace)
# Python inject some pre-defined data like, __module__, __name__ before it calls the __new__ method.

    def __new__(mcls, name, bases, class_dict, **kwargs):
        # class_dict = {'a': 100, 'b': 200, '__module__': '__main__', '__qualname__': 'MyClass'}
        print('__new__ called... got the `class_dict` and preparing to create the class object')
        print(f'receiveing kwargs: {kwargs} from the __prepare__ method.')
        return super().__new__(mcls, name, bases, class_dict)

class MyClass(metaclass=MyMeta, kw1=1, kw2=2):
    # these extra arguments will be passed to the __prepare__ **kwargs dictionary. and Python 
    # will pass away it to the __new__ method. it means that, if we are expecting our metaclass
    # to receive extra arguments in the __new__ method, we require to provide it to the 
    # __prepare__ as well.
    pass

# during class compilation, Python calls the __prepare__ first, then call __new__ method in sequence:

# __prepare__ called... creating the class object namespace (dictionary)
# passing kwargs:    {'kw1': 1, 'kw2': 2} to the __new__ method.
# __new__ called...     got the `class_dict` and preparing to create the class object
# receiveing kwargs: {'kw1': 1, 'kw2': 2} from the __prepare__ method.}


# better solution to inject data inside the class namespace would be:
class MyMeta(type):
    def __prepare__(name, bases, **kwargs):
# class_dict = {'arg1': 10, 'arg2': 20, 'arg3': 30}
        return kwargs  

    def __new__(mcls, name, bases, class_dict, **kwargs):
# class_dict = {'arg1': 10, 'arg2': 20, 'arg3': 30, '__module__': '__main__', '__qualname__': 'MyClass'}
        return super().__new__(mcls, name, bases, class_dict)

class MyClass(metaclass=MyMeta, arg1=10, arg2=20, arg3=30):
    pass

MyClass.__dict__ # {'arg1': 10, 'arg2': 20, 'arg3': 30, '__module__': '__main__', ...}


#__________________________________________________________________________________________________________
# what is really interesting about the __prepare__ method is that, it just need to return some
# object that is instance of an dict, it doesnt have to be a dict object only:
from collections import OrderedDict

isinstance(OrderedDict(), dict)  # True

class MyMeta(type):
    def __prepare__(name, bases): # not expecting extra arguments.
        d = OrderedDict()
        d['bonus'] = 'Python rocks!'
        return d

    # in this case, we are not expecting extra arguments during the class object creation.
    # therefore, we dont require to explicitly write the __new__ method, we can simple use the 
    # default type __new__ method implementation instead.

class MyClass(metaclass=MyMeta):
    pass

vars(MyClass)  # {'bonus': 'Python rocks!', '__module__': '__main__', ...}


# the thing that gets returned from the __prepare__ method just needs to be a dict or a subclass
# of dict. any mapping object can be returned.

#_______________________________________________________________________________________________________________
class CustomDict(dict):
    def __setitem__(self, key, value):
        print(f'setting {key} = {value} in custom dictionary')
        super().__setitem__(key, value)

    def __getitem__(self, key):
        print(f'getting {key} from custom dictionary')
        return int(super().__getitem__(key))

class MyMeta(type):
    def __prepare__(name, bases):
        return CustomDict()
    
class MyClass(metaclass=MyMeta):
    pass

# getting __name__ from custom dictionary
# setting __module__ = __main__ in custom dictionary
# setting __qualname__ = MyClass in custom dictionary

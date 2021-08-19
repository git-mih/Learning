# Attribute write accessors

# we saw how the getters accessors __getattribute__ and __getattr__ method was used.

# whenever we are trying to set an attribute, it will always call the __setattr__ method.
# also, there is no corresponding __setattribute__ method like the getters.


# if we are trying to set an attribute that doesnt exist yet, the __setattr__ method create that
# attribute inside the object namespace (__dict__).


# default attribute setter flow:
#                                  obj.age = 26      or  setattr(obj, 'age', 26)
#                                      |
#                            obj.__setattr__('age', 26)
#                                      |
#   the attribute 'age' is inside the class namespace? including parent classes namespace?
#               |                                                          |
#              YES                                                        NOP
#               |                                                          |
#     is it a data descriptor?                                             |
#      |                   |                                               |
#     YES                 NOP ________________ is it inside the object instance namespace?
#      |                                          |                              |
#   call __set__                                 YES                            NOP
# passing the value                               |                              |
#                                       update the value or             raise AttributeError
#                                       insert if isnt there


# the same caveats regarding infinite recursion happens here as well.
# in practice we should use the super().__setattr__ if we want to set an attribute. so we can 
# avoid infinite recursion issues with that.


# we can also override how we set class attributes. to do that, we require to override the 
# __setattr__ method inside the metaclass.


#________________________________________________________________________________________________________
class Person:
    def __setattr__(self, name, value):
        print(f'__setattr__ called. setting instance attribute...')
        super().__setattr__(name, value)
# we often intercept the __setattr__ method do something with it and then we delegate back to the 
# parent actually do the work.

p = Person()
p.name = 'Fabio'   # __setattr__ called. setting instance attribute...

# now we got that new attribute inside the object namespace: 
p.__dict__         # {'name': 'Fabio'}



# if we try to set an class attribute, the __setattr__ method is not gonna get called:
Person.city = 'POA'

# we do have this entry inside the class namespace:
Person.__dict__    #  {..., 'city': 'POA'}

# but we did not overrided the default class __setattr__ method. to do that, we require to override
# it inside the metaclass:
class MyMeta(type):
    def __setattr__(self, name, value):
        print(f'__setattr__ called. setting class attribute...')
        super().__setattr__(name, value)

class Person(metaclass=MyMeta):
    def __setattr__(self, name, value):
        print(f'__setattr__ called. setting instance attribute...')
        super().__setattr__(name, value)

# now that we overrided the metaclass __setattr__ method, it will be called whenever we try to
# set a class attribute:
Person.city = 'POA'  # __setattr__ called. setting class attribute...
Person.__dict__      #  {..., 'city': 'POA'}

#_________________________________________________________________________________________________________
# dealing with descriptors:
# if the __setattr__ method is trying to set a data descriptor object, Python will calls the 
# __set__ method of the data descriptor instead:
class NonDataDescriptor:
    def __get__(self, instance, owner_class):
        print(f'non-data descriptor __get__ called...')

class DataDescriptor:
    def __set__(self, instance, value):
        print(f'data descriptor __set__ called...')

    def __get__(self, instance, owner_class):
        print(f'data descriptor __get__ called...')


class Person:
    non_data_descriptor = NonDataDescriptor()
    data_descriptor = DataDescriptor()

    def __setattr__(self, name, value):
        print(f'__setattr__ called...')
        super().__setattr__(name, value)

p = Person()

p.data_descriptor = 100  
# __setattr__ called...
# data descriptor __set__ called...

# the __setattr__ method gets called, then it delegate back to the parent. the parent call the
# __setattr__ method and figures out that, the attribute is a data descriptor object, therefore,
# it call the __set__ method on the data descriptor.

p.non_data_descriptor = 200   
# __setattr__ called...

# the non-data descriptor doesnt have the __set__ method defined. therefore, it set the value
# inside the object instance dictionary:
p.__dict__  # {'non_data_descriptor': 200}



# __setattr__ method can be used to intercept and customize any set attribute operation on the
# instance that the method is defined. we are essentially overriding the dot operator, but this
# time we are overriding the dot operator of the assignment.

#___________________________________________________________________________________________________
# infinite recursion issue:
# suppose that we dont want certain values for attributes that starts with a single underscore:
class Person:
    def __setattr__(self, name, value):
        print(f'__setattr__ called...')
        if name.startswith('_') and not name.startswith('__'):
            raise AttributeError(f'attribute: {name} is read-only.')
        setattr(self, name, value)
# it call the __setattr__ method on our instance which will call __setattr__ method again.

p = Person()

try:
    p._name = 'Fabio'   
except AttributeError as ex:
    print(ex)

# __setattr__ called...
# AttributeError: attribute: _name is read-only.

# but if we set an attribute that is valid, that doesnt start with a single underscore:
# p.name = 'Fabio'   
# __setattr__ called...
# __setattr__ called...
# __setattr__ called...
# RecursionError: maximum recursion depth exceeded while calling a Python object

# very often when we are overriding the dunder getattribute, getattr or setattr methods, we dont 
# want to deal with it directly or by using `self.` approach. we really should be using super() instad:
class Person:
    def __setattr__(self, name, value):
        print(f'__setattr__ called...')
        if name.startswith('_') and not name.startswith('__'):
            raise AttributeError(f'attribute: {name} is read-only.')
        super().__setattr__(name, value)
        # this way we dont call ourselves with `self` again and again.

p = Person()

p.name = 'Fabio'  # __setattr__ called...
p.__dict__        # {'name': 'Fabio'}

# The __prepare__ method

# recalling that, in a metaclass the __new__ method gets called by Python. 
# whenever the metaclass is called, like: class MyClass(metaclass=MetaClass),
# Python will determine and sends to the __new__ method of the metaclass:
#   the metaclass used to create the class (mcls)
#   the name of the class object that we are creating (name)
#   it pass the classes that we are inheriting from (bases)
#   and a dictionary that is used to be the class namespace (class_dict)

# the question ins, where does that `class_dict` dictionary come from? Python is responsible to
# provide it for use, but there is actually a "hook" that we can use to inject data inside 
# that dictionary before Python pass it to the __new__ method. 

# the __prepare__ method of the metaclass provide us that "hook".

# what happens is that, the type implement this and the type implementation of __prepare__ method 
# just returns an empty dictionary by default.

# but this __prepare__ method is what actually creates the dictionary object that will be used
# as the class dictionary (namespace).


# we can override the default implementation of type __prepare__ method:
# the __prepare__ method is a static method, but more importantly is that, if additional named
# arguments are passed to the metaclass, they will be passed to the __prepare__ method as well.

# Python will calls the __prepare__ method before it calls __new__.

# the __prepare__ doesnt have to return an dictionary object itself, it can also returns any 
# subclasses of it as well.

# the return value of the __prepare__ method must be a mapping type object.

# after the __prepare__ method gets called, Python will manipulate that dictionary by injecting
# some entries, like the __name__, __module__, etc.

# finally, Python calls the __new__ method and pass that returned mapping type object as the
# `class_dict` argument. this dictionary will be the class object namespace.

#___________________________________________________________________________________________________



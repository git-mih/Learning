# Raising exceptions

# to create that propagation workflow, we use the raise statement to raise an exception.

# we cannot raise any custom class or object:
from typing import Type


class Person:
    pass

# raise Person      TypeError: exceptions must derive from BaseException


# it have to be an object that inherits from BaseException class, the class itself doesnt have 
# to be a direct sublcass.
# raise ValueError()




# BaseException
# provides a __init__ that can handle an arbitrary number of positional arguments (*args).
# when we create an instnace of an exception, we dont have to pass a single value. we can pass
# as many values that we want while creating that instance. then we are able to recover it in
# the exception instance by using the `args` attribute of the exception object instance. it is
# also used in the str() and repr() representations that BaseException implements for us.

# subclasses inherit this behavior.
ex = ValueError('a', 'b', 'c')

ex.args  # ('a', 'b', 'c')
str(ex)  # ('a', 'b', 'c')
repr(ex) # ValueError('a', 'b', 'c')

# we are not limited by just a single error message, but in general that is what we do and we 
# usually use the first argument as the custom error message.



# re-raising current exception being handled:
# when we are handling an exception, when we are inside the except clause, then we can re-raise
# the current exception. and all we have to do is just use the raise statement. we dont pass
# any specific object, Python knows that we want to take the current exception instance and
# raise it.
# we are basicly resuming the propagation workflow of that exception. as if we had not 
# interrupted.
# this is something really useful to things like bare exception handlers:
try:
    pass
except:
# we intercept that exception instance that raised, do something with that, and then we let
# the exception propagates again. we re-raise that same exception by just using the raise:
    raise



# exception traceback:
# as we saw with nested exceptions, we saw exception handlers that raise other exceptions.
# the "final" exception traceback show us a history of this, if we look at the traceback from
# the top level, we see everything that occurred.
try:
    raise ValueError()
except ValueError:
    try:
        raise TypeError()
    except TypeError:
        """final"""
        # raise KeyError()


# Traceback (most recent call last):
#   File "03raising.py", line 63, in <module>
#     raise ValueError()
# ValueError

# During handling of the above exception, another exception occurred:

# Traceback (most recent call last):
#   File "03raising.py", line 66, in <module>
#     raise TypeError()
# TypeError

# During handling of the above exception, another exception occurred:

# Traceback (most recent call last):
#   File "03raising.py", line 68, in <module>
#     raise KeyError()
# KeyError

# sometimes this is too much information for our users, we dont want the user to be aware of
# this TypeError exception that occurred for exemple.

# our internal implementations should maybe remain opaque and we have a way to do that.

# using raise... from...
# when we do a raise from, we can control at some extent what traceback will be included:
try:
    raise ValueError()
except ValueError:
    try:
        raise TypeError()
    except TypeError:
        pass
        # raise KeyError() from None

# Traceback (most recent call last):
#   File "03raising.py", line 105, in <module>
#     raise KeyError() from None
# KeyError

# if we follow this propagation workflow, technically we got the KeyError, TypeError, ValueError.
# but the only thing the user is going to see in the traceback is the KeyError.

# we can also decide that we want to raise from other exception:
try:
    raise ValueError()
except ValueError:
    try:
        raise TypeError()
    except TypeError:
        pass
        # raise KeyError() from ValueError()

#   File "03raising.py", line 105, in <module>
#     raise KeyError() from ValueError()
# KeyError
# PS C:\Users\pauloendoh\workspace\Learning\python\some-concepts\OOP\exceptions> py .\03raising.py
# ValueError

# The above exception was the direct cause of the following exception:

# Traceback (most recent call last):
#   File "03raising.py", line 122, in <module>
#     raise KeyError() from ValueError()
# KeyError

# note that we are bypassing the TypeError. we are raising the KeyError directly from the 
# ValueError exception.

# it is useful to hide exception stacks that are just implementation details.

#________________________________________________________________________________________________________________

# exception workflows can be initiated by using the raise statement. 
# in order to raise an exception we need to raise an instance of some exception type that 
# inherits directly or indirectly from the BaseException.

# we cant raise an object instance of some class that isnt a subclass of BaseException:
class Person:
    pass
try:
    raise Person()
except TypeError as ex:
    ex  # TypeError: exceptions must derive from BaseException

# all the standart exceptions in Python derives from BaseException. 
# BaseException allows any number of positional arguments (*args) in the initializer. the 
# only place that we use these arguments is in the `args` attribute and the representations,
# str() and repr().
ex = BaseException('a', 'b', 'c')
ex.args  # ('a', 'b', 'c')
str(ex)  # ('a', 'b', 'c')
repr(ex) # BaseException('a', 'b', 'c')

# any other exception that inherits from BaseException also inherits these functionalities:
ex = ValueError('a', 'b', 'c')
ex.args  # ('a', 'b', 'c')
str(ex)  # ('a', 'b', 'c')
repr(ex) # BaseException('a', 'b', 'c')

# often we just use a single argument which is usually some type of explanatory message. but is
# also handy to have the option of extra arguments avaiable.



# there is some useful variations in the raise statement. sometimes we want to catch an 
# exception and try to handle it, and maybe because we either never planed to handle the 
# exception, we just wanted to intercept the exception so we could do something with it. but we
# really want that exception propagation to continue unhandled. or we do handle that specific 
# exception and for some reason we need to re-raise that same exception, we need to continue
# propagating that exception workflow as if we did not had handled the exception.

try:
    1 / 0
except ZeroDivisionError as ex:
    print('logging exception...', repr(ex))
    # raise

# logging exception... ZeroDivisionError('division by zero')   

# Traceback (most recent call last):
#   File "03raising.py", line 185, in <module>
#     1 / 0
# ZeroDivisionError: division by zero

# we got the logging, we essentially intercepted that ZeroDivisionError, but then we re-raise
# that exception to let it propagates back as if we had not intercepted.



# sometimes we want to change a particular exception that we want to raise. this is useful for
# when we want to use custom exceptions:
class CustomError(Exception):
    """a custom exception"""
try:
    1 / 0
except ZeroDivisionError as ex:
    print('logging exception...', ex)
    # raise CustomError(*ex.args)

# we essentially "handled" the ZeroDivisionError and raised a different exception instead:
# logging exception... ZeroDivisionError('division by zero')

# Traceback (most recent call last):
#   File "03raising.py", line 208, in <module>
#     1 / 0
# ZeroDivisionError: division by zero

# During handling of the above exception, another exception occurred:

# Traceback (most recent call last):
#   File "03raising.py", line 211, in <module>
#     raise CustomError(*ex.args)
# __main__.CustomError: division by zero

# we get the CustomError raised, one very important thing to know is the traceback. 
# notice that during the handling of the ZeroDivisionError exception, another exception occurred.
# we raised CustomError.



# we can have more levels of nesting as well:
try:
    raise ValueError('level 1')
except ValueError:
    try:
        raise TypeError('level 2')
    except TypeError:
        # raise KeyError('level 3')
        pass

# Traceback (most recent call last):
#   File "03raising.py", line 234, in <module>
#     raise ValueError('level 1')
# ValueError: level 1

# During handling of the above exception, another exception occurred:

# Traceback (most recent call last):
#   File "03raising.py", line 237, in <module>
#     raise TypeError('level 2')
# TypeError: level 2

# During handling of the above exception, another exception occurred:

# Traceback (most recent call last):
#   File "03raising.py", line 239, in <module>
#     raise KeyError('level 3')
# KeyError: 'level 3'




try:
    raise ValueError('level 1')
except ValueError:
    try:
        raise TypeError('level 2')
    except TypeError:
        # raise KeyError('level 3') from None
        pass

# Traceback (most recent call last):
#   File "03raising.py", line 239, in <module>
#     raise KeyError('level 3')
# KeyError: 'level 3'




try:
    raise ValueError('level 1')
except ValueError as ex_1:
    try:
        raise TypeError('level 2')
    except TypeError as ex_2:
        # raise KeyError('level 3') from ex_1
        pass

# Traceback (most recent call last):
#   File "03raising.py", line 283, in <module>
#     raise ValueError('level 1')
# ValueError: level 1

# The above exception was the direct cause of the following exception:

# Traceback (most recent call last):
#   File "03raising.py", line 288, in <module>
#     raise KeyError('level 3') from ex_1
# KeyError: 'level 3'






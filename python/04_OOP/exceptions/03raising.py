# Raising exceptions

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



# all standart exceptions in Python derives from BaseException class.
# BaseException initializer can receives any number of positional arguments. 
# and these arguments keep stored inside the `args` attribute as a tuple value. 
# we can also get these values by using str/repr representation functions:
ex = BaseException('a', 'b', 'c')
ex.args  # ('a', 'b', 'c')
str(ex)  # ('a', 'b', 'c')
repr(ex) # BaseException('a', 'b', 'c')

# we often just use a single argument thats is usually some type of explanatory message. 
# but the option of having extra arguments is very handy tho.

# any other exception instance that inherits from BaseException will get these functionalities:
ex = ValueError('a', 'b', 'c')
ex.args  # ('a', 'b', 'c')
str(ex)  # ('a', 'b', 'c')
repr(ex) # BaseException('a', 'b', 'c')


#_____________________________________________________________________________________________________
# there is some useful variations in the raise statement, like re-raising exceptions or raise 
# different exceptions instead.


# re-raising exceptions:
# whenever we are handling an exception (inside the except clause essentially), we can 
# re-raise the current exception. 

# all we have to do is just use the raise statement without referencing any exception instance,
# Python will raise the current exception that was beeing handled.

# we are basicly resuming the propagation workflow of that exception. as if we had not 
# interrupted that.

# this is really useful to use with bare exception handlers:
try:
    pass
except:
    # intercept some exception instance that raised, do something with that. then we let the 
    # exception propagates again. we re-raise that same exception instance.
    raise


# exemple with specific exception handler:
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

# we essentially intercepted that ZeroDivisionError, "handled" that by simple logging, and 
# then we re-raise that same exception to let it propagates back as if we had not intercepted.

#_____________________________________________________________________________________________________
# we can trap a particular exception instance, and raise a different exception instead.
# this is useful for when we want to use custom exceptions:
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


# its very useful to know how the traceback works, notice that during the handling of the 
# ZeroDivisionError exception, another exception occurred.

#_____________________________________________________________________________________________________
# exception traceback:

# with nested exceptions, we saw exception handlers that raise other exceptions.
# if we look at the traceback from the top level, we see everything that occurred:
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

# sometimes this is too much information for our users, we dont want the user to be aware of
# the ValuerError or TypeError exception that occurred before it for exemple.


# our internal implementations should maybe remain opaque and we have a way to do that.
# with `raise...from`, we can control at some extent what will be included in the traceback:

# we can use `from None` to display only the last traceback object:
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

# if we follow the propagation workflow, we technically got the Key, Type and ValueError.
# but the traceback will display only the last exception instance that raises.


# we can also bypass some exceptions by jumping back to a specific exception instance in the 
# traceback by using `from exception_instance`:
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


# it is useful to hide exception stacks that are just implementation details.

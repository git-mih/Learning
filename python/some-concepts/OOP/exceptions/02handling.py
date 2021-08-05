# Handling exceptions in more details.

# in order to creates that propagation workflow, we have to raise an exception. and we can do
# it by using the `raise` keyword.

# we can do it by just using the exception class itself, and it will actually works:
# raise ValueError    # ValueError    it creates an instance of the ValueError exception for us.

# but typically, we create the exception instances ourselves and then we raise that:
# raise ValueError()  # ValueError

# and we can certainly pass arguments as well:
# raise ValueError('custom message')  # ValueError: custom message


# when we are executing a Python application for the command line and an exception is raised,
# if we dont have any handling around it, then Python propagates the exception all the way back. 
# whenever the exception propagation reaches the top, Python terminates the program and report 
# back the error in the stdout or the stderror. 

#____________________________________________________________________________________________________
# exceptions handling:
# in order to handle exceptions, we have to basicly interrupt this propagation workflow by
# using the try statement.

# the full try statement can have these clauses:
# try:
#     code that we want to protect from some potential exception. also called guarded code.
#     we want to keep this guarded code as short as possible. often is just a single statement.
#     we should really only guard code where we can do something about the exception. 

# except <ExceptionType> [as <symbol>]:
#     this is the code that will run if that specified <ExceptionType> exception is raised
#     inside the guarded code.

# finally:
#     is the piece of code that always executes, wheter exception occurred or not.

# else:
#     is the code that executes if the try terminates normally. if we dont get any 
#     exception raised in the guarded code, then the else executes.


# whenever we are guarding some code inside the try clause, we could handle different 
# exceptions types with separated exception handlers for each one:
def f1():
    raise ValueError('bad value')
# traping a Value error that is raised by f1:
try:
    f1()
except ValueError as ex:
    'handling a value error', repr(ex)  # handling a value error ValueError('bad value',)
except IndexError as ex:
    'handling an index error', repr(ex)

# but if f1 raises a index error we can catch it as well:
def f1():
    raise IndexError('bad value')
try:
    f1()
except ValueError as ex:
    'handling a value error', repr(ex)
except IndexError as ex:
    'handling an index error', repr(ex)  # handling an index error IndexError('bad value',)

# we are essentially stoping these exceptions propagation workflows that raised. 


# now, if f1 raises a exception that we doesnt expect, like a TypeError exception:
def f1():
    raise TypeError('bad type') 
try:
    # f1()
    # we are guarding f1 but we are only going to handle ValueError and IndexError exceptions.
    # anything else will keep being propagated because we are not handling it.
    pass
except ValueError as ex:
    'handling a value error', repr(ex)
except IndexError as ex:
    'handling an index error', repr(ex)

# in this case it will keeps propagating till Python terminates the program:
# TypeError: bad type


# while we are handling multiple exceptions types, what is really important is to always go 
# from the most specific to the least specific, in terms of class hierarchy:
try:
    [1, 2, 3][999]
except IndexError:
    'invalid index' # invalid index...
except LookupError:
    'lookup error'

# if we switch the handlers, the LookupError handler will catch the exception and handle that:
except LookupError:
    'lookup error'  # lookup error...
except IndexError: 
    # the IndexError exception workflow will never reach the IndexError handler now.
    'invalid index'


# we can group exception types in a single except clause and handle multiple exceptions together:
except (ValueError, TypeError) as exc:
    type(exc)  # tuple


# bare exception handlers:
# these are exception handlers that do not specify an exception type, they catch any exception.
except:
# we cant use the `as` here, so how do we get a reference to the actual exception instance?
# we can do that using the sys module. it has a function: sys.exc_info() that returns information
# about the current exception object that is propagating in this workflow.
# it will returns a tuple containing the 'exc_type, 'exc_value' and the 'exc_traceback'.
    pass

# usually we need to know what type of exception it is in order to do something about.
# its good in certain circunstances like, cleanup work, logging, re-raising exceptions.

#____________________________________________________________________________________________________
# exception objects:
# there is specific properties and methods that an exception object have, but it depends on 
# the exception type.

# but since all exceptions inherits from the BaseException, they at least have what the 
# BaseException provides.

# all standard exceptions have at least these two properties:
# args  - which are the arguments used to create the exception object instance. the ones who
#         get passed to the __init__ essentially. but very often is just the error message.

#         most standard exceptions constructors supports multiple arguments, like:
try:
    raise ValueError('custom message', 'secondary message')
except ValueError as ex:
    ex   # ('custom message', 'secondary message')

# __traceback__  - that is the traceback object. it is a object which gives us an ideia of the
#                  stack trace, where the exception occurred and how it get propagated.
#                  the traceback object is the last element of the tuple that is returned by 
#                  sys.exc_info().

#____________________________________________________________________________________________________
# try and finally:
# the finally clause is guaranteed to run. either an exception has occurred or not.
# we could actually do this:
try:
    pass 
# we dont have except clauses. the exceptions wont be handled. so it will get propagated up.
finally:
# but before the propagation workflow occurs, the finally block is going to execute.
    pass

#____________________________________________________________________________________________________
# what happens if an exception handler itself raises an exception? no problem.
# it will works normally. if the exception isnt handled, it will propagate up in the chain 
# as normal.


# exception handling can be also nested inside an except handler, not just inside the 
# try clause. we can use nesting anywhere, inside the finally clause, the else, doesnt matter.

# suppose that we want to creates a list of Person objects from a deserialized json object:
import json

payload = """{
    "Alex": {"age": 18},
    "Bryan": {"age": 21, "city": "London"},
    "Guido": {"age": "unknown"}
}"""

# deserializing json object into a regular dictionary:
data = json.loads(payload)
# {'Alex': {'age': 18}, 
#  'Bryan': {'age': 21, 'city': 'London'}, 
#  'Guido': {'age': 'unknown'}}

class Person:
    __slots__ = 'name', '_age'

    def __init__(self, name):
        self.name = name
        self._age = None

    @property
    def age(self):
        return self._age
    
    @age.setter
    def age(self, value):
        # age must be an integer greater than 0, otherwise: invalid age
        if isinstance(value, int) and value >= 0:
            self._age = value
        else:
            raise ValueError('invalid age')
        
    def __repr__(self):
        return f'Person(name={self.name}, age={self._age})'

persons = []

for name, attribute in data.items():
    try:
        p = Person(name)  # p = Person('Alex')

        for attrib_name, attrib_value in attribute.items():
            try:
                setattr(p, attrib_name, attrib_value)  # Alex.age = 18
        # at this point, if we got an ValueError exception raised, it will get propagated back,
        # because the inner try statement doesnt know how to handle it.
            except AttributeError:
                print(f'ignoring attribute: {name}.{attrib_name}={attrib_value}')
    # the ValueError exception will get propagated back to the outer try statement. the outer
    # try statement do have a ValueError exception handler:
    except ValueError as exc:
        print(f'Data for Person({name}) contains invalid attribute value: {exc}')
    else:
# this is going to run as long the outer try clause doesnt raise a exception. 
# The fact that we had an AttributeError raised inside the inner try statement doesnt matter, 
# cause that exception is being silenced by the inner try statement, and the outer try doesnt 
# know about that. its really important to understand it.
        persons.append(p)

# output:
# ignoring attribute: Bryan.city=London
# Data for Person(Guido) contains invalid attribute value: invalid age

persons  # [Person(name=Alex, age=18), Person(name=Bryan, age=21)]

#____________________________________________________________________________________________________
# handling exceptions vs avoiding exceptions:
# this is more about how do we work with exceptions in our code.

# "it's easier to ask forgiveness than it is to get permission"  by Grace Hopper.

# this principle is sometimes referred to as the EAFP in Python. and that is very tipical.

# and this is the Pythonic way of doing it. this is basicly: "lets ask for forgiveness later".
# we try to do something and if doesnt work, then we handle it (ask forgiveness).

# there two ways to look at exceptions in our code.

# we can try to do something and then catch the exception, like:
def get_item_forgiveness(seq, idx, default=None):
    try:
        return seq[idx]
    # as long the seq object type supports the `[]` and a valid idx value, it will works.
    except (IndexError, TypeError, KeyError) as ex:
        return default
    # if the seq object we passed in doesnt support it, we just return the default value.

get_item_forgiveness([1, 2, 3], 0)    # 1
get_item_forgiveness([1, 2, 3], 7, 'Nope!') # Nope!

get_item_forgiveness({'a': 100}, 'a')  # 100
get_item_forgiveness({'a': 100}, 'zz', 'Nope!')  # Nope!

def get_item_permission(seq, idx, default=None):
    # asking permission before we can run our code basicly:
    if hasattr(seq, '__getitem__'):
        if idx < len(seq):
            return seq[idx]
        # if the seq object does support the sequence protocol, then it returns that element.
    return default
    # otherewise, it returns the default.

get_item_permission([1, 2, 3], 0) # 1
get_item_permission([1, 2, 3], 7, 'Nope!') # Nope!

# get_item_permission({'a': 100}, 'a')  
#      TypeError: '<' not supported between instances of 'str' and 'int'

# in this case we tried to avoid exceptions by checking conditions even before it start doing 
# something. this doesnt even begin to address all the potential problems. like, all things 
# could go wrong while we are doing something after the condition. and in this case, we would 
# have to write more and more check conditions in order to prevent new exceptions to raise.

# in general we should not try to catch the exceptions before they even occur. in Python we 
# should try to do something, and if doesnt work, then we handle that exception.


# that is the hole thing about Python, we are not really interested in the type of some
# particular object, we are more interested in "does this particular object supports an 
# specific set of functionalities?" 

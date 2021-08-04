# Python Exceptions

#_________________________________________________________________________________________________
# what are exceptions?
# exceptions are actually objects. they are object instances of some class.

# when an exception is raised, it trigger a special kind of execution that called 
# propagation workflow.

# the propagation workflow of the exceptions can be triggered by Python if something went bad, 
# like providing an invalid index value of a list:
l = [1, 2, 3]
# l[99]  
# -----------------------------------------------
# Traceback (most recent call last):
#   File "exceptions\01.py", line 21, in <module>
#     l[99]
# IndexError: list index out of range

# this is the result of the exception propagation workflow. what is happening essentially  
# is that, we did not handled the exception. 

#_________________________________________________________________________________________________
# we can basicly intercept the propagation workflow by doing what we call, exception handling.
# we require to use the try clause to handle exceptions: 
l = [1, 2, 3]            # try is a compound statement with except/finally/else.
try:
    l[99]
except IndexError as exc:
# we can get a reference to the exception instance inside the except clause by using `as`.
# it gives us a reference to the actual object instance of the exception that raised.

# now we have access to that exception instance inside the variable 'exc' that we assigned to:
    print(exc.__class__, ':', exc)  # <class 'IndexError'> : list index out of range


# the except clause has interrupted the propagation workflow of that specific exception.

# since we dont have an exception inside the except block itself, at that point we handled 
# the exception and stoped the propagation workflow. the program keeps running normally.

#_________________________________________________________________________________________________
# there is a difference between just creating an object instance of some exception and have
# an exception raised.

# when we raise an exception, we are actually creating an propagation workflow where we should
# try to handle that exception or just let it propagate.

# we can create any exception instance and that doesnt trigger the exception propagation workflow:
exc = Exception()  
type(exc)  # <class 'Exception'>

#_________________________________________________________________________________________________
# call stack:
# suppose we are inside our main module, then we call f1 and f1 calls f2, f2 calls f3:
#                           ->|___f3___|
#              ->|___f2___|   |___f2___|
# ->|___f1___|   |___f1___|   |___f1___|
#   |<module>|   |<module>|   |<module>|

def f1():
    f2()

def f2():
    f3()

def f3():
    exc = ValueError()
    raise exc

# the exception propagation workflow:
#          ┌--> exception raised in f3. if the exception is not handled, execution of f3 stops at
#   |___f3___|  that point. then it propagates back to f2 try to handle.
#   |___f2___|  
#   |___f1___|
#   |<module>|
#          ┌--> f2 try to handle that exception, if it cant, it stops its execution and 
#   |___f2___|  propagates the exception back to f1 handle.
#   |___f1___|
#   |<module>|
#          ┌--> f1 is in our main module, so if we dont handle the exception here, then the 
#   |___f1___|  program terminates.
#   |<module>|

# there is a maintained stack trace that keeps track of what is happening in this propagation
# workflow. it help us to document the origin of the exception and every call in the stack.

#_________________________________________________________________________________________________
# what are exceptions used for?
# they are not necessarily errors. it just indicates some sort of anomalous behavior and 
# sometimes is not even anomalous, its just used for control flow of the program, basicly used
# to send signal like "something happened, we should handle it". 
# great exemple is the StopIteration exception that is raised by iterators.


# exceptions are not necessarily fatal, they do not necessarily need to result in the program 
# termination. if we dont handle then, sure they will terminate. but we can actually handle the
# exceptions as they occur during the propagation workflow.

# it means that we can do something and then let the program continue running normally.

# or we can trap the exception, do something that correct that exception if we can, and then 
# let the program continue running.

# or we can maybe do something and let the original exception propagates again.

# or we can interrupt that propagation workflow and maybe raise a different exception.

#_________________________________________________________________________________________________
# Python exception hierarchy:
# Python's builtin exception classes use inheritance to form a class hierarchy. so, there is
# a base exception for every exception in Python, including custom exceptions that will also
# need to inherit from one of the exceptions classes in Python. 
# there is 4 main 

# BaseException
#     +--- SystemExit        (raised on sys.exit())
#     +--- KeyboardInterrupt (raised on Ctrl+C)
#     +--- GeneratorExit     (raised when generator or coroutines get closed)
#     +--- Exception         (everything else inherit from this class)

isinstance(Exception(), BaseException)  # True

# most of the time, any exception that we work with inherits from Exception. 
# some of the direct subclasses of the Exception include:
# ArithmeticError
#     +--- FloatingPointError
#     +--- ZeroDivisionError
# AttributeError
# LookupError
#     +--- IndexError
#     +--- KeyError
# RuntimeError
# SyntaxError
# TypeError
# ValueError    and more...

issubclass(IndexError, LookupError) # True
issubclass(IndexError, Exception)   # True

# exceptions are just object instance of these classes essentially.


# when exceptions inherit from other exceptions, it is useful cause, for exemple, if we catch
# a LookupError exception, it will also catch an IndexError exception. it happens because
# IndexError is a subclass of LookupError:
l = [1, 2, 3]
try:
    l[99]
except LookupError as ex:
    print(ex.__class__, ':', ex)  # <class 'IndexError'>: list index out of range


# so if we catch an Exception exception, it will also catch any subclass of Exception. 
# we call it a broad catch. 

# but we should avoid these broad exception handlers because we dont know exactly what to do 
# if an specific exception raise:
try:
    l[99]
except Exception as ex:
# we cant know what exception may raise. we really cant handle without knowing.
    pass

# we do have useful cases of using broad exception handlers. but in general, its just a lazy 
# way of traping exceptions. 


# we could even go broad and trap the BaseExceptions exception or we could also do what we 
# call, bare exception handler, where we use a "naked" except clause:
try:
    l[99]
except:
    print('exception occurred')  # exception occurred

# in general, we dont use these broad exception handlers.

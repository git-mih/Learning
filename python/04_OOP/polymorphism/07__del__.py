# Class finalizer: __del__

# the garbage collector destroys objects that are no longer referenced anywhere.
# we use the __del__ method to hook into this lifecycle event. the __del__ method
# will get called right before the object is destroyed by the GC.

# so the GC determines when this __del__ method is called. we dont control when this
# __del__ method will gets called.

# what the __del__ method do, is just executes a little bit of code before the object
# gets destroyed by the GC.

# but when does __del__ get called? we dont control when, that is the basic issue
# with __del__ method. it will only get called when all references to the object
# are gone.

# but we have to be extremely careful with our code inside __del__, cause is easy to
# inadvertently creates additional references or circular references and the object
# not get destroyed anymore.

# additional issues:
# if __del__ contains references to global variables or other objects, those objects
# may be gone by the time __del__ is called. like, if an exception occurs in the
# __del__ method, the exception isnt raised. it will be silenced by Python.
# the exception will be sent to stderr but the main program will not be aware that
# something went wrong during that finalization.

# NOTE: we should always prefer using context managers to clean up resources.

import ctypes
def ref_count(address):
	return ctypes.c_long.from_address(address).value


class Person:
	def __init__(self, name):
		self.name = name

	def __repr__(self):
		return f'Person({self.name})'

	def __del__(self):
		print(f'__del__ called for {self}')

p = Person('Fabio')
# p is referencing the Person('Fabio') object

ref_count(id(p))   # 1

# lets remove this reference now:
del p  # ref_count(id(p))   # 0
# at this point, the reference count for the object Person('Fabio') will be 0
# and right before the GC destroy the object itself, it will call the __del__ method.

# __del__ called for Person('Fabio')


#_______________________________________________________________________________________
# capturing a 'hidden' reference
class Person:
	def __init__(self, name):
		self.name = name

	def __repr__(self):
		return f'Person({self.name})'

	def __del__(self):
		print(f'__del__ called for {self}')

	def gen_ex(self):
		raise ValueError('something went bad...')

p = Person('Fabio')
ref_count(id(p))    # 1

try:
	# raising the ValueError through gen_ex
	p.gen_ex()  
except ValueError as ex:
	print(ex)

# we could display the exception but we dont have a pointer to it. it means that,
# we no longer have that exception after the exception is finished running.

# ex           # NameError: name 'ex' is not defined

# a simple way of solving it, is storing the exception object into a symbol like:
try:
	p.gen_ex()  
except ValueError as ex:
	error = ex # type(error)  # <class 'ValueError'>
	print(ex)

# we now have the reference to the ValueError exception object.
error          # something went bad...


# now lets look at the reference count of the Person('Fabio') object.
ref_count(id(p))  # 2

# why? well, the ValueError object (error) has another reference to the 
# Person('Fabio') object. 

# in particular it get stored inside the traceback of the exception.
dir(error)   # [..., '__traceback__']
dir(error.__traceback__)    # ['tb_frame', 'tb_lasti', 'tb_lineno', 'tb_next']
dir(error.__traceback__.tb_frame)    # [..., 'f_locals']
type(error.__traceback__.tb_frame.f_locals)  # dict


# for key, value in error.__traceback__.tb_frame.f_locals.items(): ...
#   we may get RuntimeErro: dictionary changed size during iteration.

# to prevent that, we can create a static copy of this dictionary and iterate over it
for key, value in error.__traceback__.tb_frame.f_locals.copy().items():
	# there is a bunch of stuffs, but we can see that it has a reference to 'p'
	# p = Person('Fabio') inside this dict.
	# so we can conclude there is references to that object in this stack trace.
	if isinstance(value, Person):
		print(key, value)     # p Person(Fabio)

ref_count(id(p))  # 2
# we have a reference to the Person('Fabio') object in the variable 'p' itself and
# we also have an reference to that object inside the ValueError (error) object.

# so even if we delete the reference 'p':
del p

# we still have reference to the Person('Fabio') object.
ref_count(id(Person('Fabio')))  # 1

# we should also delete the ValueError object (error) so the reference count of our
# object gets to 0 and then calls the __del__ method. but what if we have another
# hidden reference pointing to Person('Fabio') object? the __del__ will never gets
# called unless the program finish. we dont have control by using __del__, it depends
# on GC.


#_______________________________________________________________________________________
class Person:
	def __del__(self):
		raise ValueError('Something went bad...')

p = Person()
del p
# reference count of Person() object is 0 right now, the __del__ is called but Python
# will silence the exception for us and keep running the program.

# NOTE: the exception will be sent to the stderr output.

import sys
sys.stderr # <_io.TextIOWrapper name='<stderr>' mode='w' encoding='utf-8'>

# lets redirect the stderr to a file instead.
class ErrorToFile:
	def __init__(self, fname):
		self._fname = fname
		self._current_stderr = sys.stderr
	
	def __enter__(self):
		self._file = open(self._fname, 'w')
		sys.stderr = self._file

	def __exit__(self, exc_type, exc_value, exc_tb):
		sys.stderr = self._current_stderr
		if self._file:
			self._file.close()
		return False

p = Person()
with ErrorToFile('error.txt'):
	del p     # exception will be writed and sent to the 'error.txt' file.
	print(1)  # 1
	print(2)  # 2
	print(3)  # 3

# reading the exception:
with open('error.txt') as f:
	f.read()

# Exception ignored in: <function Person.__del__ at 0x000001C61ECC9DC0>
# Traceback (most recent call last):
#   File "C:\OOP\polymorphism\07__del__.py", line 141, in __del__
#     raise ValueError('Something went bad...')
# ValueError: Something went bad...


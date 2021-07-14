# Callables

# any object instance can be made to emulate a callable by implementing
# the __call__ method.

class Person:
	def __call__(self, name):
		return f'hello {name}'

p = Person()
callable(p)          # True

p.__call__('fabio')  # hello fabio

# shorthand by using parentesis:
p('Fabio')           # hello fabio


# it is useful for creating function-like objects that need to maybe maintain state,
# or maybe implementing other functionalities. 
# it is also useful for creating decorators classes. where classes can be used as
# decorators.
#____________________________________________________________________________________
class Person:
	def __call__(self):
		return '__call__ called...'

p = Person()
callable(p) # True
p()         # __call__ called...

# in Python in general we talk about callables without necessary talk about functions.
# because other things than functions are also callables, like: methods, classes and 
# in this case, a Person object instance is a callable as well.


# this is widely used. making object instances of classes that are callable happens
# in a lot of places and we dont necessary realize it. we think about these things 
# as functions where often they are not functions, just another type of callable.

# for exemple, we have the partial function in functools. 
# well, that is not actually a function.
from functools import partial

type(partial)   # <class 'type'>

# partial is actually a callable class and not a function. the partial class creates
# callable instances by implementing the __call__. 

# defining a actual function:
def f(a, b, c):
	return a, b, c

type(f)  # <class 'function'>

# we are going to call the 'f' function indirectly through the partial object instance
partial_f = partial(f, 10, 20)
type(partial_f)      # <class 'functools.partial'>
callable(partial_f)  # True

# partial_f is now an callable object instance of the partial class, and a callable.
partial_f(30)    # (10, 20, 30)

#________________________________________________________________________________________
def f(a, b, c):
	return a, b, c

# making our own partial 'function' implementation:
class Partial:
	def __init__(self, fn, *args):
		self._fn = fn
		self._args = args

	def __call__(self, *args):
		return self._fn(*self._args, *args)

partial_f = Partial(f, 10, 20)

type(partial_f)     # <class '__main__.Partial'> object instance of Partial object
callable(partial_f) # True 

partial_f(30)       # (10, 20, 30)

#________________________________________________________________________________________
# implementing a dictionary that will be used for caching.
# it will keep tracking of the number of times someone requested an item for this 
# cache dictionary that doesnt exist.
from collections import defaultdict

# quick review of default dict:
d = defaultdict(lambda: 'N/A') 
# everytime we try to access a key from 'd' and it doesnt exist, it calls the function
# and put that key in the defaultdict dictionary.
d['a']    # N/A

# but if the key exists it returns the value back:
d['b'] = 100
d['b']    # 100

d.items() # dict_items([('a', 'N/A'), ('b', 100)])


# now lets use it to keep track the number of times it has been called. it will tell
# us how many times a non-existing key was called.

# first, the defaultdict needs a callable to call, so we need to pass a callable to 
# the constructor. lets create a class and implement the __call__ method and then
# pass the object instance of this class to the defaultdict calls whenever requested
# an non-existing key:
class DefaultValue:
	def __init__(self):
		self.counter = 0

	def __iadd__(self, other):
		if isinstance(other, int):
			self.counter += other
			return self
		raise ValueError('can only increment with an integer value')

	def __call__(self):
		self.counter += 1
		return 'N/A'

default1 = DefaultValue() # callable(default1)  # True
default2 = DefaultValue() # callable(default2)  # True

default1.counter     # 0

# now lets create the defaultdict dictionaries to store the cache:
cache_1 = defaultdict(default1)
cache_2 = defaultdict(default2)

cache_1['a']  # N/A
cache_1['b']  # N/A

default1.counter     # 2
default2.counter     # 0   independent of the counter of default1 object instance.

#________________________________________________________________________________________
# often we use closures to create decorators, but sometimes its easier to use 
# a class instead.

# simple profiler function:
# we gonna keep tracking of how many times a function gets called and
# how long that function takes to run on average.

from time import perf_counter, sleep
from functools import wraps

# class approach:
class Profiler:
	def __init__(self, fn):
		self.counter = 0
		self.total_elapsed = 0
		self.fn = fn

	def __call__(self, *args, **kwargs):
		self.counter += 1
		start = perf_counter()
		result = self.fn(*args, **kwargs)
		end = perf_counter()
		self.total_elapsed += (end - start)

	@property
	def avg_time(self):
		return self.total_elapsed / self.counter

@Profiler
def f(a, b):
	sleep(1)
	return a, b

# 'f' now an object instance of the Profiler class, and it is also a callable object
type(f)       # <class '__main__.Profiler'>
callable(f)   # True

# additional attributes now:
f.counter     # 0
f.fn          # <function f at 0x0000021D2776D3A0> (original 'f' function)


f(10, 20)     # (10, 20)
# Python is essentially calling the __call__:  f.__call__(10, 20) 

f.counter       # 1
f.total_elapsed # 1.0107968

f(30, 40)
f.counter       

#_________________________________________________________________________________________
# closure approach:
def profiler(fn):
	_counter = 0
	_total_elapsed = 0
	_avg_time = 0

	@wraps(fn)
	def inner(*args, **kwargs):
		nonlocal _counter
		nonlocal _total_elapsed
		nonlocal _avg_time
		_counter += 1
		start = perf_counter()
		result = fn(*args, **kwargs)
		end = perf_counter()
		_total_elapsed += (end - start)
		_avg_time = _total_elapsed / _counter
		return result

	def counter():
		return _counter

	def avg_time():
		return _avg_time
	
	# attributes inside the inner function, these attributes will point to these
	# functions which will return the current value of _counter.
	inner.counter = counter
	inner.avg_time = avg_time
# it will be inserted inside the inner function namespace before we return the inner function
# inner.__dict__   # {'counter': <function at 0x01>, 'avg_time': <function at 0x02>}
	return inner

@profiler
def f():
	sleep(1)

type(f)   # <class 'function'>

f()
f()

f.counter()  # 2
f.avg_time() # 1.0020038
#________________________________________________________________________________________

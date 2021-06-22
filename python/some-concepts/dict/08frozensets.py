# Fronzensets are immutable sets
fs = frozenset({1, 2, 3})     # hash(fs) -272375401224217160

# argument to frozenset must be any hashable iterable object
fs = frozenset(range(4))      # frozenset({0, 1, 2, 3})
fs = frozenset([1, 2, 3])     # frozenset({1, 2, 3})
fs = frozenset('python')      # frozenset({'h', 'n', 'o', 'p', 'y', 't'})

# frozenset(([1, 2], [3, 4]))   TypeError: unhashable type
# frozenset(5)                  TypeError: 'int' isnt a iterable

# fronzensets are hashable objects.
# we can use it as dict keys or set elements
s = {frozenset({1, 2, 3}), frozenset('fa')}  # type(s)  set

# frozensets only makes shallow copies
fs1 = frozenset([1, 2])       # fs1 = frozenset({1, 2})
fs2 = fs1.copy()			  # fs2 = frozenset({1, 2})

# fs1 is fs2     True, both points to the same object
# fs1 == fs2     True, both shares the same objects. they're immutable, it is safe.

# non-mutate operations works with frozensets, such as: |, &, - and ^
s1 = frozenset('abc')
s2 = {1, 2}

# data type will be defined by the left most element of the operation.
s3 = s1 | s2     # s3 = frozenset({'b', 'c', 1, 2, 'a'})
s4 = s2 | s1     # s4 = {'a', 1, 2, 'c', 'b'}

#_____________________________________________________________________________
def memoizer(fn):
	cache = {}
	def wrapper(*args, **kwargs):                # this aproach, order of args would not matter
		key = (*args, frozenset(kwargs.items())) # frozenset(args) | frozenset(kwargs.items())
		print(cache)
		print(key)
		if key in cache:
			return cache[key]
		else:
			result = fn(*args, **kwargs)
			cache[key] = result
			return result
	return wrapper

@memoizer
def f(*, a, b):
	return a + b

f(a=1, b=2)
# cache: {}            kwargs.items() 
# key:  (frozenset({('a', 1), ('b', 2)}),)

f(a=4, b=5) #       key                       v
# cache: {(frozenset({('a', 1), ('b', 2)}),): 3} 
# key:  (frozenset({('b', 5), ('a', 4)}),)

# cache: {(frozenset({('a', 1), ('b', 2)}),): 3, (frozenset({('b', 5), ('a', 4)}),): 9}

# f(a=1, b=2) or f(a=4, b=5) 
# these values is already stored in cache, it just returns and dont calculate it again

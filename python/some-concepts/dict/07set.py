#							BASICS
s = {'a', 100, (1, 2, 3)} # set
s = set() 				  # empty set
s = {'fafafafa'}          # {'f', 'a'} no duplicates

# the set() constructor can accept any iterable
s = set([1, 2, 3])        # {1, 2, 3}
s = set('python')         # {'o', 'n', 'y', 'p', 't', 'h'}
s = set(range(4))     	  # {0, 1, 2, 3}
s = set({'a': 1, 'b': 2}) # {'a', 'b'}  iterate over the keys only

# but the iterable itself should not contain unhashable element
# s = set([[1, 2, 3]])    TypeError: unhashable element 'list'

# set comprehension
s = {c for c in 'python'} # {'o', 'n', 'y', 'p', 't', 'h'}

# unpacking (no duplicates and no order)
s1 = {'a', 'b', 'c'}
s2 = {'b', 'c', 'd'}
s = {*s1, *s2}            # {'b', 'd', 'a', 'c'}

#______________________________________________________________________
#						COMMOM OPERATIONS

# membership operations using hash tables are much faster than list/tuples.
# but this speed comes with cost of memory.
s = {i for i in range(10_000)}       # s.__sizeof__()   524488 
d = {i: None for i in range(10_000)} # d.__sizeof__()   294984
l = [i for i in range(10_000)]       # l.__sizeof__()   85160

# even empty set/dict require more memory allocation
s = set()                            # s.__sizeof__()   200 
d = dict()                           # d.__sizeof__()   216
l = list()                           # l.__sizeof__()   40

# set/dict over allocate memory space to try to avoid collisions.
# trying to add a few references to set/dict will not change size till it get full
s.add(10)							 # s.__sizeof__()   200
d['a'] = 10                          # d.__sizeof__()   216
l.append(10)                         # l.__sizeof__()   72

# just references of the objects itself get stored in the hash table

# All these operations are mutating the set object
s = {'a', 'b', 'c'}
# s.add('x')      {'x', 'a', 'b', 'c'}
# s.remove('b')   {'x', 'a', 'c'}
# s.remove('f')   KeyError
# s.discard('f')  no error msg if element isnt avaiable
# s.discard('a')  {'x', 'c'}

s = {'python'}
# s.pop()         't'    remove and returns a random element
# s.clear()       {}

#______________________________________________________________________
#						SET OPERATIONS
# NOTE: None of these operations bellow mutates the object.

s1 = {1, 2, 3}
s2 = {2, 3, 4}
# s1.intersection(s2)  {2, 3}
# s1 & s2              {2, 3}

s1 = {1, 2, 3}
s2 = {2, 3, 4}
# s1.union(s2)         {1, 2, 3, 4}
# s1 | s2			   {1, 2, 3, 4}

s1 = {1, 2, 3, 4, 5}
s2 = {4, 5}
# s1.difference(s2)    {1, 2, 3}
# s1 - s2              {1, 2, 3}

s1 = {1, 2, 3, 4, 5}
s2 = {4, 5, 6, 7, 8}
# s1.symmetric_difference(s2)  {1, 2, 3, 6, 7, 8}  (union - difference)
# s1 ^ s2 (XOR)                {1, 2, 3, 6, 7, 8}

s1 = {1, 2, 3}
s2 = {2, 3, 4}
s3 = {30, 40, 50}
# s1.isdisjoint(s2)  False   they share {2, 3}
# s1.isdisjoint(s3)  True    they dont share any element

s1 = {1, 2, 3}
s2 = {1, 2, 3}
s3 = {1, 2, 3, 4}
s4 = {10, 20, 30}
# s1.issubset(s2)    True 
# s1 <= s2           True
# s1 < s2 			 False

# s1.issuperset(s1)  True
# s3 > s1            True

# by using these operators, we cant perform operations in non-set data types
s1 = {1, 2}
# s1 & [2, 3]        TypeError
# {1, 2} & [2, 3]    TypeError

# but using method based, we can use any iterable.
s1 = {1, 2}
# s1.intersection([2, 3])      {2}
# 	we can think it is being converted like set() does. its like we're doing set([2, 3])
# s1.intersection(range(10))   {2}

# s1.intersection([[1, 2], [3, 4]])   TypeError: unhashable type

# OBS: 
# list/tuples doesnt have these methods. But we could type cast a list to perform it
l1 = [1, 2, 3]
l2 = [2, 3, 4]
# set(l1).intersection(l2)     {2, 3}  Dope.

#______________________________________________________________________
#						UPDATE OPERATIONS
# it doesnt mutate s1 object. it just changed the obj which s1 was pointing to
s1 = {1, 2, 3}   # id(s1) 0x0001
s2 = {2, 3, 4}

s1 = s1 | s2     # id(s1) 0x0008    s1 = {1, 2, 3, 4}

# union in place mutation
s1.update(s2)    # id(s1) 0x0001    s1 = {1, 2, 3, 4}  or
s1 |= s2         # id(s1) 0x0001    s1 = {1, 2, 3, 4} 

# intersection in place mutation
s1 = {1, 2, 3}   
s2 = {2, 3, 4}

s1.intersection_update(s2)  # {2, 3}
s1 &= s2                    # {2, 3}

# difference in place mutation
s1 = {1, 2, 3, 4}   
s2 = {2, 3}
s3 = {3, 4}

s1.difference_update(s2)     # {1, 4}
s1 -= s2                     # {1, 4}
s1.difference_update(s2, s3) # {1, 3, 4}
s1 -= (s2 - s3)              # {1, 3, 4}

# simmetric difference in place mutation
s1 = {1, 2, 3, 4, 5}   
s2 = {4, 5, 6, 7}

s1.symmetric_difference_update(s2) 
s1 ^= s2               # {1, 2, 3, 6, 7}

# NOTE: methods are more flexibles than operators. by using method based
# we can pass any iterable to the method argument. and with the operators,
# we require to use only set's
s1 = {1, 2}
s1.update([3, 4], (5, 6, 7), 'py') # {1, 2, 3, 4, 5, 6, 7, 'y', 'p'}

# we could use operators, but we need to typecast them
s1 = {1, 2}
s1 |= set([3, 4]) | set((5, 6, 7)) | set('py')


#______________________________________________________________________
def combine(string, target):
	target.update(string.split(' ')) # ['lumberjacks', 'sleep', 'all', 'night'], ...

def cleanup(combined):
	words = {'the', 'and', 'a', 'or', 'is', 'of'}
	combined -= words # filtering these words from result

result = set()
combine('lumberjacks sleep all night', result)
# result = {'all', 'sleep', 'lumberjacks', 'night'}
combine('the ministry of silly walks', result)
# result = 
# {'the', 'walks', 'of', 'night', 'silly', 'sleep', 'all', 'ministry', 'lumberjacks'}
combine('this parrot is a late parrot', result)
# result = 
# {'late', 'the', 'walks', 'of', 'this', 'night', 'silly', 'sleep', 'parrot', 'a', 'all', 'ministry', 'lumberjacks', 'is'}
cleanup(result)
# result = 
# {'night', 'all', 'ministry', 'lumberjacks', 'sleep', 'walks', 'this', 'parrot', 'late', 'silly'

#______________________________________________________________________
#							COPYING SETS

class Person:
	def __init__(self, name):
		self.name = name

	def __repr__(self):
		return f'Person(name={self.name})'

p1 = Person('jhon')
p2 = Person('eric')

# SHALLOW COPY
s1 = {p1, p2}   # s1 = {Person(name=jhon), Person(name=eric)}

# copy() method
s2 = s1.copy()  # s2 = {Person(name=jhon), Person(name=eric)}
# s1 is s2      False, different containers sharing the same objects.

# s1 == s2      True, they have the same objects
# p1 in s1      True
# p1 in s2      True

# unpacking
s3 = {*s1} 	    # s3 = {Person(name=jhon), Person(name=eric)}
# s1 == s3      True, they have the same objects

# set() constructor
s4 = set(s1)    # s4 = {Person(name=jhon), Person(name=eric)}
# s1 == s4      True, they have the same objects

p1.name = 'beth'
# mutating the object is going to mutate all of them
# s1 = {Person(name=beth), Person(name=eric)}
# s2 = {Person(name=beth), Person(name=eric)}
# s3 = {Person(name=beth), Person(name=eric)}
# s4 = {Person(name=beth), Person(name=eric)}


# DEEPCOPY
from copy import deepcopy

s5 = deepcopy(s1) # s5 = {Person(name=beth), Person(name=eric)}

# s1 is s5       False, different containers
# s1 == s5       False, not sharing the same objects anymore

p1.name = 'fabi'
# s1 = {Person(name=fab), Person(name=eric)}
# s2 = {Person(name=fab), Person(name=eric)}
# s3 = {Person(name=fab), Person(name=eric)}
# s4 = {Person(name=fab), Person(name=eric)}
# s5 = {Person(name=beth), Person(name=eric)} 
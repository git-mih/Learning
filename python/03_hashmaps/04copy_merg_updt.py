#	 		 			 UPDATING/MERGING

# manual update (in place)
d = {'a': 1, 'b': 2, 'c': 3}
d['b'] = 100 

# update by merging another dict (in place)
d1 = {'a': 1, 'b': 2}
d2 = {'c': 3, 'd': 4}
d1.update(d2) 
# d1 = {'a': 1, 'b': 2, 'c': 2, 'd': 3}

# update by using keyword argument (in place)
d1 = {'a': 1, 'b': 2}
d1.update(b=20, x=40, c=30) 
# d1 = {'a': 1, 'b': 20, 'x': 40, 'c': 30}

# update by using iterable of iterables, any type.(in place)
d1 = {'a': 1, 'b': 2}
d1.update([('c', 2), ['d', 3]]) # [ ('key1', value1), ['key2', value2] ]
# d1 = {'a': 1, 'b': 2, 'c': 2, 'd': 3}

# even using generator expressions
d1 = {'a': 1, 'b': 2}
d1.update((k, ord(k)) for k in 'cde') # ('c', 99) || ('d', 100) || ('e', 101)
# d1 = {'a': 1, 'b': 2, 'c': 99, 'd': 100, 'e': 101}

# update by unpacking (new instance)
d1 = {'a': 1, 'b': 2}
d2 = {'b': 20, 'c': 3}
d3 = {'c': 30, 'd': 4}

d = {**d1, **d2, **d3} # we can chain multiple dicts, 
					   # the last instance will always update the previous.
# d = {'a': 1, 'b': 20, 'c': 30, 'd': 4}

# we can unpack dict to send data to functions which expect keyword arguments only 
d = {'kw1': 10, 'kw2': 20}  
def f(*, kw1, kw2): # the keys must match keyword arguments name.
	print(kw1, kw2)
# f(**d)   10 20

def f(**kwargs): # {'a': 10, 'b': 20, 'c': 30}
	print(kwargs)
	for k, v in kwargs.items():
		print(k, v)
# f(a=10, b=20, c=30)   a 10 || b 20 || c 30

#_________________________________________________________________________
# 						 SHALLOW COPIES 

# copy() method
d1 = {'a': [1, 2], 'b': [3, 4]}
d2 = d1.copy()
# d1 is d2            False   different containers
# d1['a'] is d2['a']  True    sharing the same object 

# d1['a'].append(777)
# d1 = {'a': [1, 2, 777], 'b': [3, 4]}
# d2 = {'a': [1, 2, 777], 'b': [3, 4]}

# del d1['a']
# d1 = {'b': [3, 4]}
# d2 = {'a': [1, 2, 777], 'b': [3, 4]} doesnt affect

# dict() constructor
d1 = {'a': [1, 2], 'b': [3, 4]}
d2 = dict(d1)
# d1 is d2            False   different containers
# d1['a'] is d2['a']  True    sharing the same object 

# unpacking concept
d1 = {'a': [1, 2], 'b': [3, 4]}
d2 = {**d1, 'c': 5} 
# d1 is d2            False   different containers
# d1['a'] is d2['a']  True    sharing the same object 

# dict comprehension
d1 = {'a': [1, 2], 'b': [3, 4]}
d2 = {k: v for k, v in d1.items()}
# d1 is d2            False   different containers
# d1['a'] is d2['a']  True    sharing the same object 


#_________________________________________________________________________
# 						 DEEPCOPY
from copy import deepcopy

d1 = {'a': [1, 2], 'b': [3, 4]}
d2 = deepcopy(d1)
# d1 is d2            False   different containers
# d1['a'] is d2['a']  False   no longer share the same object 

# d1['a'].append(777)
# d1 = {'a': [1, 2, 777], 'b': [3, 4]}
# d2 = {'a': [1, 2], 'b': [3, 4]}
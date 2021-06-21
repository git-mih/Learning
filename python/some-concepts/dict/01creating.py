a = {'k1': 100, 'k2': 200} # literals

key = hash((1,2,3)) # tuple is hashable, so we can use it as a key
d = {key: 'python'} # d = {(1,2,3): 'tuple'}

t1 = (1, 2, 3) # hash 123456
t2 = (1, 2, 3) # hash 123456 also

# hash(t1) == hash(t2)  ->  True
# t1 == t2              ->  True
# t1 is t2              ->  False. they are not the same object

#_____________________________________________________________________
def fn_add(a, b):
	return a + b

def fn_mult(a, b):
	return a * b

def fn_inv(a):
	return 1 / a

funcs = {fn_add: (10, 20), fn_mult: (2, 8), fn_inv: (2,)}

print('\nusing fn.items() views:')
for fn, args in funcs.items():
	result = fn(*args) # add(10, 20) || mult(2, 8) || inv(2,)
	print(result)

#_____________________________________________________________________
d = dict(a=1, b=2)
l = [('a', 1), ('b', 2)] # l[0] = ('a', 1) || l[1] = ('b', 2)
d = dict(l) # {'a': 1, 'b': 2}

#_____________________________________________________________________
d1 = {'a': 10, 'b': 20}
d2 = dict(d1) # d2 isnt d1. but, its a Shallow copy

d1 = {'a': [1, 2], 'b': 3}
d2 = dict(d1) # d1['a'] is d2['a'] --> True

# d1['a'][1] = 1000 
# d1 -> {'a': [1, 1000], 'b': 3}
# d2 -> {'a': [1, 1000], 'b': 3}

# d2['a'].append(777)
# d1 -> {'a': [1, 1000, 777], 'b': 3}
# d2 -> {'a': [1, 1000, 777], 'b': 3}

#_____________________________________________________________________
keys = ('a', 'b', 'c')
values = (1, 2, 3)
d = {k: v for k, v in zip(keys, values)} # d = {'a': 1, 'b': 2, 'c': 3}

keys = ('abcd')
values = range(1, 5)
d = {k: v for k, v in zip(keys, values) if v % 2 == 0} # d = {'b': 2, 'd': 4}

#_____________________________________________________________________
d = dict.fromkeys(['a', 'b', 'c']) # fromkeys(iterable, value=None)
# {'a': None, 'b': None, 'c': None}

d = dict.fromkeys('abcd', 0) 
# {'a': 0, 'b': 0, 'c': 0, 'd': 0}

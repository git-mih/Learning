# 						DICTIONARY VIEWS
# dictionary views can perform set operations: |, &, - and ^ 

# d.keys()   <class 'dict_keys'>    sets like behavior
# d.items()  <class 'dict_items'>   iff there is no unhashable elements
# d.values() <class 'dict_values'>  doesnt act like sets

d1 = {'a': 1, 'b': 2, 'c':3, 'd':4}
d2 = {'b': 20, 'c': 30, 'e': 6}

# applying set intersection operation over the key view
d = {}
for key in d1.keys() & d2.keys():
	d[key] = (d1[key], d2[key]) 
# d = {'b': (2, 20), 'c': (3, 30)}

d = {key: (d1[key], d2[key]) for key in d1.keys() & d2.keys()} # d1 & d2 {'b', 'c'}
# d = {'b': (2, 20), 'c': (3, 30)}

# getting intersection and d2 values only
d = {key: d2[key] for key in d1.keys() & d2.keys()}
# {'c': 30, 'b': 20}

#__________________________________________________________________________________
# views are very dynamic. 
# they mutate/update their values automatically
d = {'a': 1, 'b': 2}

keys = d.keys()       # dict_keys(['a', 'b'])            # 0x0001
values = d.values()   # dict_values([1, 2])              # 0x0004
items = d.items()     # dict_items([('a', 1), ('b', 2)]) # 0x0007

d['z'] = 777          # mutating original dict

# printing/iterating over the views again                   same
# keys  = dict_keys(['a', 'b', 'z'])                     # 0x0001 
# value = dict_values([1, 2, 777])                       # 0x0004
# items = dict_items([('a', 1), ('b', 2), ('z', 777)])   # 0x0007

# whenever we iterate over the views, it goes back to the dict and 
# creates a new iterator and then iterate over the updated dict. 

#__________________________________________________________________________________
# what if we mutate the dictionary while iterating over these views? we cant...
# we cant change the size of the dict while iterating over any view
d = dict(zip('abc', range(1, 4)))    # {'a': 1, 'b': 2, 'c': 3}

# for k, v in d.items():
#   print(k, v)    # a  1   first iteration works ok, but the 2nd we get an
	# del d[k]       RuntimeError: dictionary changed size during iteration.

d = {'a': 1, 'b': 2}
# for k, v in d.items():
# 	print(k, v)    # a  1   trying to insert a new key while iterating over the view
#   d['z'] = 777   RuntimeError: dictionary changed size during iteration.

# we cant modify the size of the dict while we are iterating over an view.
# either items(), keys() or values().

# but its perfectly ok to modify a value while iterating over a view.
d = {'a': 1, 'b': 2, 'c': 3}
for k, v in d.items():
# 	print(k, v)    # a  1       //  b  2        //  c  3
	d[k] = 777     # d['a'] = 777 // d['b'] = 777 // d['c'] = 777

# d = {'a': 777, 'b': 777, 'c': 777}

# we could also modify further elements of the dict
d = {'a': 1, 'b': 2, 'c': 3}
for k, v in d.items():
	# print(k, v)    # a  1   //  b  2    //  c  777
	d['c'] = 777     # d['c'] = 777

#__________________________________________________________________________________
# what if we do want to mutate the size of the dict while iterating over it?
# we can do it 

d = {'a': 1, 'b': 2, 'c': 3}
keys = list(d.keys())  # ['a', 'b', 'c'] 
for k in keys:
	v = d[k]      # v=1  // v=2  // v=3
	# print(k, v) # a 1  // b 2  // c 3
	del d[k]      # deleting the dict key
#                   we can do it cause we're not iterating over the real dict
#                   we are iterating over the list that have a copy of the keys

# d = {}            we deleted the entire dict while iterating

# better way
d = {'a': 1, 'b': 2, 'c': 3}
for k in list(d.keys()):   # ['a', 'b', 'c']
	v = d.pop(k)           # v=1 // v=2 // v=3
	# print(k, v)          # a 1 // b 2 // c 3

# d = {}

# another way
d = {'a': 1, 'b': 2, 'c': 3}
while len(d) > 0:       # len(d) = 3
	k, v = d.popitem()  # pops the last inserted value
	# print(k, v)       # c 3 // b 2 // a 1

# d = {}


#__________________________________________________________________________________
# we can also iterate over the dict directly, iterating over the keys
d = dict.fromkeys('python', 0)    # {'p': 0, 'y': 0, 't': 0, 'h': 0, 'o': 0, 'n': 0}
# for k in d:   
	# print(k)     p // y // t // h // o // n

# or we can do it manually
d_iter = iter(d)
# next(d_iter)  p
# next(d_iter)  y

# list(d_iter) ['t', 'h', 'o', 'n']
# list(d_iter) []


#__________________________________________________________________________________
# we are directly iterating over the hash table.
d = {'a': 1, 'b': 2, 'c': 3}
# for k, v in d.items(): 
# 	print(k, v)

# iterating over the hash table, but we do have to look up the value,
# we are iterating and asking the key value everytime.
d = {'a': 1, 'b': 2, 'c': 3}
# for k in d:
# 	print(k, d[k])

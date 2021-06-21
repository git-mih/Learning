# 						DICTIONARY VIEWS
# d.keys()   <class 'dict_keys'>
# d.values() <class 'dict_values'>
# d.items()  <class 'dict_items'>

# these objects acts like set. and we can perform set
# operations on it, such as:
# |, &, - and ^ (union, intersection, difference, simetric diff(union - diff))

d1 = {'a': 1, 'b': 2, 'c':3, 'd':4}
d2 = {'b': 20, 'c': 30, 'e': 6}

print(type(d1.keys()))
print(type(d1.values()))
print(type(d1.items()))

# getting intersection of d1 and d2 and their values
d = {}
for key in d1.keys() & d2.keys():
	d[key] = (d1[key], d2[key])
print('for loop:')   
print(d)  # {'b': (2, 20), 'c': (3, 30)}

d = {key: (d1[key], d2[key]) for key in d1.keys() & d2.keys()} # d1 & d2 {'b', 'c'}
print('\ndict comprehension:') 
print(d)  # {'b': (2, 20), 'c': (3, 30)}

# getting intersection and d2 values only
d = {key: d2[key] for key in d1.keys() & d2.keys()}
print('\nd2 values only: ') 
print(d)  # {'c': 30, 'b': 20}

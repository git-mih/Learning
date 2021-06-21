# sorting dict based on key values
composers = {'johann': 65, 'ludwig': 56, 'frederic': 39, 'wolfgang': 35}

# sorted(composers.items())   will sort based on ascii code
# [('frederic', 39), ('johann', 65), ('ludwig', 56), ('wolfgang', 35)]

# we now get this list and apply the lambda on each element by using sorted() + key=
# sorted(list, key=lambda e: e[1])
# [('wolfgang', 35), ('frederic', 39), ('ludwig', 56), ('johann', 65)]

ordered_comp = {k: v 
				for k, v in sorted(composers.items(), key=lambda e: e[1])}
# {'wolfgang': 35, 'frederic': 39, 'ludwig': 56, 'johann': 65}

ordered_comp  = dict(sorted(composers.items(), key=lambda e: e[1]))
# {'wolfgang': 35, 'frederic': 39, 'ludwig': 56, 'johann': 65}

#_______________________________________________________________________

# getting intersection of d1 and d2 and their values
d1 = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
d2 = {'b': 20, 'c': 30, 'y': 40, 'z': 50}

d = {}
for key in d1.keys() & d2.keys():
	d[key] = (d1[key], d2[key])
# {'b': (2, 20), 'c': (3, 30)}

d = {k: (d1[k], d2[k]) for k in d1.keys() & d2.keys()}
# {'b': (2, 20), 'c': (3, 30)}

#_______________________________________________________________________

d1 = {'python': 10, 'java': 3, 'c#': 8, 'javascript': 15}
d2 = {'java': 8, 'c++': 13, 'c#': 4, 'go': 9, 'python': 6}
d3 = {'pearl': 5, 'python': 1, 'earlang': 2, 'c': 8}

unsorted = {}
for d in (d1, d2, d3):
	# d = {'python': 10, 'java': 3, 'c#': 8, 'javascript': 15}
	for k, v in d.items():
		# print(unsorted)         {}  // {'python': 10} // {'python': 10, 'java': 3} ...
		# print(f'\n{k} {v}')     python 10 // java 3 ... 
		unsorted[k] = unsorted.get(k, 0) + v # {'python': 10} // {'java': 3} ...

# unsorted = {'python': 17, 'java': 11, 'c#': 12, 'javascript': 15, 'c++': 13, 'go': 9, 'pearl': 5, 'earlang': 2, 'c': 8}

# sorting by key values
sort = dict(sorted(unsorted.items(), key=lambda e: e[1], reverse=True))
# sort =     {'python': 17, 'javascript': 15, 'c++': 13, 'c#': 12, 'java': 11, 'go': 9, 'c': 8, 'pearl': 5, 'earlang': 2}

def merge(*dicts):   # making a funtion of it
	unsorted = {}
	for d in dicts:
		for k, v in d.items():
			unsorted[k] = unsorted.get(k, 0) + v 
	_sorted = dict(sorted(unsorted.items(), key=lambda e: e[1], reverse=True))
	return _sorted

d = merge(d1, d2, d3)
# d = {'python': 17, 'javascript': 15, 'c++': 13, 'c#': 12, 'java': 11, 'go': 9, 'c': 8, 'pearl': 5, 'earlang': 2}

#_______________________________________________________________________
d = dict(zip('abc', range(1, 10))) # {'a': 1, 'b': 2, 'c': 3}

d = {'a': 1, 'b': 2}
# d.get('python')   -> we dont get error. by default it returns None
# d.get('a')        -> 1
# d.get('z', 'N/A') -> N/A

text = """AriAna ipsum dolor sit amet, consectetuer adipiscing
elit. Integer eu lacus accumsan arcu fermentum euismod. Donec
adipiscing. Suspendisse eu lectus. In nunc. Duis vulputate
tristique enim. Donec quis lectus a justo imperdiet tempus."""

# counting how many times each character appears
counts = dict()
for ch in text: 
	key = ch.lower().strip() # removing whte spaces
	if key: # is not empty
		counts[key] = counts.get(key, 0) + 1 
		# 'a': 0+1 || 'o': 0+1 || 'a': 1+1 || ...

# {'a': 12, 'r': 8, 'i': 21, 'n': 14, 'p': 7, 's': 19, 'u': 20, 
#  'm': 9, 'd': 9, 'o': 7, 'l': 6, 't': 16, 'e': 24, ',': 1, 
#  'c': 13, 'g': 3, '.': 7, 'f': 1, 'v': 1, 'q': 2, 'j': 1}

#_____________________________________________________________________
d = dict.fromkeys('abcd', 0)
# 'a' in d   True
# 'z' in d   False

# del d['a']  ->  {'b': 0, 'c': 0, 'd': 0}

result = d.pop('b') # 0
result = d.pop('python', 123) # 123  default, if isnt avaiable inside dict

d = {i: i**2 for i in range(1, 5)} # {1: 1, 2: 4, 3: 9, 4: 16}
# d.popitem()   # pop last item     (4, 16)
# d.popitem()   # pop 2nd last item (3, 9) and so on...

d = dict(a=1, b=2, c=3)
# d.setdefault('a', 77)   1, 'a' is already in the dictionary, it just returns
# d.setdefault('z', 4)    if z inst avaiable, set {'z': 4}

d = dict.fromkeys('abcdefgh', 'N/A')
# d.clear()   d = {}
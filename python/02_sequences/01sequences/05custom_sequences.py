# Custom sequence types:

# the following methods can be defined to implement container objects. containers usually are 
# sequences (such as lists or tuples) or mappings (like dictionaries), but can represent other 
# containers as well.

# __len__(self):
# called to implement the built-in function len(). should return the length of the object, 
# an integer >= 0.


# __getitem__(self, key):
# called to implement evaluation of self[key].

# for Sequence types:
#   - the accepted keys should be integers and slice objects. 
#   - interpretation of negative indexes is up to the __getitem__() method.
#   - if key is of an inappropriate type, TypeError may be raised. 
#   - if a value outside the set of indexes for the sequence IndexError should be raised.

# for Mapping types:
#   - if key is missing (not in the container), KeyError should be raised.

# NOTE: 
# for loops expect that, IndexError get raised for illegal indexes to allow proper detection of 
# the end of the sequence.


# __setitem__(self, key, value):
# called to implement assignment to self[key], like:  self[key] = value
# this should only be implemented for mappings if the objects support changes to the values 
# for keys, or if new keys can be added, or for sequences if elements can be replaced.


# __delitem__(self, key):
# called to implement deletion of self[key], like:  del self[key]
# this should only be implemented for mappings if the objects support removal of keys, or for 
# sequences if elements can be removed from the sequence.


# __contains__(self, item):
# called to implement membership test operators. should return True if item is in self, and 
# False otherwise. 
# for mapping objects, this should consider the keys of the mapping rather than the values.

# for objects that doesnt define __contains__, the membership test first tries iteration via 
# __iter__, then the old sequence iteration protocol via __getitem__.

#____________________________________________________________________________________________________
# any Python object that is able to return an element when given an index is considered a sequence.

hasattr(list, '__getitem__') # True
hasattr(str, '__getitem__')  # True

# if an object provides that, then we should be able to retrieve elements by using [ ] notation:
[1, 2, 3, 4][0] # 1

# __getitem__ support slice objects as well:
'abcde'[2:]     # cde
'abcde'.__getitem__(slice(2, None)) # cde

# we should also be able to iterate through all elements of that sequence:
[e*2 for e in [1, 2, 3]] # [2, 4, 6]


# just keep in mind that, sequence types are iterables, but not all iterables are sequence types:
hasattr(set, '__getitem__')  # False

#____________________________________________________________________________________________________
# immutable sequence types:

# the only operation that immutable sequence types generally implement that is not also implemented 
# by mutable sequence types is support for the hash built-in function, by implementing __hash__.

# this support allow immutable sequences, such as tuples, to be used as dictionary keys and stored 
# in sets and frozensets instances.


# we can also implement the __getitem__ method to be able to retrieve an element based on its 
# index or raise an IndexError exception if the index is out of range.

#____________________________________________________________________________________________________
# creating an sequence type where we can iterate:

# we should raise an IndexError if we want to be able to iterate over sequences. otherwise, Python 
# wont be able to stop the iteration:
class Silly:
    def __init__(self, n):
        self.n = n

    def __getitem__(self, idx):
        if idx < 0 or idx >= self.n:
            raise IndexError('index out of range')
        else:
            return f'silly element at position {idx}'

s = Silly(3)

s[1]     # silly element at position 1
# s[777] # IndexError: index out of range

for item in s: print(item)
# silly element at position 0
# silly element at position 1
# silly element at position 2

[item * 2 for item in s]
# [
#   'silly element at position 0silly element at 0 position 0', 
#   'silly element at position 1silly element at 1 position 1', 
#   'silly element at position 2silly element at 2 position 2'
# ]

#____________________________________________________________________________________________________
# dealing with slices:
class Silly:
    def __init__(self, n):
        self.n = n

    def __getitem__(self, idx):
        return f'receiving an slice object:  {idx}'

# instantiating the Silly object and defining its length:
s = Silly(3)

s[1:]                         # receiving an slice object:  slice(1, None, None)
s[slice(1, None)]             # receiving an slice object:  slice(1, None, None)
s.__getitem__(slice(1, None)) # receiving an slice object:  slice(1, None, None)


# another way of dealing with slices, by returning a new instance of the class:
class MyClass:
    # assuming that we are receiving an sequence type:
    def __init__(self, s):
        self._s = s

    def __getitem__(self, idx):
        if isinstance(idx, slice):
            return MyClass(self._s[idx])
        else:
            return self._s[idx]

    def __repr__(self):
        return f'{type(self).__name__}({self._s})'

c = MyClass([1, 2, 3])

c     # MyClass([1, 2, 3])
c[1:] # MyClass([2, 3])
c[1]  # 2

#____________________________________________________________________________________________________
# (+ and -ve int) and slices:
class Fib:
    def __init__(self, n):
        self.n = n

    @staticmethod
    def _fib(n):
        if n < 2:
            return 1
        return Fib._fib(n - 1) + Fib._fib(n-2)

    def __getitem__(self, idx):
        if isinstance(idx, int):
            if idx < 0:
                idx = self.n + idx
            if idx >= self.n:
                raise IndexError
            else:
                return Fib._fib(idx)
        else:
            # assuming that we are passing an slice object to the idx:
            start, stop, step = idx.indices(self.n)
            return [Fib._fib(item) for item in range(start, stop, step)]

# instantiating the Fib object and defining its length (allowing iteration):
f = Fib(8)

# (int object)   -> int
f[5]   # 8
f[-1]  # 21

# (slice object) -> list
f[4:]  # [5, 8, 13, 21]

for item in Fib(15)[8:12]: print(item)
# 34
# 55
# 89
# 144

[e for e in Fib(15)[8:12]] # [34, 55, 89, 144]

#_______________________________________________________________________________________________________
# mutable sequence types:

# beside the __getitem__ method, the following operatins are defined on mutable sequence types:

# 's' is an instance of a mutable sequence type and 't' is any iterable object.


# __setitem__:
# s[i] = x          item i of s is replaced by x.

# s[i:j] = t        slice of s from i to j is replaced by the contents of the iterable t.

# s[i:j:k] = t      the elements of s[i:j:k] are replaced by those of t.  't' must have the 
#                   same length as the slice it is replacing.


# __delitem__:
# del s[i:j]        same as s[i:j] = []
# del s[i:j:k]      removes the elements of s[i:j:k] from the list.


# s.append(x)       appends x to the end of the sequence (same as s[len(s):len(s)] = [x])
# s.extend(t)       extends s with the contents of t.
# s += t            extends s with the contents of t.
# s.insert(i, x)    inserts x into s at the index given by i (same as s[i:i] = [x]).
# s.copy()          creates a shallow copy of s (same as s[:]).
# s.clear()         removes all items from s (same as del s[:]).
# s.pop()           retrieves the item at i and also removes it from s.
# s.pop(i)          retrieves the item at i and also removes it from s.
# s.remove(x)       remove the first item from s where s[i] is equal to x.
# s *= n            updates s with its contents repeated n times.
# s.reverse()       reverses the items of s in place.

#_______________________________________________________________________________________________________
# in general, we expect that, whenever we perform a concatenation of two sequence objects, the 
# result is a new sequence object of the same type. 
# but if we want to mutate an custom sequence object, we should use in-place concatenation that 
# will mutate the object, and not create a new one.

class Person:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f'MyClass(name={self.name})'

    # concatenation:
    def __add__(self, other):
        return Person(self.name + other.name)

    # in-place concatenation:
    def __iadd__(self, other):
        if isinstance(other, Person):
            self.name += other.name
        else:
            self.name += other
        return self

    # repetition concatenation:
    def __mul__(self, n):
        return Person(self.name * n)
    
    # in-place repetition concatenation:
    def __imul__(self, n):
        self.name *= n
        return self

# concatenation (new object):
p1 = Person('Fabio')    # MyClass(name=Fabio)    <__main__.Person object at 0x01111>
p2 = p1 + Person('Giu') # MyClass(name=FabioGiu) <__main__.Person object at 0x02222>

p1 = Person('Fabio')    # MyClass(name=Fabio)      <__main__.Person object at 0x01111>
p2 = p1 * 2             # MyClass(name=FabioFabio) <__main__.Person object at 0x02222>


# in-place concatenation:
p1 = Person('Fabio')    # MyClass(name=Fabio)    <__main__.Person object at 0x01111>
p1 += Person('Giu')     # MyClass(name=FabioGiu) <__main__.Person object at 0x01111>

p1 = Person('Fabio')    # MyClass(name=Fabio)      <__main__.Person object at 0x01111>
p1 *= 2                 # MyClass(name=FabioFabio) <__main__.Person object at 0x01111>

#_______________________________________________________________________________________________________
import numbers

class Point:
    def __init__(self, x, y):
        if isinstance(x, numbers.Real) and isinstance(y, numbers.Real):
            self._pt = (x, y)
        else:
            raise TypeError('Point co-ordinates must be a real number')
    
    def __repr__(self):
        return f'Point(x={self._pt[0]}, y={self._pt[1]})'

    def __len__(self):
        return len(self._pt)
    
    def __getitem__(self, item):
        return self._pt[item]


class Polygon:
    def __init__(self, *pts):
        if pts:
            self._pts = [Point(*pt) for pt in pts]
        else:
            self._pts = []
        
    def __repr__(self):
        pts_str = ', '.join([str(pt) for pt in self._pts])
        return f'Polygon({pts_str})'

    def __len__(self):
        return len(self._pts)

    def __setitem__(self, key, value):
        try:
            rhs = [Point(*pt) for pt in value]
            is_single = False
        except TypeError:
            try:
                rhs = Point(*value)
                is_single = True
            except TypeError:
                raise TypeError('invalid Point or iterable of Points')
        if (isinstance(s, int) and is_single)\
            or isinstance(s, slice) and not is_single:
            self._pts[s] = rhs
        else:
            raise TypeError('incompatible index/slice assignment')

    def __getitem__(self, value):
        return self._pts[value]

    def append(self, pt):
        self._pts.append(Point(*pt))

    def insert(self, i, pt):
        self._pts.insert(i, Point((pt)))

    def extend(self, other):
        if isinstance(other, Polygon):
            self._pts += other._pts
        else:
            points = [Point(*pt) for pt in other]
            self._pts += points
    
    def pop(self, i):
        return self._pts.pop(i)

    def __iadd__(self, other):
        self.extend(other)
        return self
    
    def __delitem__(self, item):
        del self._pts[item]


p = Polygon((0, 0), (1, 1), (2, 2))

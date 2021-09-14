# Custom sequences:

# any Python object that is able to return an element when given an index number is considered
# an sequence type, and to create our own sequence type objects, we just require to implement
# this behaviour.

from typing import Type


hasattr(list, '__getitem__') # True
hasattr(str, '__getitem__')  # True

# if an object provides it, then we should be able to retrieve elements by using [ ] notation. 
# we should also be able to iterate through all elements of that sequence:
[1, 2, 3, 4][0]          # 1
'abcde'[2:]              # cde
[e*2 for e in [1, 2, 3]] # [2, 4, 6]

# just keep in mind that, sequence types are iterables, but not all iterables are sequence types:
hasattr(set, '__getitem__')  # False

#____________________________________________________________________________________________________
# custom immutable sequence type:

# at its most basic, an immutable sequence type should be able to, given an index, return the 
# element present at that index. for that, we require to implement the __getitem__ method.



# __getitem__ method:

# should return the element that is avaiable in that specific index or raise an IndexError 
# exception if the index is out of range.

# the __getitem__ method gets called whenever we use the [ ] notation:
[1, 2, 3, 4][0]             # 1
[1, 2, 3, 4].__getitem__(0) # 1

class Silly:
    def __getitem__(self, idx):
        if isinstance(idx, int):
            return f'silly element at position {idx}'

s = Silly()      # <__main__.Silly object at 0x001>
s[0]             # silly element at position 0
s[3]             # silly element at position 3
s.__getitem__(4) # silly element at position 4


# creating a sequence type where we can iterate:

# we should care about raise an IndexError if we want to be able to iterate over sequences,
# otherwise, Python wont be able to stop its iteration:
class Silly:
    def __init__(self, n):
        self.n = n

    def __getitem__(self, idx):
        if idx < 0 or idx >= self.n:
            raise IndexError('index out of range')
        else:
            return f'silly element at position {idx}'

s = Silly(3)     # <__main__.Silly object at 0x001>
s[1]             # silly element at position 1
s.__getitem__(0) # silly element at position 0
# s[777]         # IndexError: index out of range


# iterating:
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


# to deal with slices, we just require to differentiate it from integers, cause we can pass either
# an integer as index, or a slice object:
class Silly:
    def __init__(self, n):
        self.n = n
    
    def __len__(self):
        return self.n

    def __getitem__(self, idx):
        return f'receiving an slice object:  {idx}'

# instantiating the Silly object and defining its length:
s = Silly(3) # <__main__.Silly object at 0x001>
len(s)       # 3

s[1:]                         # receiving an slice object:  slice(1, None, None)
s[slice(1, None)]             # receiving an slice object:  slice(1, None, None)
s.__getitem__(slice(1, None)) # receiving an slice object:  slice(1, None, None)



# providing both, integer (+ and -ve) and slices objects:
class Fib:
    def __init__(self, n):
        self.n = n

    @staticmethod
    def _fib(n):
        if n < 2:
            return 1
        return Fib._fib(n - 1) + Fib._fib(n-2)
    
    def __len__(self):
        return self.n

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
fibonacci = Fib(8) # <__main__.Fib object at 0x001>

# passing index: (integer object) -> int
fibonacci[5]   # 8
fibonacci[-1]  # 21

# passing index: (slice object) -> list
fibonacci[4:]  # [5, 8, 13, 21]

# iterating:
for item in Fib(15)[8:12]: print(item)
# 34
# 55
# 89
# 144

[e for e in Fib(15)[8:12]] # [34, 55, 89, 144]



# another way of dealing with slices, by returning a new instance of the class:
class MyClass:
    # assuming that we are receiving an sequence type:
    def __init__(self, s):
        self._s = s

    def __getitem__(self, idx):
        if isinstance(idx, slice):
            # we return a new sliced sequence type:
            return MyClass(self._s[idx])
        else:
            return self._s[idx]

    def __repr__(self):
        return f'{type(self).__name__}({self._s})'

c = MyClass([1, 2, 3]) # <__main__.MyClass object at 0x001>

c     # MyClass([1, 2, 3])
c[1:] # MyClass([2, 3])
c[1]  # 2

#_______________________________________________________________________________________________________
# custom mutable sequence type:

# in general, we expect that, whenever we perform a concatenation of two sequence objects, the 
# result is a new sequence object of the same type. but if we want to mutate an custom sequence 
# object, we should use in-place concatenation that will mutate the object, and not create a 
# new one.

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

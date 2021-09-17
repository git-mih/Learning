# Cyclic iterators:

# allow us to keep looping over the same collection. for exemple, we may want to loop through
# an collection 10 times, but the collection has a length of 4, in practice if we try to call
# next on that collection after its 4 iterations, we would get a StopIteration exception and
# get out the loop.

# # Cyclic iterators allow us to keep iterating over that collection again and again. 

class CyclicIterator:
    def __init__(self, l):
        self.l = l
        self.i = 0

    def __iter__(self):
        return self
    
    def __next__(self):
    # 0%4  1%4  2%4  3%4  4%4  5%4  6%4  7%4  8%4  9%4  ... 
    #  0    1    2    3    0    1    2    3    0    1    
        result = self.l[self.i % len(self.l)] 
        self.i += 1
        return result

iter_cyc = CyclicIterator('FABI')
for _ in range(10): print(next(iter_cyc), end='') # FABIFABIFA


# we require to raise an StopIteration exception to be able to use it in a for loop:
class CyclicIterator:
    def __init__(self, l, length):
        self.l = l
        self.i = 0
        self.length = length

    def __iter__(self):
        return self
    
    def __next__(self):
        if self.i >= self.length:
            raise StopIteration
        else:
            result = self.l[self.i % len(self.l)] 
            self.i += 1
            return result

iter_cyc = CyclicIterator('FABI', 20)
for e in iter_cyc: print(e, end='') # FABIFABIFABIFABIFABI


# itertools equivalent:
import itertools
from typing import final

iter_cyc = itertools.cycle('FABI')
for _ in range(10): print(next(iter_cyc), end='') # FABIFABIFA

#_______________________________________________________________________________________________________
# generic cyclic iterator:

class CyclicIterator:
    def __init__(self, iterable):
        self.iterable = iterable
        self.iterator = iter(self.iterable) # creating the iterator once.

    def __iter__(self):
        return self
    
    def __next__(self):
        try:
            item = next(self.iterator)
        except StopIteration: # re-creating the iterable once it get exhausted.
            self.iterator = iter(self.iterable)
            item = next(self.iterator)
        finally:
            return item

iter_cyc = CyclicIterator('ABC')
for _ in range(10): print(next(iter_cyc)) # ABCABCABCA

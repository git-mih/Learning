# Python optimization:  Interning

# important note is that, a lot of what we discuss with memory management, gc and optimizations,
# is usually specific to the Python implementation that we are using.

# earlier we saw that, if we had this:
a = 10 # <'int' object at 0x000001>
b = 10 # <'int' object at 0x000001>

# they both are shared references, both share the same object essentially.

# but what about this:
a = 500 # <'int' object at 0x000001>
b = 500 # <'int' object at 0x000007>

# Python doesnt create a shared reference in this case, why not?
# it is something called interning. and interning is basicly re-use objects on-demand.

# at startup, Python pre-loads (caches) a global list of integers objects between [-5, 256].
# it means that, any time an integer is referenced in that range, Python will just use the cached
# version of that object, not requiring to computate it.

# these integers object between -5, 256 are Singletons objects essentially. in other words, they
# are classes that only can be instantiated once. if we try to create a new object from that, it
# doest do it, will just return the first one that was created.

# it is just an optimization strategy, cause small integer objects shows up very often so, when
# we assign a variable to reference some integer object in that range:
a = 10

# Python will essentially just point to the existing reference to that integer object, it doesnt
# have to create that integer object again, it was already been created when Python started up.

# but if we write:
a = 257  # Python doesnt use that global list, a new object is created every time now.


# some strings are also automatically interned by Python, but not all. 
# as the Python code gets compiled, identifiers are interned, such as: 
#   variable names, function names, class names, etc...

# some string literals may also be automatically interned. in general, strings that looks like
# an identifier:
a = 'some_long_string' # <'str' object at 0x000001>
b = 'some_long_string' # <'str' object at 0x000001>
a is b  # True

# but if they dont looks like identifiers, they dont get interned automatically by Python:
a = 'the quick brown fox jumps over the lazy dog' # <'str' object at 0x000001>
b = 'the quick brown fox jumps over the lazy dog' # <'str' object at 0x000007>
a is b  # False


# it is all about speed and possiibly memory optimization. lets say that we want to see if two 
# strings are equal. using equality operator '==' will compare the strings character by character.

# but if we know that `some_long_string...` string object has been interned by Python, then 
# `a` and `b` will share the same reference, the same object in memory essentially. 
# now we can use identity operator 'is' which is much faster than character by character look up.


# not all strings are automatically interned by Python but we can force strings to be interned
# by using the sys.intern() method:
import sys

# the following strings doesnt looks like identifiers, they will not be interned automatically.
# but we gonna interne them explicitly with the sys module:
a = sys.intern('the quick brown fox jumps over the lazy dog') # <'str' object at 0x000001>
b = sys.intern('the quick brown fox jumps over the lazy dog') # <'str' object at 0x000001>
a is b  # True

#____________________________________________________________________________________________________
# Python optimization:  Peephole

# this is another variety of optimization that happen at compile time. it means that, once our
# application is running, once a piece of code gets compiled, its going to keep using that 
# compiled version of the code.

# certain things get optimized, for exemple: 
#   constant expressions:
24 * 60  # 1440

# Python will pre-calculate that constant expression once and cache its value. and whenever we
# perform that calculation, it doesnt required to be re-calculated, Python just returns that
# constant value (1440).

#   short sequences (< 20):
(1, 2) * 5        # (1, 2, 1, 2, 1, 2, 1, 2, 1, 2)
'abc' * 3         # abcabcabc
'hello' + 'world' # hello world (<20)

# but if we have sequences where the length is > 20:
'the quick brown fox' * 10



# membership tests are another peephole technique where mutables objects are replaced by immutables.
2 in [1, 2, 3]  # True

# lists are mutable and there is no variables inside that list object, so it cant change its values.
# therefore we have a constant expression. it means that, when Python compile that line of code, 
# it will replace that list object to its immutable counterpart. 

# Python will do it essentially:
2 in (1, 2, 3)  # True

# set membership is much faster than list or tuple membership. it happen because sets are basicly
# dictionaries. and is way more faster to make a look up by using hash maps than collection object:

# instead of writing:
2 in (1, 2, 3)

# we should really think of writing it by using sets:
2 in {1, 2, 3}


# lets compile a block of code inside a function, and Python will pre-calculate all constant
# expressions on it:
def f():
    a = 24 * 60
    b = (1, 2) * 5
    c = 'abc' * 3
    d = 'the quick brown fox' * 10
    e = [1, 2] * 3

# the compiled code object is accessible via the attribute __code__ on the function and carries 
# a few important attributes. but we are interested in co_consts:
f.__code__.co_consts

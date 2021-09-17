# Copying sequences: 

#___________________________________________________________________________________________________
# Shallow copy:

# an Shallow copy creates a new object, but it uses all the objects that were inside the
# copied list and uses the same references (memory address) in the new copied object.

# immutable elements:
s = [1, 2]
id(s)     # 0x1111
id(s[0])  # 0x01
id(s[1])  # 0x02

cp = s.copy()
id(cp)    # 0x2222
id(cp[0]) # 0x01
id(cp[1]) # 0x02

# when we made a copy of 's', the sequence object was copied, but its elements points to the
# same memory address as the original sequence elements. the sequence was copied, but its 
# elements were not. this is called a Shallow copy. it copy the container itself, not the items.


# mutable elements:
s = [[0, 0], [0, 0]] # 0x1111
cp = s.copy()        # 0x2222

# we essentially copied the container:
s[0] is cp[0]        # True

# if we change the container, we are not going to change the original sequence:
cp[0] = 777
cp   # [777, [0, 0]]
s    # [[0, 0], [0, 0]]

# but, the elements inside that copied container are sharing the same references:
s = [[0, 0], [0, 0]] # 0x1111
cp = s.copy()        # 0x2222

cp[0][0] = 777
cp   # [[777, 0], [0, 0]]
s    # [[777, 0], [0, 0]]

#___________________________________________________________________________________________________
# Deep copy:

# if collections contains mutable elements, shallow copies are not sufficient to ensure that, 
# the copy will not modify the original sequence object.

# the ideia of deep copy is that, we want to make sure that our copy will not share reference
# with the elements of the original sequence object.

# Partial deep copy:
s = [[0, 0], [0, 0]]       # 0x1111

# making a copy of every element of the original sequence:
cp = [e.copy() for e in s] # 0x2222

cp[0][0] = 777
cp  # [[777, 0], [0, 0]]
s   # [[0, 0], [0, 0]]

# in this case, we not just making a copy of the container: [0, 0], like we were. we are 
# essentially copying its elements as well. but, we are making a shallow copy of each element.

# if we had inner mutable sequences as well, we would be copying its container at that level, 
# not its elements again. the elements would share the same reference:
s = [[[0, 0], [0, 0]], [[0, 0], [0, 0]]] # 0x1111
cp = [e.copy() for e in s]               # 0x2222

cp[0][0][0] = 777
cp[1][0][0] = 999
cp # [[[777, 0], [0, 0]], [[999, 0], [0, 0]]]
s  # [[[777, 0], [0, 0]], [[999, 0], [0, 0]]]

# we would need to make copies like that, at least 3 levels deep to ensure a true Deep copy.
# Deep copies, in general, tends to need a recursive approach, but if we would try to do it
# ourselves, we would require to be careful with circular references:
a = [10, 20]
b = [a, 30]
a.append('b')

#___________________________________________________________________________________________________
# copy module:

# the standard library 'copy' have an generic copy and deepcopy operation.
# it provides a copy version because isnt every object that can make shallow copy of itself. 
# for exemple, built-in objects like, lists, sets, dictionaries have the 'copy' method, they 
# can do it.

import copy

# Shallow copy:
s = [1, 2, 3]      # [1, 2, 3] 0x1111
cp = copy.copy(s)  # [1, 2, 3] 0x2222

# Deep copy:
s = [[[0, 0], [0, 0]], [[0, 0], [0, 0]]] # 0x1111
cp = copy.deepcopy(s)                    # 0x2222

cp[0][0][0] = 777

s  # [[[0, 0], [0, 0]], [[0, 0], [0, 0]]] 
cp # [[[777, 0], [0, 0]], [[0, 0], [0, 0]]]


# custom classes can implement the __copy__ and __deepcopy__ methods that will allow us to
# override how shallow and deepcopies are made for our custom objects. but the copy module
# will now how to make a copy even if we dont explicity specify these attributes in our class:
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __repr__(self):
        return f'Point({self.x}, {self.y})'

class Line:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
    
    def __repr__(self):
        return f'Line({self.p1.__repr__()}, {self.p2.__repr__()})'

p1 = Point(0, 0)
p2 = Point(0, 0)

line1 = Line(p1, p2)         # 0x1111
line2 = copy.deepcopy(line1) # 0x2222

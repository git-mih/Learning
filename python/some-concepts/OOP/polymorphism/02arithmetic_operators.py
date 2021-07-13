# Special methods: arithmetic operators:
class C:
	def __add__(self, other): ...      # +
	def __sub__(self, other): ...      # -
	def __mul__(self, other): ...      # *
	def __truediv__(self, other): ...  # /
	def __floordiv__(self, other): ... # //
	def __mod__(self, other): ...      # %
	def __pow__(self, other): ...      # **
	def __matmul__(self, other): ...   # @

# when we try to perform some operation like, add:
a = 4
b = 2

a + b         # 6
# Python is essentyally calling the __add__ method.
a.__add__(b)  # 6

# To indicates the operation isnt suported, we implement the corresponding method
# and return NotImplemented

#___________________________________________________________________________________
# Special methods: Reflected operators:
class C:
	def __radd__(self, other): ...     
	def __rsub__(self, other): ...     
	def __rmul__(self, other): ...     
	def __rtruediv__(self, other): ... 
	def __rfloordiv__(self, other): ...
	def __rmod__(self, other): ...     
	def __rpow__(self, other): ...     
	def __rmatmul__(self, other): ...  

# consider: 
a = 2
b = 4

# when we try to perform some operation like, add:
a + b  # 6

# Python will attempt to call the __add__ method.
a.__add__(b)  # 6


# if the __add__ returns NotImplemented and the operands are not of the same type,
# Python will swap the operands and try this instead:
b.__radd__(a) # 6
		
#___________________________________________________________________________________
# Special Methods: in-place operators:
class C:
	def __iadd__(self, other): ...      # +=
	def __isub__(self, other): ...      # -=
	def __imul__(self, other): ...      # *=
	def __itruediv__(self, other): ...  # /=
	def __ifloordiv__(self, other): ... # //=
	def __imod__(self, other): ...      # %=
	def __ipow__(self, other): ...      # **=
	def __imatmul__(self, other): ...   # @=

l = [1, 2, 3]       # id(l) 0x00001

# in-place mutation. 
l += [4, 5]
# l.__iadd__([4, 5])

l # [1, 2, 3, 4, 5] # id(l) 0x00001


class Person:
	def __init__(self, name):
		self.name = name
	def __repr__(self):
		return f"Person('{self.name}')"
		
class Family:
	def __init__(self, mother, father):
		self.mother = mother
		self.father = father
		self.children = []

	def __iadd__(self, other):
		self.children.append(other)
		return self

f = Family(Person('Mary'), Person('John'))
f.children  # []

f += Person('Eric')
f.children  # [Person('Eric')]

f += Person('Fabio')
f.children  # [Person('Eric'), Person('Fabio')]

#___________________________________________________________________________________
# Special Methods: unary operators, functions
class C:
	def __neg__(self): ...      # -operand
	# not the same as subtraction, this negative is a unary operator which takes a
	# single operand and operates on it.

	def __pos__(self): ...      # +operand
	# same

	def __abs__(self): ...      # abs(operand)
	# used by the abs() builtin function.

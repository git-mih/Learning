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

class Number:
	def __init__(self, x):
		self.x = x
	
	def __add__(self, other):
		if isinstance(other, Number):
			return self.x + other.x
		return NotImplemented

# To indicates the operation isnt suported, we implement the corresponding method
# and return NotImplemented.

a = Number(3)
b = Number(7)

# when we try to perform the addition operation
a + b         # 10

# Python is essentyally calling the __add__ method.
a.__add__(b)  # 10

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

class Number:
	def __init__(self, x):
		self.x = x
	
	def __add__(self, other):
		if isinstance(other, Number):
			return self.x + other.x
		return NotImplemented

	def __radd__(self, other):  # self = a, other = 7
		return self.x + other   # self.x = 3 + 7 = 10

a = Number(3) # type(a)  <class 'Number'>

# 7 + a         # TypeError: unsupported operand type(s) for +: 'int' and 'Number'
# 7.__add__(a)  # TypeError: unsupported operand type(s) for +: 'int' and 'Number'

# once the 7.__add__(a) fails cause we cant add 'int' + 'Number'
# Python will attempt to call the __radd__ method. swaping the operands like: 
a.__radd__(7)  # 10

# if we dont provide the reflected operator __radd__, we will get the same error:
# a + 7         # TypeError: unsupported operand type(s) for +: 'Number' and 'int'
# a.__radd__(7) # TypeError: unsupported operand type(s) for +: 'Number' and 'int'

# but once we have implemented the __radd__ method, it will works properly:
7 + a   # 10

# at first, it will fail, then Python will try: 
a.__radd__(7) # and it will works   # 10

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

class Number:
	def __init__(self, x):
		self.x = x
	
	def __neg__(self):
		return -self.x

	def __abs__(self):
		return abs(self.x)

a = Number(3)

-a      # -3
abs(a)  #  3
abs(-a) #  3
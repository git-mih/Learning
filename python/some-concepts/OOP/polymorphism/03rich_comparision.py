# Special methods: Rich Comparasions
class C:
	def __lt__(self, other): ... # <
	def __le__(self, other): ... # <=

	def __eq__(self, other): ... # ==
	def __ne__(self, other): ... # !=

	def __gt__(self, other): ... # >
	def __ge__(self, other): ... # >=

# if the method returns NotImplemented, Python automatically try to use the reflection. 
# eg:
a = 4
b = 2

a < b # if this method __lt__ is implemented and retursn NotImplemented it will try:
b > a

class Number:
	def __init__(self, x):
		self.x = x
	
	def __eq__(self, other):
		if isinstance(other, Number):
			return self.x == other.x
		return NotImplemented

	def __lt__(self, other):
		if isinstance(other, Number):
			return abs(self.x) < abs(other.x)
		return NotImplemented

a = Number(3)
b = Number(3)
c = Number(7)

a is b # False

a == b # True
a == c # False


a < c  # True

c > a  # True
# we did not implemented the __gt__. but it works cause we defined the __lt__.
# Python try to call n3.__gt__(n1), it returns NotImplemented and then Python try to
# call the reflected operator n1.__lt__(n3). and this one we defined.

#___________________________________________________________________________________
# we can use a special decorator from functools module to fill mostly of these methods
# for us. we just require to implement the __eq__ method and one of the Rich comparasion
# methods.
from functools import total_ordering

@total_ordering
class Number:
	def __init__(self, x):
		self.x = x
	
	def __eq__(self, other):
		if isinstance(other, Number):
			return self.x == other.x
		return NotImplemented
	
	def __lt__(self, other):
		if isinstance(other, Number):
			return self.x < other.x
		return NotImplemented

a = Number(3)
b = Number(3)
c = Number(7)

a < b  # False

# total_ordering implement automatically the __le__ and many more.
a <= b # True
a <= c # True
# every object have the __repr__ method. its inherited from the base class that
# all objects have.

# __repr__ will be called if __str__ isnt specified. or we can also
# call repr() which will explicitly call the __repr__ method.
class Point:
	pass

p = Point()
p               # <__main__.Person object at 0x000001DE61C49EE0>  inherited
repr(p)         # <__main__.Person object at 0x000001DE61C49EE0>  inherited

# if __str__ doesnt exist, python falls back to the __repr__ method. The default one.

print(p)        # <__main__.Person object at 0x000001DE61C49EE0>  inherited
print(str(p))   # <__main__.Person object at 0x000001DE61C49EE0>  inherited

#___________________________________________________________________________
# both, __repr__ and __srt__.
class Person:
	def __init__(self, name, age):
		self.name = name
		self.age = age

	def __repr__(self) -> str:
		return f"Person(name='{self.name}', age={self.age})"

	def __str__(self):
		return self.name

p = Person('Python', 36)

p               # Person(name='Python', age=36)
repr(p)         # Person(name='Python', age=36)

# print() is looking for the __srt__ method.
print(p)        # Python
print(str(p))   # Python

#___________________________________________________________________________
# implementing __repr__ method only.
class Person:
	def __init__(self, name, age):
		self.name = name
		self.age = age

	def __repr__(self) -> str:
		return f"Person(name='{self.name}', age={self.age})"

p = Person('Python', 36)

# print() is looking for the __srt__ method. doesnt find, then call __repr__.
p               # Person(name='Python', age=36)
repr(p)         # Person(name='Python', age=36)
print(p)        # Person(name='Python', age=36)
print(str(p))   # Person(name='Python', age=36)

#___________________________________________________________________________
# format functions will also prefer to call __str__ when avaiable.
f'The person is {p}'       # The person is Python
'The person is'.format(p)  # The person is Python
'The person is %s' % p     # The person is Python

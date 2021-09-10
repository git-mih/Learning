# Duck typing:

# is an concept where the class data type isnt checked if minimum methods/attr are avaiable.

#     "if it walks like a duck, and it quacks like a duck, then it must be a duck."

class Duck:
	def walk(self):
		print('the Duck is walking')

	def talk(self):
		print('the Duck is quacking')

class Chicken:
	def walk(self):
		print('the Chicken is walking')

	def talk(self):
		print('the Chicken is clucking')



class Person:
	def catch(self, duck):
		duck.walk() 
		duck.talk()
		print('Person caught the critter')

d = Duck()       # <Duck object at 0x001>
c = Chicken() # <Chicken object at 0x002>

person = Person()   
person.catch(d) # The Duck is walking... the Duck is Quacking! Person caught the critter.

# we can also catch a Chicken object cause it has the same walk/talk methods:
person.catch(c) # The Chicken is walking... the Chicken is Clucking! Person caight the critter.

# "its walking like a duck, and talking like a duck, then it must be a duck"

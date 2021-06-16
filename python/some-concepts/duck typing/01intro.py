# "if it walks like a duck, and it quacks like a duck, then it must be a duck."
#	Concept where the class type isnt checked if minimum methods/attr are present.

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

#############################################
duck = Duck()
chicken = Chicken()

person = Person()
person.catch(duck)
person.catch(chicken) # also works, cause it have the same walk/talk methods
                      # "its walking like a duck, and talking like a duck, then it must be a duck"
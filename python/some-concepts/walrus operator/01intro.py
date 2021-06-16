# Walrus operator
# We can also call it Assignement expression
# it assign values to variables as part of a larger expression

print(happy := True) # True

while food := input('some food: '): 
	if food == 'stop':
		break
	print(f'food = {food}')

# while food := input('some food: ') != 'stop':
# would also work, but it would evaluate the (input and !=) and return True/False
# and then assign True/False to food.  

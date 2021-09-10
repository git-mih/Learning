import json

from pprint import pprint
from decimal import Decimal

# JSON objects are all strings

# serializing
d = {'a': 100, 'b': 200}
j = json.dumps(d)          # j = {"a": 100, "b": 200} <class 'str'>

j = json.dumps(d, indent=2)
# j = '{
#   	  "a": 100,
#   	  "b": 200
# 	    }'

# deserializing
d = json.loads(j)          # d = {'a': 100, 'b': 200} <class 'dict'>
# old_d == d  True 
# old_d is d  False 

#______________________________________________________________________
# JSON keys have to be strings. So, JSONEncode will convert keys 
# to be string type automatically

d = {1: 'jhon', 2: 'eric'} # int keys
j = json.dumps(d)          # j = {"1": "jhon", "2": "eric"} 'str'

d = json.loads(j)          # {'1': 'jhon', '2': 'eric'}     'dict'
# old_d == d  False 
# no longer have the same value as before...

j = '''   
{
	"name": "Jhon Cleese",
	"age": 82,
	"heigt": 1.96,
	"walksFunny": true,
	"sketches": [
		{
			"tittle": "Dead Parrot",
			"costars": ["Michael Pallin"]
		},
		{
			"tittle": "Ministry of Silly Walks",
			"costars": ["Michael Pallin", "Terry Jones"]
		}
	],
	"boring": null
}
''' 
d = json.loads(j) # pprint(d)
# d = 
# {'age': 82,
#  'boring': None,
#  'heigt': 1.96,
#  'name': 'Jhon Cleese',
#  'sketches': [{'costars': ['Michael Pallin'], 'tittle': 'Dead Parrot'},
#               {'costars': ['Michael Pallin', 'Terry Jones'],
#                'tittle': 'Ministry of Silly Walks'}],
#  'walksFunny': True}

# d['age']        -> int
# d['height']     -> float
# d['sketches']   -> list
# d['walksFunny'] -> bool


#______________________________________________________________________
# JSON doesnt understand what Tuple is, it will convert tuple to list
d = {'a': (1, 2, 3)}
j = json.dumps(d)    # {"a": [1, 2, 3]}    d['a'] -> list

d = json.loads(j)    # {'a': [1, 2, 3]}

# bad JSON
j = '{"a": (1, 2, 3)}' 
# d = json.loads(j)  JSONDecoder unable to decode this json string

#______________________________________________________________________
# What about other data types? such as sets, Decimal, etc..

# set
# json.dumps({'a': {1, 2, 3}})
# TypeError: Object of type set is not JSON serializable

# well, we could fix it casting the set
json.dumps({'a': list({1, 2, 3})})     #  {"a": [1, 2, 3]}

# Decimal
# json.dumps({'a': Decimal('3.14')}) 
# TypeError: Object of type Decimal is not JSON serializable

# JSON expects a dict and we are passing it, but JSONEncoder doesnt know
# how to serialize these specific objects by default.

# samething happen with complex numbers, Date objects and so on
# try:
# 	json.dumps({'a': 1+1j})
# except TypeError as ex:
# 	print(ex)         Object of type complex is not JSON serializable

# JSONEncoder only can handle simple data types like:
# dict, list, str, int, float, bool and None.

# it also understands NaN, Infinity & -Infinity as their 
# corresponding float values, which is outside the JSON spec.

#______________________________________________________________________
# Providing custom data type to JSONEncoder
class Person:
	def __init__(self, name, age):
		self.name = name
		self.age = age
	
	def __repr__(self):
		return f'Person(name={self.name}, age={self.age})'

p = Person('Fabio', 26)  # Person(name=Fabio, age=26) <class 'Person'>
# j = json.dumps({'person1': p})
# TypeError: Object of type Person is not JSON serializable

# to fix that, we should convert the Person object to dict
class Person:
	def __init__(self, name, age):
		self.name = name
		self.age = age
	
	def __repr__(self):
		return f'Person(name={self.name}, age={self.age})'

	def toJSON(self):    # return {'name': 'Fabio', 'age': 26}
		return dict(name=self.name, age=self.age) 

p = Person('Fabio', 26)  # Person(name=Fabio, age=26)   <class 'Person'>
p.toJSON()               # {'name': 'Fabio', 'age': 26} <class 'dict'>

j = json.dumps({'person1': p.toJSON()}) 
# j = '{"person1": {"name": "Fabio", "age": 26}}'


# we can also use the vars()/__dict__ method which does the same.
# it will make a dict with all of our object attributes.
class Person:
	def __init__(self, name, age):
		self.name = name
		self.age = age

	def toJSON(self):    
		return vars(self) # return {'name': 'Fabio', 'age': 26}

p1 = Person('Fabio', 26).toJSON() # we can also use directly
p2 = Person('Giu', 24).toJSON() 

j = json.dumps({'person1': p2, 'person2': p2}, indent=2)
# {
#   "person1": {
#     "name": "Giu",
#     "age": 24
#   },
#   "person2": {
#     "name": "Giu",
#     "age": 24
#   }
# }

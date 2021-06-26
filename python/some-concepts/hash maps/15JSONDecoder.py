import json
from json import JSONDecoder

# JSONDecoder get a JSON string and return something out of it. 
# usually a python dictionary. in this case we're doing nothing beside returning
# a string message
class CustomDecoder(JSONDecoder):
	def decode(self, arg):
		# print('decode: ', type(arg), arg)
		return 'a simple string object'

j = '''
{
	"a": 100,
	"b": [1, 2, 3],
	"c": "python",
	"d": {
		"e": 4,
		"f": 5.5
	}
}
'''
result = json.loads(j, cls=CustomDecoder)
# decode:  <class 'str'>
# {
#         "a": 100,
#         "b": [1, 2, 3],
#         "c": "python",
#         "d": {
#                 "e": 4,
#                 "f": 5.5
#         }
# }

# result = a simple string object

#____________________________________________________________________________
class Point:
	def __init__(self, x, y):
		self.x = x
		self.y = y

	def __repr__(self):
		return f'Point(x={self.x}, y={self.y})'

j1 = '''
{
	"points": [
		[10, 20],
		[-1, -2],
		[0.5, 0.5]
	]
}
'''

j2 = '''
{
	"a": 1,
	"b": 2
}
'''
# overwriting the decode method in a subclass of JSONDecoder. kinda like we did
# before with the default method of JSONEncoder and the json.dumps function w/default.
class CustomDecoder(JSONDecoder):
	def decode(self, arg):      # arg is the json string.
		if 'points' in arg:     # checking if 'points' is a substring of arg. 
			d = json.loads(arg) 
			return 'parsing object for points'
		else:     # we delegate to the parent class handle the error
			return super().decode(arg) 

# JSONDecoder handled directly, we are using the default decode method 
# json.loads by default call the JSONDecoder.decode()
json.loads(j1)
# {'points': [[10, 20], [-1, -2], [0.5, 0.5]]}  

# now json.loads will call our modifyed decode method
json.loads(j1, cls=CustomDecoder)  # parsing object for points
# before JSONDecoder try to deserialize the json string, json.loads will
# delegate it to our custom decoder try to deserialize these json objects one by one.

# the json objects that our custom decoder wont be able to parse will be
# passed away to the JSONDecoder handle.
json.loads(j2, cls=CustomDecoder)
# {'a': 1, 'b': 2}
# j2 is being delegated to JSONEncoder handle. 
# our custom decoder is passing it away cause our custom decoder doesnt know
# how to handle or we're just delegating to JSONDecoder handle exceptions.

#____________________________________________________________________________
j1 = '''
{
	"points": [
		[10, 20],
		[-1, -2],
		[0.5, 0.5]
	]
}
'''
class CustomDecoder(JSONDecoder):
	def decode(self, arg):
		d = json.loads(arg) # JSONDecoder deserialize it and we are going to customize
		if 'points' in d:   # checking if 'points' is some key now.
			d['points'] = [Point(x, y) for x, y in d['points']]
		return d

json.loads(j1, cls=CustomDecoder)
# {'points': [Point(x=10, y=20), Point(x=-1, y=-2), Point(x=0.5, y=0.5)]}

json.loads(j1)
# {'points': [[10, 20], [-1, -2], [0.5, 0.5]]}

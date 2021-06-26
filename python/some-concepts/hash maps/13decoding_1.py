# json.loads function parameter object_hook.  acts kinda like the default of dumps()
import json

from datetime import datetime
from fractions import Fraction

# deals with any level recursevly and not only root json object.
j = '''
{
	"a": 1,
	"b": 2,
	"c": {
		"c.1": 1,
		"c.2": 2,
		"c.3": {
			"c.3.1": 1,
			"c.3.2": 2
		}
	}
}
'''
def handler_decoder(arg):
	# print('decoding:', arg)
	return arg

d = json.loads(j, object_hook=handler_decoder)
# decoding: {'c.3.1': 1, 'c.3.2': 2}   #  "c.3" object (inner most)
# decoding: {'c.1': 1, 'c.2': 2, 'c.3': {'c.3.1': 1, 'c.3.2': 2}}  #  "c" object (2nd inner)
# decoding: {'a': 1, 'b': 2, 'c': {'c.1': 1, 'c.2': 2, 'c.3': {'c.3.1': 1, 'c.3.2': 2}}}  #  root object

# when it start decode the root object, all inner objects was already handled by
# our custom decoder function.
# d = {'a': 1, 'b': 2, 'c': {'c.1': 1, 'c.2': 2, 'c.3': {'c.3.1': 1, 'c.3.2': 2}}}

# its a silly decoder that does nothing besides pass away the objects. 
# but we can do whatever we wants to.


# the dumps() function used to call the default method whenever it could not
# serialize a custom/standard python object.
# the loads() function calls the object_hook method for each json object it founds
# starting for the inner most json object. so we dont have to deal with it recursevly.
# the JSONDecoder do the recursive work for us.

# our decoder get called 3 times, cause the json object have 3 layers of json objects.
# "c.3" is a json object, "c" is also a json object and finally, the root json object
# where "a", "b" and "c" sits, the entire object itself.

#_______________________________________________________________________________
j = '''
{
	"time": {
		"objecttype": "datetime",
		"value": "2018-10-21T09:14:00"
	},
	"message": "created this json string"
}
'''

def custom_decoder(arg):
	if 'objecttype' in arg and arg['objecttype'] == 'datetime':
		return datetime.strptime(arg['value'], '%Y-%m-%dT%H:%M:%S')

d = json.loads(j, object_hook=custom_decoder)
# None,   cause the root object when takes place, evaluates that condition to False.

# {'objecttype': 'datetime', 'value': '2018-10-21T09:14:00'}
# {'time': datetime.datetime(2018, 10, 21, 9, 14), 'message': 'created this json string'}
# we alredy got the datetime obj. but the root object evaluates now and returns None


custom_decoder({'objecttype': 'datetime', 'value': '2018-10-01T13:30:45'})
# 2018-10-01 13:30:45, Okay. but what if its not True?
custom_decoder({'a': 1}) 
# None,   it will return None cause we're not specifying the return value
#         to anything else than the datetime object we wrote. 

# to fix that, we just require to return the arg itself.
j = '''
{
	"times": {
		"created": {
			"objecttype": "datetime",
			"value": "2018-10-21T09:14:00"
		},
		"updated": {
			"objecttype": "datetime",
			"value": "2018-10-21T10:00:05"
		}
	},
	"message": "created this json string"
}
'''
def custom_decoder(arg):
	if 'objecttype' in arg and arg['objecttype'] == 'datetime':
		return datetime.strptime(arg['value'], '%Y-%m-%dT%H:%M:%S')
	else:
		return arg  # if the root obj evaluates to False, return as it is.

d = json.loads(j, object_hook=custom_decoder)
# {'message': 'created this json string',
#  'times': {'created': datetime.datetime(2018, 10, 21, 9, 14),
#            'updated': datetime.datetime(2018, 10, 21, 10, 0, 5)}}

# what is nice about this approach, is that, it deal with recursion for us.
# we dont have to worry about where this 
# datetime object is occurying inside json cause it is going to be called for
# every dictionary in that big json dictionary, the root object.

#_______________________________________________________________________________
# extending to deserialize fraction as well.
class Person:
	def __init__(self, name, ssn):
		self.name = name
		self.ssn = ssn
	def __repr__(self) -> str:
		return f'Person({self.name}, {self.ssn})'

def custom_decoder(arg):
	if 'objecttype' in arg:
		if arg['objecttype'] == 'datetime':
			return datetime.strptime(arg['value'], '%Y-%m-%dT%H:%M:%S')
		elif arg['objecttype'] == 'fraction':
			return Fraction(arg['numerator'], arg['denominator'])
		elif arg['objecttype'] == 'person':
			return Person(arg['name'], arg['ssn'])
		return arg
	return arg
# or
def custom_decoder(arg):
	d = arg
	if 'objecttype' in arg:
		if arg['objecttype'] == 'datetime':
			d = datetime.strptime(arg['value'], '%Y-%m-%dT%H:%M:%S')
		elif arg['objecttype'] == 'fraction':
			d = Fraction(arg['numerator'], arg['denominator'])
		elif arg['objecttype'] == 'person':
			d = Person(arg['name'], arg['ssn'])
	return d

j = '''
{
	"cake": "yummy chocolate cake",
	"myShare": {
		"objecttype": "fraction",
		"numerator": 1,
		"denominator": 8
	},
	"eaten": {
		"at": {
			"objecttype": "datetime",
			"value": "2018-12-21T21:30:00"
		},
		"time_taken": "30 seconds"
	}
}
'''
json.loads(j, object_hook=custom_decoder)
# {'cake': 'yummy chocolate cake',
#  'eaten': {'at': datetime.datetime(2018, 12, 21, 21, 30),
#            'time_taken': '30 seconds'},
#  'myShare': Fraction(1, 8)}

j = '''
{
	"accountHolder": {
		"objecttype": "person",
		"name": "Mi ich",
		"ssn": 100
	},
	"created": {
		"objecttype": "datetime",
		"value": "1995-04-20T03:00:00"
	}
}
'''
json.loads(j, object_hook=custom_decoder)
# {'accountHolder': Person(Mi ich, 100),
#  'created': datetime.datetime(1995, 4, 20, 3, 0)}

#_______________________________________________________________________________
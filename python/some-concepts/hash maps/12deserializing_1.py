import json

from pprint import pprint

j = '''
{
	"name": "Python",
	"age": 27,
	"version": ["2.x", "3.x"]
}
'''
json.loads(j)
# {'name': 'Python', 'age': 27, 'version': ['2.x', '3.x']} <class 'dict'>

j = '''
{
	"time": "2018-10-21T09:14:00",
	"message": "created this json string"
}
'''
# python assumes that the time element is supposed to be a string data.
# it could be a datetime object maybe? we dont know.

json.loads(j)  
# {'time': '2018-10-21T09:14:00', 'message': 'created this json string'}


# How can we iterate over the JSON string and know that key should be a datetime object?
# or maybe a Person object... 
# How do we know that we have to re-write that as a custom or standard python object?

#_________________________________________________________________________________________
# we need a specific structure, a schema in JSON. then, we
# manually load up some custom/standard python objects by specific looking for 
# some elements in the JSON string.

# creating a basic schema to identify datetime object
j = '''
{
	"time": {
		"objecttype": "datetime",
		"value": "2018-10-21T09:14:00"
	},
	"message": "created this json string"
}
'''
# now its easier to create the datetime object, its being specified.
# we just require to grab the value and create the datetime object.

# we did not know what "2018-10-21T09:14:00" was before, could be a datetime or anything.
# now we know and can handle this.

json.loads(j)
# {'message': 'created this json string',
#  'time': {'objecttype': 'datetime', 'value': '2018-10-21T09:14:00'}}


#_________________________________________________________________________________________
from datetime import datetime

j = '''
{
	"time": {
		"objecttype": "datetime",
		"value": "2018-10-21T09:14:00"
	},
	"message": "created this json string"
}
'''
# this approach will deals only with the root elements of the json object

d = {}
for key, value in json.loads(j).items():
	if (isinstance(value, dict) 
	    and 'objecttype' in value 
		and value['objecttype'] == 'datetime'
		):
		d[key] = datetime.strptime(value['value'], '%Y-%m-%dT%H:%M:%S')

# json.loads(j).items()  have 2 items in there, "time" and "message".

# key: time
# value: {                           # isinstance(value, dict)?           -> True
# 	'objecttype': 'datetime',        # 'objecttype' in value              -> True
# 	'value': '2018-10-21T09:14:00'   # value['objecttype'] == 'datetime'  -> True
# 	}                                # then: 
# ---------                          # value['value'] give us '2018-10-21T09:14:00'
# key: message
# value: created this json string


# we got our python dict with datetime object in there.
# d = {'time': datetime.datetime(2018, 10, 21, 9, 14)}

#_________________________________________________________________________________________
from fractions import Fraction
# this approach will deals only with the root elements of the json object 
j = '''
{
	"cake": "yummy chocolate cake",
	"myShare": {
		"objecttype": "fraction",
		"numerator": 1,
		"denominator": 8
	}
}
'''
# lets convert that to a Fraction object.
d = json.loads(j)
for key, value in d.items():
	if (isinstance(value, dict) and
		'objecttype' in value and
		value['objecttype'] == 'fraction'
		):
		d[key] = Fraction(value['numerator'], value['denominator'])

# d = {'cake': 'yummy chocolate cake', 'myShare': Fraction(1, 8)}

import json
from json import JSONDecodeError

# we can use jsonschema to validate json objects
from jsonschema import validate
from jsonschema.exceptions import ValidationError

# we were able to do that work with JSONEncoder/Decoder cause we assumed
# we had a schema to work on.

# if we dont have a schema pre-defined, is kinda hard to know what we should
# do with the data we're trying to decode.

# schema is just a standard that allow us to define what properties, what keys,
# are inside a dict, what the object type is, what the value is and other constraints
# that we can add to it.



# creating a json schema
person_schema = {
	"type": "object",
	"properties": {
		"firstName": {"type": "string"},
		"middleInitial": {"type": "string"},
		"lastName": {"type": "string"},
		"age": {"type": "number"}
	}
}

# this json object conform our schema properly
p1 = '''
{
	"firstName": "John",
	"middleInitial": "M",
	"lastName": "Cleese",
	"age": 79
}
'''
validate(json.loads(p1), person_schema)
# None, it is a valid json object

p2 = '''
{
	"firstName": "John",
	"age": -10.5
}
'''
validate(json.loads(p2), person_schema)
# None, it is also valid json object conforming with or schema

p3 = '''
{
	"firstName": "John",
	"middleInitial": "M",
	"lastName": "Cleese",
	"age": "Unknown"
}
'''
# validate(json.loads(p3), person_schema)
# jsonschema.exceptions.ValidationError: 'Unknown' is not of type 'number

# this one doesnt conform with our schema, we have a string where we should have a number

#________________________________________________________________________________________
# improving our schema
person_schema = {
	"type": "object",
	"properties": {
		"firstName": {
			"type": "string",
			"minLength": 1
			},
		"middleInitial": {
			"type": "string",
			"minLength": 1,
			"maxLength": 1
			},
		"lastName": {
			"type": "string",
			"minLength": 1
			},
		"age": {
			"type": "integer",
			"minimum": 0
			},
		"eyeColor": {
			"type": "string",
			"enum": ["amber", "blue", "brown", "gray", "green", "hazel", "violtet"]
		}, # eye color isnt required, but if is specified, must have these values only.
		"address": {
			"type": "object", # we can have nested objects as well with properties
			"properties": {
				"city": {
					"type": "string",
					"minLentght": 1
				}
			}
		}
	},
	"required": ["firstName", "lastName"] # these are required
}
# does these json documents conform with our new schema now?

p1 = '''
{
	"firstName": "John",
	"middleInitial": "M",
	"lastName": "Cleese",
	"age": 79
}
'''
validate(json.loads(p1), person_schema)
# None

p2 = '''
{
	"firstName": "John",
	"age": -10.5
}
''' 
# validate(json.loads(p2), person_schema)
# jsonschema.exceptions.ValidationError: 'lastName' is a required property

p3 = '''
{
	"firstName": "John",
	"middleInitial": "M",
	"lastName": "Cleese",
	"age": "Unknown"
}
'''
# validate(json.loads(p3), person_schema)
# jsonschema.exceptions.ValidationError: 'Unknown' is not of type 'integer'


#______________________________________________________________________________________
# validate() will only raise the first exception that raises.
# if we want, we can get all invalidations at once. we require to use the:
from jsonschema import Draft4Validator

validator = Draft4Validator(person_schema)

for error in validator.iter_errors(json.loads(p1)):
	print(error, end='\n---------------------------------------------\n')
# p1 is a valid json object

# for error in validator.iter_errors(json.loads(p2)):
	# print(error, end='\n---------------------------------------------\n')

# we get all invalidations at once by using it to p2 or p3


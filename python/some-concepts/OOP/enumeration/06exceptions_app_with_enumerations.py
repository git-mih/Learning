# Exceptions application that provides a easy way to generate exceptions.

# raising consistent exception types with associated exception code for each exception, like 
# HTTPStatus does. and we also are going to provide default exception messages.
# at the end, our users can easily list out all the possible exceptions of our app as well.

from enum import Enum, unique

# custom exceptions:
class GenericException(Exception):
    pass

class Timeout(Exception):
    pass


@unique
class AppException(Enum):
    generic = 100, GenericException, 'Application exception.'
    timeout = 101, Timeout, 'Timeout connecting to resource.'
    NotAInteger = 200, ValueError, 'Value must be an integer.'
    NotAList = 201, ValueError, 'Value must be a list.'

    def __new__(cls, code, exception, exc_msg):
        member = object.__new__(cls)
        member._value_ = code        # 101
        member.exception = exception # <class '__main__.Timeout'>
        member.message = exc_msg     # 'Timeout connecting to resource.'
        return member

# looking up for a member object based on his value:
AppException(101)  # AppException.timeout

# raising the custom exception:
try:
    raise AppException.timeout.exception(f'{AppException.timeout.value} - {AppException.timeout.message}')
except Exception as ex:
    ex  # 101 - Timeout connecting to resource.

#____________________________________________________________________________________________________________
# a simpler way of doing that:
@unique
class AppException(Enum):
    generic = 100, GenericException, 'Application exception.'
    timeout = 101, Timeout, 'Timeout connecting to resource.'
    NotAInteger = 200, ValueError, 'Value must be an integer.'
    NotAList = 201, ValueError, 'Value must be a list.'

    def __new__(cls, code, exception, exc_msg):
        member = object.__new__(cls)
        member._value_ = code        # 101
        member.exception = exception # <class '__main__.Timeout'>
        member.message = exc_msg     # 'Timeout connecting to resource.'
        return member
    
    @property
    def code(self):
        return self.value       
    # AppException.timeout.value
    
    def throw(self):
        raise self.exception(f'{self.code} - {self.message}')
    # essentially:
# AppException.timeout.exception(f'AppException.timeout.code - AppException.timeout.message')

try:
    AppException.timeout.throw()
except Exception as ex:
    ex  # 101 - Timeout connecting to resource.

# catching the custom exception instead of 'Exception':
try:
    AppException.timeout.throw()
except Timeout as ex:
    print(ex) # 101 - Timeout connecting to resource.

#____________________________________________________________________________________________________________
# overwriting the default exception message:
@unique
class AppException(Enum):
    generic = 100, GenericException, 'Application exception.'
    timeout = 101, Timeout, 'Timeout connecting to resource.'
    NotAInteger = 200, ValueError, 'Value must be an integer.'
    NotAList = 201, ValueError, 'Value must be a list.'

    def __new__(cls, code, exception, exc_msg):
        member = object.__new__(cls)
        member._value_ = code
        member.exception = exception
        member.message = exc_msg
        return member
    
    @property
    def code(self):
        return self.value       
    
    def throw(self, message=None): 
        message = message or self.message
        raise self.exception(f'{self.code} - {message}')
try:
    AppException.generic.throw('custom message that will override the self.message.')
except GenericException as ex:
    ex  # 100 - custom message that will override the self.message.

#____________________________________________________________________________________________________________
# providing a list with all possible exception that it have:
l = [(exc.name, exc.code, exc.message, exc.exception.__name__) for exc in AppException]
# [('generic', 100, 'Application exception.', 'GenericException'), 
#  ('timeout', 101, 'Timeout connecting to resource.', 'Timeout'), 
#  ('NotAInteger', 200, 'Value must be an integer.', 'ValueError'), 
#  ('NotAList', 201, 'Value must be a list.', 'ValueError')]

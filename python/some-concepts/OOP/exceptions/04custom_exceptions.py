# Custom exceptions

# we can create custom exceptions by simply subclassing any Python exception type.

# we dont usually inherits from BaseException class, but we tipicaly inherits from Exception
# or some subclass of the Exception class:
class TimeoutError(Exception):
    """Timeout exception"""

# this TimeoutError exception doesnt do anything more than any of the standard exceptions in 
# Python. the only thing that we got by doing it is that, we can now trap and handle an 
# specific exception called TimeOutError that our code may raise:
try:
    raise TimeoutError('timeout occurred')
except TimeoutError as ex:
    ex    # timeout occurred

# we can use bare exception handlers to intercept our custom exceptions as well:
import sys
try:
    raise TimeoutError('custom exception error message')
except:
    # getting the current exception instance that is propagating here by using sys module:
    ex_type, ex_msg, ex_tb = sys.exc_info()

# <class '__main__.TimeoutError'>  exception type
# custom exception error message   exception msg
# <traceback object at 0x000001>   exception traceback

#____________________________________________________________________________________________________
# we dont have to inherit from Exception tho, we can create exceptions that inherits from any
# subclass of BaseException itself.
class ReadOnlyError(AttributeError):
    """indicates that an attribute is read-only"""
try:
    raise ReadOnlyError('account number is read-only', 'BA10001')
except ReadOnlyError as ex:
    repr(ex)   # ReadOnlyError('account number is read-only', 'BA10001')

# ReadOnlyError inherits from AttributeError, so we can actually handle AttributeError in general:
try:
    raise ReadOnlyError('account number is read-only', 'BA10001')
except AttributeError as ex:
    repr(ex)   # ReadOnlyError('account number is read-only', 'BA10001')

# in fact, we could go all way back until the BaseException class and get the same thing:
try:
    raise ReadOnlyError('account number is read-only', 'BA10001')
except BaseException as ex:
    repr(ex)   # ReadOnlyError('account number is read-only', 'BA10001')

#____________________________________________________________________________________________________
# whenever that we have an relatively complex application, we often creates our own exception
# hierarchy:
class WebScrapperException(Exception):
    pass
class HTTPException(WebScrapperException):
    pass
class InvalidURLException(HTTPException):
    pass
class TimeoutException(HTTPException): 
    pass
class PingTimeoutException(TimeoutException):
    pass
class LoadTimeoutException(TimeoutError):
    pass
class ParserException(WebScrapperException):
    pass

# WebScrapperException
#   +-- HTTPException
#   |      +-- InvalidURLException
#   |      +-- TimeoutError
#   |             +-- PingTimeoutException
#   |             +-- LoadTimeoutException
#   +-- ParserException

#____________________________________________________________________________________________________
# custom exceptions are just classes, we can add our own custom attributes, properties, methods
# and overwrite dunder methods as well.

# this might be useful to provide additional context or functionalities to our esceptions:
from http import HTTPStatus
import json
from datetime import datetime


# our custom base exception class:
class APIException(Exception):
    http_status = HTTPStatus.INTERNAL_SERVER_ERROR
    internal_err_msg = 'API exception occurred.'
    user_err_msg = 'we are sorry, an unexpected error occurred on our end.'

    def __init__(self, *args, user_err_msg=None):
        if args:
            self.internal_err_msg = args[0]
            super().__init__(*args)
        else:
            super().__init__(self.internal_err_msg)

        if user_err_msg is not None:
            self.user_err_msg = user_err_msg

    def to_json(self):
        err_object = {'stauts': self.http_status, 'message': self.user_err_msg}
        return json.dumps(err_object) # returning JSON object to the user.
    
    def log_exception(self):
        # creating a dictionary with all information about the exception:
        exception = {
            "type": type(self).__name__,
            "http_status": self.http_status,
            "message": self.args[0] if self.args else self.internal_err_msg,
            "args": self.args[1:]
        }
        # returning our exception:
        return f'EXCEPTION: {datetime.utcnow().isoformat()}: {exception}'

# custom exceptions that will inherits from our APIException class:
class ApplicationException(APIException):
    http_status = HTTPStatus.INTERNAL_SERVER_ERROR
    internal_err_msg = 'Generic server side exception'       # log_exception
    user_err_msg = 'we sorry, an unexpected error occurred.' # to_json

class DBException(ApplicationException):
    http_status = HTTPStatus.INTERNAL_SERVER_ERROR
    internal_err_msg = 'Database exception'
    user_err_msg = 'we sorry, an unexpected error occurred.'

class DBConnectionError(DBException):
    http_status = HTTPStatus.INTERNAL_SERVER_ERROR
    internal_err_msg = 'Database connection exception'
    user_err_msg = 'we sorry, an unexpected error occurred.'

class ClientException(APIException):
    http_status = HTTPStatus.BAD_REQUEST
    internal_err_msg = 'Client submitted bad request'
    user_err_msg = 'bad request was received'

class NotFoundError(ClientException):
    http_status = HTTPStatus.NOT_FOUND
    internal_err_msg = 'Resource not found'
    user_err_msg = 'requested resource was not found'

class NotAuthorizedError(ClientException):
    http_status = HTTPStatus.UNAUTHORIZED
    internal_err_msg = 'Client not authorized to perform operation'
    user_err_msg = 'you are not authorized to perform this request'



class Account:
    def __init__(self, account_id, account_type):
        self.account_id = account_id
        self.account_type = account_type


def lookup_account_by_id(account_id):
    if not isinstance(account_id, int) or account_id <= 0:
        raise ClientException(f'account number {account_id} is invalid.',
                              f'account_id = {account_id}',
                              'type error - account number not an integer')
    if account_id < 100:
        raise DBConnectionError('permanent failure connecting to db.', 'db=db01')
    elif account_id < 200:
        raise NotAuthorizedError('user doesnt have permissions to read this account.', 
                                 f'account_id = {account_id}')
    elif account_id < 300:
        raise NotFoundError('account not found', f'account_id = {account_id}')
    else:
        # if account_id is greater than 300, we create and return the Account object instance:
        return Account(account_id, 'Savings')

def get_account(account_id):
    try:
        account = lookup_account_by_id(account_id)
    except APIException as ex:
         print(ex.log_exception()) 
         print(ex.to_json())
    else:
        # if Account was created succesfully, we just send the JSON object to the user:
        return HTTPStatus.OK, {'id': account.account_id, 'type': account.account_type}

get_account('abc')
# EXCEPTION: 2021-08-08T04:49:30.455391: {'type': 'ClientException', 
#                                         'http_status': <HTTPStatus.BAD_REQUEST: 400>, 
#                                         'message': 'account number abc is invalid.', 
#                                         'args': ('account_id = abc', 'type error - account number not an integer')}
# {"stauts": 400, "message": "a bad request was received"}

get_account(50)
# EXCEPTION: 2021-08-08T04:50:26.633598: {'type': 'DBConnectionError', 
#                                         'http_status': <HTTPStatus.INTERNAL_SERVER_ERROR: 500>, 
#                                         'message': 'permanent failure connecting to db.', 
#                                         'args': ('db=db01',)}
# {"stauts": 500, "message": "we are sorry, an unexpected error occurred on our end."}

get_account(150)
# EXCEPTION: 2021-08-08T04:51:11.387319: {'type': 'NotAuthorizedError', 
#                                         'http_status': <HTTPStatus.UNAUTHORIZED: 401>, 
#                                         'message': 'user doesnt have permissions to read this account.', 
#                                         'args': ('account_id = 150',)}
# {"stauts": 401, "message": "youre not authorized to perform this request"}

get_account(250)
# EXCEPTION: 2021-08-08T04:51:44.861158: {'type': 'NotFoundError', 
#                                         'http_status': <HTTPStatus.NOT_FOUND: 404>, 
#                                         'message': 'account not found', 
#                                         'args': ('account_id = 250',)}
# {"stauts": 404, "message": "requested resource was not found"}

get_account(350) # (<HTTPStatus.OK: 200>, {'id': 350, 'type': 'Savings'})

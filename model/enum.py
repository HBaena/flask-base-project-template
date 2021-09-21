class StatusMsg():
    OK = 'ok'
    FAIL = 'fail'

class ErrorMsg():
    DB_ERROR = 'db_error'
    VALUES_REQUIRED = 'all_values_are_required'
    MISSING_VALUES = 'missing_values'
    WRONG_PASSWORD = 'wrong_password'
    ROUTE_ERROR = 'endpoint_error'
    NEEDED_VALUES = '[{}] need value(s)'
    UNKNOWN_ERROR = 'unknown_error'
    AUTH_ERROR = 'authorization_error'

class AuthError():
    EXPIRED_TOKEN = 'Token expired, try to get another one using refresh token'
    INVALID_TOKEN = 'Token invalid, try to get another one using refresh token'
    UNAUTHORIZED = 'Missing Authorization header'

class RouteErrorMsg():
    ARG_ERROR = 'endpoint_argument_unexpected'


class DBErrorMsg():
    USER_EXISTS = 'user_already_exists'
    USER_NOT_EXISTS = 'user_not_exists'
    CREATING_ERROR = 'error_writing_db'
    READING_ERROR = 'error_reading_db'
    CONNECTION_ERROR = 'error_with_db_connection'
    ID_ERROR = 'id_not_exists_in_db'
    NO_EXISTS_INFO = 'no_exists_info'

class SuccessMsg():
    SENT = 'sent_message'
    CREATED = 'created_successfully'
    READED = 'read_successfully'
    UPDATED = 'updated_successfully'
    DELETED = 'deleted_successfully'
    FOUND = 'coincidences_found'
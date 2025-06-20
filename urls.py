class Url:
    BASE_URL = 'https://stellarburgers.nomoreparties.site'
    CREATE_USER = '/api/auth/register' #POST
    LOGIN_USER = '/api/auth/login' #POST
    CHANGE_USER_DATA = '/api/auth/user' #PATCH
    CREATE_ORDER = '/api/orders' #POST
    GET_USER_ORDERS = '/api/orders' #GET
    DELETE_USER = '/api/auth/user' #DELETE
    GET_TOKEN_USER = '/api/auth/token' #POST
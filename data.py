class DataForUser:
    CREATE_USER_BODY = {
    "email": "test-data@yandex.ru",
    "password": "password",
    "name": "Username"
    }
class MessageAnswer:
    ERR_WITHOUT_NAME = "Email, password and name are required fields"
    ERR_INCORRECT_DATA = 'email or password are incorrect'
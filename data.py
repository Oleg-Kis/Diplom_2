from faker import Faker

fake = Faker()

class DataForUser:
    CREATE_USER_BODY = {
    "email": "test-data@yandex.ru",
    "password": "password",
    "name": "Username"
    }

class MessageAnswer:
    ERR_WITHOUT_NAME = "Email, password and name are required fields"
    ERR_INCORRECT_DATA = 'email or password are incorrect'
    ERR_NOT_AUTH = 'You should be authorised'


class DataIngredients:
    VALID_INGREDIENTS = {
    "ingredients": ["61c0c5a71d1f82001bdaaa6d","61c0c5a71d1f82001bdaaa6f"]
    }

    NOT_VALID_INGREDIENTS = {
    "ingredients": ["61c0c5a71d1f82001bdaaa6","61c0c5a71d1f82001bdaaa6"]
    }

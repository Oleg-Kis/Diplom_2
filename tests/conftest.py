import pytest

from generators import generate_user_body
from methods.user_methods import UserMethods


@pytest.fixture
def generate_user_data():
    user_body = generate_user_body()
    email = user_body["email"]
    password = user_body["password"]
    name = user_body["name"]
    yield [user_body, email, password, name]
    access_token = UserMethods.get_user_access_token(email, password)
    UserMethods.delete_user(access_token)

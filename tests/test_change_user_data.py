import allure
import pytest

import data
import generators
from methods.user_methods import UserMethods


class TestChangeUserData:
    @allure.title("Изменение данных авторизированного пользователя")
    @pytest.mark.parametrize('key, value', generators.UserDataForChange.DATA_CHANGE)
    def test_change_auth_user_data(self, generate_user_data, key, value):
        with allure.step('Создаем пользователя'):
            UserMethods.create_user(generate_user_data[0])
        with allure.step('Авторизация и получение токена'):
            access_token = UserMethods.get_user_access_token(generate_user_data[1], generate_user_data[2])
        with allure.step('Изменение данных пользователя'):
            change_data = generate_user_data[0].copy()
            change_data[key] = value
            change_response = UserMethods.change_user_data(access_token, change_data)
            assert change_response.status_code == 200 and change_response.json()["success"] == True

    @allure.title("Изменение пароля неавторизированного пользователя")
    def test_change_not_auth_user_data(self, generate_user_data):
        with allure.step('Создаем пользователя и получаем токен'):
            access_token = UserMethods.create_user(generate_user_data[0]).json().get("accessToken")
        with allure.step('Изменение данных пользователя'):
            change_data = generate_user_data[0].copy()
            change_data['password'] = 'repassword'
            change_response = UserMethods.change_user_data(access_token, change_data)
            assert change_response.status_code == 200 and change_response.json()["success"] == True

    @allure.title("Изменение именя неавторизированного пользователя")
    def test_change_not_auth_user_data(self, generate_user_data):
        with allure.step('Создаем пользователя и получаем токен'):
            access_token = UserMethods.create_user(generate_user_data[0]).json().get("accessToken")
        with allure.step('Изменение данных пользователя'):
            change_data = generate_user_data[0].copy()
            change_data['name'] = 'rename'
            change_response = UserMethods.change_user_data(access_token, change_data)
            assert change_response.status_code == 200 and change_response.json()["success"] == True

    @allure.title("Изменение почты неавторизированного пользователя")
    def test_change_not_auth_user_data(self, generate_user_data):
        with allure.step('Создаем пользователя и получаем токен'):
            access_token = UserMethods.create_user(generate_user_data[0]).json().get("accessToken")
        with allure.step('Изменение данных пользователя'):
            change_data = generate_user_data[0].copy()
            change_data['email'] = data.FakeEmailNotAuth()
            change_response = UserMethods.change_user_data(access_token, change_data)
            assert change_response.status_code == 200 and change_response.json()["success"] == True
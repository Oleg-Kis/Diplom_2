import allure

from data import MessageAnswer
from methods.user_methods import UserMethods


class TestLoginUser:
    @allure.title("Логин пользователя с валидными данными")
    def test_login_user_valid_data(self, generate_user_data):
        with allure.step('Создаем пользователя'):
            user = UserMethods.create_user(generate_user_data[0])
        with allure.step('Авторизация пользователя'):
            login_user = UserMethods.login_user(generate_user_data)
        assert user.status_code == 200
        assert login_user.status_code == 200 and login_user.json()["success"] == True

    @allure.title("Логин пользователя с неверным паролем")
    def test_login_user_incorrect_password(self, generate_user_data):
        with allure.step('Создаем пользователя'):
            user = UserMethods.create_user(generate_user_data[0])
        with allure.step('Авторизация пользователя с неверным паролем'):
            user_log = UserMethods.login_user_incorrect_password(generate_user_data)
        assert user.status_code == 200
        assert user_log.status_code == 401 and user_log.json()["message"] == MessageAnswer.ERR_INCORRECT_DATA

    @allure.title("Логин пользователя с неверным логином")
    def test_login_user_incorrect_email(self, generate_user_data):
        with allure.step('Создаем пользователя'):
            user = UserMethods.create_user(generate_user_data[0])
        with allure.step('Авторизация пользователя с неверным логином'):
            user_log = UserMethods.login_user_incorrect_email(generate_user_data)
        assert user.status_code == 200
        assert user_log.status_code == 401 and user_log.json()["message"] == MessageAnswer.ERR_INCORRECT_DATA
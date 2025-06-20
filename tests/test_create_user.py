import allure

from data import MessageAnswer
from methods.user_methods import UserMethods

class TestCreateUser:
    @allure.title("Создание пользователя с валидными данными")
    def test_create_user_all_valid_data(self, generate_user_data):
        with allure.step('Создаем пользователя'):
            user = UserMethods.create_user(generate_user_data[0])
            assert user.status_code == 200 and user.json()["success"] == True

    @allure.title("Создание двух одинаковых пользователей")
    def test_create_two_identical_users(self, generate_user_data):
        with allure.step('Создаем первого пользователя'):
            user_one = UserMethods.create_user(generate_user_data[0])
        with allure.step('Создаем второго пользователя с аналогичными данными'):
            user_two = UserMethods.create_user(generate_user_data[0])
        assert user_one.status_code == 200 and user_two.status_code == 403

    @allure.title("Создание пользователя без поля Имя")
    def test_not_create_user_without_name(self, generate_user_data):
        with allure.step('Создаем тело запроса без пол Имя'):
            courier = UserMethods.create_user_without_name(generate_user_data)
        assert courier.status_code == 403 and courier.json()["message"] == MessageAnswer.ERR_WITHOUT_NAME
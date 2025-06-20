import allure

from methods.user_methods import UserMethods


class TestCreateUser:
    @allure.title("Создание пользователя с валидными данными")
    def test_create_user_all_valid_data(self, generate_user_data):
        with allure.step('Создаем пользователя'):
            user = UserMethods.create_user(generate_user_data[0])
            assert user.status_code == 200 and user.json()["success"] == True
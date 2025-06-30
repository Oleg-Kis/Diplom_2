import allure

from data import DataIngredients
from methods.order_methods import OrderMethods
from methods.user_methods import UserMethods


class TestCreateOrder:
    @allure.title("Создание заказа авторизированного пользователя")
    def test_create_order_auth_user(self, generate_user_data):
        with allure.step('Создаем пользователя'):
            UserMethods.create_user(generate_user_data[0])
        with allure.step('Авторизация пользователя и получение токена'):
            access_token = UserMethods.get_user_access_token(generate_user_data[1], generate_user_data[2])
        with allure.step('Создаем заказ'):
            ingredients = DataIngredients.VALID_INGREDIENTS
            order = OrderMethods.create_order(access_token, ingredients)
            assert order.status_code == 200 and order.json()["success"] == True

    @allure.title("Создание заказа неавторизированного пользователя")
    def test_create_order_not_auth_user(self, generate_user_data):
        with allure.step('Создаем пользователя и получаем токен'):
            access_token = UserMethods.create_user(generate_user_data[0]).json().get("accessToken")
        with allure.step('Создаем заказ'):
            ingredients = DataIngredients.VALID_INGREDIENTS
            order = OrderMethods.create_order(access_token, ingredients)
            assert order.status_code == 200 and order.json()["success"] == True

    @allure.title("Создание заказа авторизированного пользователя без ингредиентов")
    def test_create_order_without_ingredients(self, generate_user_data):
        with allure.step('Создаем пользователя'):
            UserMethods.create_user(generate_user_data[0])
        with allure.step('Авторизация пользователя и получение токена'):
            access_token = UserMethods.get_user_access_token(generate_user_data[1], generate_user_data[2])
        with allure.step('Создаем заказ'):
            ingredients = {"ingredients": []}
            order = OrderMethods.create_order(access_token, ingredients)
            assert order.status_code == 400 and order.json()["success"] == False

    @allure.title("Создание заказа авторизированного пользователя с неверным хешем ингредиентов")
    def test_create_order_without_ingredients(self, generate_user_data):
        with allure.step('Создаем пользователя'):
            UserMethods.create_user(generate_user_data[0])
        with allure.step('Авторизация пользователя и получение токена'):
            access_token = UserMethods.get_user_access_token(generate_user_data[1], generate_user_data[2])
        with allure.step('Создаем заказ'):
            ingredients = DataIngredients.NOT_VALID_INGREDIENTS
            order = OrderMethods.create_order(access_token, ingredients)
            assert order.status_code == 500

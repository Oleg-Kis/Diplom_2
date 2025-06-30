import allure

from data import DataIngredients
from methods.order_methods import OrderMethods
from methods.user_methods import UserMethods


class TestGetUserOrders:
    @allure.title("Получение заказов авторизированного пользователя")
    def test_get_orders_auth_user(self, generate_user_data):
        with allure.step('Создаем пользователя'):
            UserMethods.create_user(generate_user_data[0])
        with allure.step('Авторизация пользователя и получение токена'):
            access_token = UserMethods.get_user_access_token(generate_user_data[1], generate_user_data[2])
        with allure.step('Создаем заказ'):
            ingredients = DataIngredients.VALID_INGREDIENTS
            OrderMethods.create_order(access_token, ingredients)
        with allure.step('Получаем список заказов'):
            orders = OrderMethods.get_orders_auth_user(access_token)
            assert orders.status_code == 200 and orders.json()["success"] == True and type(orders.json()["orders"]) == list

    @allure.title("Получение заказов неавторизированного пользователя")
    def test_get_orders_not_auth_user(self, generate_user_data):
        with allure.step('Создаем пользователя и получаем токен'):
            access_token = UserMethods.create_user(generate_user_data[0]).json().get("accessToken")
        with allure.step('Создаем заказ'):
            ingredients = DataIngredients.VALID_INGREDIENTS
            OrderMethods.create_order(access_token, ingredients)
        with allure.step('Получаем список заказов'):
            orders = OrderMethods.get_orders_auth_user(access_token)
            assert orders.status_code == 200 and orders.json()["success"] == True and type(orders.json()["orders"]) == list

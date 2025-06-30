import requests

from urls import Url


class OrderMethods:
    @staticmethod
    def create_order(access_token, body):
        headers = {"Authorization": access_token}
        params = body
        response = requests.post(f'{Url.BASE_URL}{Url.CREATE_ORDER}', headers=headers, data=params)
        return response

    @staticmethod
    def get_orders_auth_user(access_token):
        headers = {"Authorization": access_token}
        response = requests.get(f'{Url.BASE_URL}{Url.GET_USER_ORDERS}', headers=headers)
        return response

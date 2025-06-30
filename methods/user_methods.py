import requests

from urls import Url


class UserMethods:
    @staticmethod
    def create_user(body):
        response = requests.post(f'{Url.BASE_URL}{Url.CREATE_USER}', json=body)
        return response

    @staticmethod
    def create_user_without_name(body):
        email = (body[1])
        password = (body[2])
        params = {"email": email, "password": password}
        response = requests.post(f'{Url.BASE_URL}{Url.CREATE_USER}', params=params)
        return response

    @staticmethod
    def login_user(body):
        email = (body[1])
        password = (body[2])
        params = {'email': email, 'password': password}
        response = requests.post(f'{Url.BASE_URL}{Url.LOGIN_USER}', data=params)
        return response

    @staticmethod
    def login_user_incorrect_password(body):
        email = (body[1])
        password = (body[2])
        params = {'email': email, 'password': password + 'a'}
        response = requests.post(f'{Url.BASE_URL}{Url.LOGIN_USER}', data=params)
        return response

    @staticmethod
    def login_user_incorrect_email(body):
        email = (body[1])
        password = (body[2])
        params = {'email': email + 'a', 'password': password}
        response = requests.post(f'{Url.BASE_URL}{Url.LOGIN_USER}', data=params)
        return response

    @staticmethod
    def delete_user(access_token):
        headers = {"Authorization": access_token}
        response = requests.delete(f'{Url.BASE_URL}{Url.DELETE_USER}', headers=headers)
        return response

    @staticmethod
    def get_user_access_token(email, password):
        params = {'email': email, 'password': password}
        response = requests.post(f'{Url.BASE_URL}{Url.LOGIN_USER}', data=params)
        access_token = response.json().get("accessToken")
        return access_token

    @staticmethod
    def change_user_data(access_token, new_data):
        headers = {"Authorization": access_token}
        response = requests.patch(f'{Url.BASE_URL}{Url.CHANGE_USER_DATA}', headers=headers, data=new_data)
        return response

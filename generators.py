from faker import Faker

fake = Faker()

def generate_user_body():
    return {
        "email": fake.email(),
        "password": fake.word(),
        "name": fake.word()
    }

class UserDataForChange:
    DATA_CHANGE = [
        ["email", fake.email()],
        ["password", fake.word()],
        ["name", fake.word()]
    ]

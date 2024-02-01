from faker import Faker


def generate_user_data():
    user_data = {
        "email": Faker().email(),
        "password": Faker().password(),
        "name": Faker().first_name()
    }
    return user_data

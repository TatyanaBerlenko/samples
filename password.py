import random
import string


class User:
    def __init__(self, name) -> None:
        self.name = name
        self.password = get_password()

    def __str__(self) -> str:
        return 'Name: {}, Password: {}'.format(self.name, self.password)


def get_password(pass_len=6):
    digits = string.digits
    letters = string.ascii_lowercase
    password = ''
    for i in range(pass_len):
        is_digit = random.random()
        if is_digit < 0.5:
            password += random.choice(digits)
        else:
            password += random.choice(letters)
    return password


user_1 = User('Alex')
user_2 = User('Marya')
user_3 = User('Katy')
print(user_1)
print(user_2)
print(user_3)

import string
import random


class PasswordGenerator:

    types = {
        1: string.digits,
        2: string.ascii_lowercase,
        3: string.ascii_uppercase,
        4: string.ascii_letters,
        5: string.ascii_letters + string.digits,
        6: string.ascii_letters + string.digits + string.punctuation
    }

    def __init__(self, length, password_type):
        self.length = length
        self.password_type = password_type

    def generate_password(self):
        password_symbols = PasswordGenerator.types[self.password_type]
        random_password = ''.join(random.choice(password_symbols) for _ in range(self.length))
        return random_password


if __name__ == '__main__':

    types = {
        1: '1. Digits only',
        2: '2. Lowercase letters only',
        3: '3. Uppercase letters only',
        4: '4. Uppercase and lowercase letters',
        5: '5. Uppercase and lowercase letters and digits',
        6: '6. Uppercase and lowercase letters, digits and special symbols'
    }

    for password_type in sorted(types.values()):
        print(password_type)

    password_type = int(input('Choose your password policy: '))
    length = int(input('Print password length: '))

    password_generator = PasswordGenerator(length, password_type)
    print(password_generator.generate_password())



import string
import random


class PasswordGenerator:

    def __init__(self, size):
        self.size = size

    def generate_password(self):
        specific_symbols_count = self.size // 6 + 1
        digits_count = self.size // 4
        uppercase_count = (self.size - specific_symbols_count - digits_count) // 2
        lowercase_count = self.size - uppercase_count - specific_symbols_count - digits_count

        password_symbols = [random.choice(string.punctuation) for _ in range(specific_symbols_count)]
        password_symbols.extend([random.choice(string.digits) for _ in range(digits_count)])
        password_symbols.extend([random.choice(string.ascii_uppercase) for _ in range(uppercase_count)])
        password_symbols.extend([random.choice(string.ascii_lowercase) for _ in range(lowercase_count)])

        random.shuffle(password_symbols)

        return ''.join(password_symbols)


if __name__ == '__main__':

    length = int(input('Print password length: '))

    password_generator = PasswordGenerator(length)
    print(password_generator.generate_password())



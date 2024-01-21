class PasswordGenerator:

    types = {
        1: '1. Digits only',
        2: '2. Lowercase letters only',
        3: '3. Uppercase letters only',
        4: '4. Uppercase and lowercase letters',
        5: '5. Uppercase and lowercase letters and digits',
        6: '6. Uppercase and lowercase letters, digits and special symbols'
    }

    def __init__(self, length, type):
        self.length = length
        self.type = type

    def generate_passwords(self):
        return 'dumbpassword'

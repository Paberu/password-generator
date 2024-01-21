import unittest

from PasswordGenerator import PasswordGenerator


class TestGenerator(unittest.TestCase):

    def testInit(self):
        self.assertTrue(PasswordGenerator(length=5, password_type=1))

    def testGenerate(self):
        pass_gen = PasswordGenerator(length=5, password_type=1)
        password = pass_gen.generate_password()
        print(password)
        self.assertEqual(len(password), 5)


unittest.main()

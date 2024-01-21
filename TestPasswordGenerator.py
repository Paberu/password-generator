import unittest

from PasswordGenerator import PasswordGenerator


class TestGenerator(unittest.TestCase):

    def testInit(self):
        self.assertTrue(PasswordGenerator(length=5, type=1))


unittest.main()

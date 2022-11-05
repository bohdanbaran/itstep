import unittest
from main import *

def adder(*args, **kwargs):
    result = 0
    for _ in args:
        result += _
    for _ in kwargs.values():
        result += _
    return result


class My_Test(unittest.TestCase):
    def test_args(self):
        self.assertEqual(adder(2, 2), 4)


if __name__ == "__main__":
    unittest.main()




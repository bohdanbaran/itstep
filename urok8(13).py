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
        self.assertEqual(adder(2,2), 4)
    def test_kwargs(self):
        self.assertEqual(adder(a=10, b=11), 21)
    def test_mixed(self):
        self.assertEqual(adder(1, a=2), 3)



if __name__ == "__main__":
    unittest.main()




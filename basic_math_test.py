import unittest
import basic_math


# TODO add more unit tests to get full code coverage
class TestingAddingOne(unittest.TestCase):
    def test_adding_one_skeleton(self):
        var1 = 1
        a = basic_math.adding_one(var1)
        b = var1 + 1
        self.assertEqual(a, b)


class TestingAdding(unittest.TestCase):
    def testing_adding_skeleton(self):
        var1 = 2
        var2 = 4
        a = basic_math.adding(var1, var2)
        b = var1 + var2
        self.assertEqual(a, b)


class TestingSubtraction(unittest.TestCase):
    def testing_subtraction_skeleton(self):
        var1 = 4
        var2 = 2
        a = basic_math.subtraction(var1, var2)
        b = var1 - var2
        self.assertEqual(a, b)


class TestingDivision(unittest.TestCase):
    def testing_division_skeleton(self):
        var1 = 5
        var2 = 2
        a = basic_math.integer_divide(var1, var2)
        b = var1 // var2
        self.assertEqual(a, b)


class TestingRemainder(unittest.TestCase):
    def testing_remainder_skeleton(self):
        var1 = 5
        var2 = 2
        a = basic_math.remainder(var1, var2)
        b = var1 % var2
        self.assertEqual(a, b)


class TestingPower(unittest.TestCase):
    def testing_power_skeleton(self):
        var1 = 5
        var2 = 3
        a = basic_math.power(var1, var2)
        b = var1 ** var2
        self.assertEqual(a, b)


class TestingRoot(unittest.TestCase):
    def testing_root_skeleton(self):
        var1 = 10
        var2 = 2
        a = basic_math.root(var1, var2)
        b = 3
        self.assertEqual(a, b)


if __name__ == '__main__':
    unittest.main()

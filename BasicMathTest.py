import unittest
import BasicMath


class MyTestCase(unittest.TestCase):
    def skeleton_test_adding_one(self):
        self.assert_(BasicMath.adding_one(1), 3)

    def skeleton_test_adding(self):
        self.assertEqual(BasicMath.adding(2, 4), 5)

    def test_something(self):
        self.assertEqual(True, True)


if __name__ == '__main__':
    unittest.main()

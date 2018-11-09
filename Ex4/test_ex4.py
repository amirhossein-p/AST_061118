import unittest
import numpy as np
import ex4

class testCase(unittest.TestCase):

    def testCalcArea(self):
        self.assertEqual(ex4.Circle(2).CalcArea(2),([3.00, 3.10, 3.14], [3.226, 1.274]))

    def testCalcCircumference(self):
        self.assertEqual(ex4.Circle(2).CalcCircumference(2),([6.00, 6.20, 6.28], [3.226, 1.274]))

if __name__ == '__main__':
    unittest.main()

import unittest
import numpy as np
import ex1

class testCase(unittest.TestCase):
    """Tests for `isTest.py`."""
    def test_calcSum(self):
        self.assertEqual(ex1.calcSum([1,2,3,4,5]), 1+2+3+4+5)

    def test_calcProduct(self):
        self.assertEqual(ex1.calcProduct([1,2,3,4,5]), 1*2*3*4*5)

    def test_calcAverage(self):
        self.assertEqual(ex1.calcAverage([1,2,3,4,5]), (1+2+3+4+5)/5)

    def test_calcVariance(self):
        self.assertEqual(ex1.calcVariance([1,2,3,4,5]), np.var([1,2,3,4,5]))

    def test_calcMin(self):
        self.assertEqual(ex1.calcMin([1,2,3,4,5]), 1)

    def test_calcMax(self):
        self.assertEqual(ex1.calcMax([1,2,3,4,5]), 5)

if __name__ == '__main__':
    unittest.main()

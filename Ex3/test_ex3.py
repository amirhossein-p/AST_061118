import unittest
import numpy as np
import ex3

class testCase(unittest.TestCase):
    """Tests for `isTest.py`."""
    def test_fn1(self):
        self.assertEqual(ex3.fn1(2),["0","2"]) #2n

    def test_fn2(self):
        self.assertEqual(ex3.fn2(2),["0.0000","1.0000"]) #n^1/2 in 4 decimal points
    

    def test_fn3(self):
        self.assertEqual(ex3.fn3(2),["1.00E+00","1.00E+01"]) #10^n in scientific notation to 2 decimal points

    def test_fn4(self):
        self.assertEqual(ex3.fn4(2),["0","1"]) #n^3

    def test_fn5(self):
        self.assertEqual(ex3.fn5(2),["None","2.0000"]) #2^(1/n) in 4 decimal points


    def test_fn6(self):
        self.assertEqual(ex3.fn6(2),["1.00E+00","2.72E+00"]) #e^(n) in scientific notation to 2 decimal points

if __name__ == '__main__':
    unittest.main()

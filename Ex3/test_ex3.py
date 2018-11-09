import unittest
import numpy as np
import ex3

class testCase(unittest.TestCase):
    """Tests for `isTest.py`."""
    def test_fn1(self):
        self.assertEqual(ex3.fn1(2),[0,2,4])

    def test_fn2(self):
        self.assertEqual(ex3.fn2(2),[0,1,1.41421356237])
    

    def test_fn3(self):
        self.assertEqual(ex3.fn3(2),[1,10,100])

    def test_fn4(self):
        self.assertEqual(ex3.fn4(2),[0,1,8])

    def test_fn5(self):
        self.assertEqual(ex3.fn5(2),[0,1,8])


    def test_fn4(self):
        self.assertEqual(ex3.fn4(2),[1,10,100])

if __name__ == '__main__':
    unittest.main()

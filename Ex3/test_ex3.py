import unittest
import ex3

class testCase(unittest.TestCase):

    def test_fn1(self):
        self.assertEqual(ex3.fn1(5), [0,2,4,6,8])


if __name__ == '__main__':
    unittest.main()

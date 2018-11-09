import unittest
from isTest import isEqual

class isEqualTestCase(unittest.TestCase):
    """Tests for `isTest.py`."""

    def test_is_2_and_2_equal(self):
        # """Is five successfully determined to be prime?"""
        self.assertTrue(not isEqual(2,3))
        self.assertTrue(isEqual(2,2))


if __name__ == '__main__':
    unittest.main()

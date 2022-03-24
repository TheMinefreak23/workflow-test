"""
Mock docstring
"""
import unittest

from mock import mock

class TestMock(unittest.TestCase):
    """Mock doc"""
    def test_mock(self):
        """Mock doc"""
        self.assertEqual(mock.mock_func(2), 4)

if __name__ == '__main__':
    unittest.main()

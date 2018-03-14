
import sys
import unittest

class TestSmoke(unittest.TestCase):
    def test_python(self):
        self.assertTrue(sys.version >= "2.7.10")

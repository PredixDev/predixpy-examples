
import sys
import unittest

class TestDependency(unittest.TestCase):
    def test_python(self):
        self.assertTrue(sys.version >= "2.7.10")

from unittest import TestCase
from code import SomeCode


class TestCode(TestCase):
    def test_code(self):
        self.assertEqual(SomeCode().do_something(), 7)

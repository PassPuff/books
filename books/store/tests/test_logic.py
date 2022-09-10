from unittest import TestCase

from store.logic import operations


class LogicTestCase(TestCase):
    def test_plus(self):
        result = operations(6, 13, '+')
        self.assertEqual(19, result)

    def test_minus(self):
        result = operations(22, 14, '-')
        self.assertEqual(8, result)

    def test_multiply(self):
        result = operations(20, 13, '*')
        self.assertEqual(260, result)

    def test_division(self):
        result = operations(420, 2, '/')
        self.assertEqual(210, result)
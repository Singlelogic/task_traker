import unittest
from views.commands import validate_date


class TestViews(unittest.TestCase):
    def test_validate_date(self):
        self.assertTrue(validate_date("2020-09-30"))
        self.assertTrue(validate_date("2019-10-31"))
        self.assertTrue(validate_date("2019-12-01"))
        self.assertTrue(validate_date("2001-01-01"))
        self.assertTrue(validate_date("0001-01-01"))
        self.assertFalse(validate_date("2020-13-01"))
        self.assertFalse(validate_date("2020-12-32"))
        self.assertFalse(validate_date("2020-12"))
        self.assertFalse(validate_date("2020"))
        self.assertFalse(validate_date("hello"))
        self.assertFalse(validate_date(""))

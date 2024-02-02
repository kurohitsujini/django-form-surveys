from django.test import TestCase
from django.core.exceptions import ValidationError
from djf_surveys.validators import validate_rating


class ValidationForm(TestCase):
    def test_validate_rating(self):
        with self.assertRaises(ValidationError):
            validate_rating(0, 10)

        with self.assertRaises(ValidationError):
            validate_rating(100, 10)

        validate_rating(2,5)

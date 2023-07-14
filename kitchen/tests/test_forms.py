from django.test import TestCase

from kitchen.forms import (
    DishSearchForm,
    DishTypeSearchForm,
    CookExperienceUpdateForm,
)


class FormTest(TestCase):
    @staticmethod
    def create_form(years_of_experience):
        return CookExperienceUpdateForm(data={"years_of_experience": years_of_experience})

    def test_years_of_experience_is_valid(self):
        self.assertTrue(self.create_form(3).is_valid())

    def test_years_of_experience_is_not_valid(self):
        self.assertFalse(self.create_form("A").is_valid())

    def test_dish_search_form(self):
        form_data = {"name": "test"}
        form = DishSearchForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_dish_type_search_form(self):
        form_data = {"dish_type": "Drinks"}
        form = DishTypeSearchForm(data=form_data)
        self.assertTrue(form.is_valid())

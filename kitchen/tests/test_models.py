from django.contrib.auth import get_user_model
from django.test import TestCase

from kitchen.models import Cook, Dish, DishType


class ModelsTests(TestCase):
    def test_dish_type_str(self):
        dish_type = DishType.objects.create(
            name="Test dish name",
        )
        self.assertEqual(
            str(dish_type), f"{dish_type.name}"
        )

    def test_dish_str(self):
        dish_type = DishType.objects.create(
            name="Test dish name",
        )
        dish = Dish.objects.create(
            name="Test dish",
            price=100.00,
            dish_type=dish_type
        )
        self.assertEqual(str(dish), f"{dish.name} {dish.price}")

    def test_create_cook_with_years_of_experience(self):
        username = "test"
        password = "test12345"
        years_of_experience = 10
        cook = get_user_model().objects.create_user(
            username=username, password=password, years_of_experience=years_of_experience
        )
        self.assertEqual(cook.username, username)
        self.assertTrue(cook.check_password(password))
        self.assertEqual(cook.years_of_experience, years_of_experience)

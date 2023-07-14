from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from kitchen.models import DishType

DISH_TYPE_URL = reverse("kitchen:dish_type_list")


class PublicDishTypeTest(TestCase):
    def test_login_required(self):
        res = self.client.get(DISH_TYPE_URL)

        self.assertNotEquals(res.status_code, 200)


class PrivateDishTypeTest(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user("test" "password123")
        self.client.force_login(self.user)

    def test_retrieve_manufacturers(self):
        DishType.objects.create(
            name="Test dish type 1",
        )
        DishType.objects.create(
            name="Test dish type 2",
        )

        response = self.client.get(DISH_TYPE_URL)
        dish_types = DishType.objects.all()

        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            list(response.context["dishtype_list"]), list(dish_types)
        )
        self.assertTemplateUsed(response, "kitchen/dish_type_list.html")

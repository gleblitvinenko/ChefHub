from django.urls import path

from kitchen.views import (
    index,
    DishTypeListView,
    DishListView,
    CookListView
)

app_name = "kitchen"

urlpatterns = [
    path("", index, name="index"),
    path(
        "dish_types/",
        DishTypeListView.as_view(),
        name="dish_type_list"
    ),
    path(
        "dishes",
        DishListView.as_view(),
        name="dish_list"
    ),
    path(
        "cooks",
        CookListView.as_view(),
        name="cook_list"
    ),
]

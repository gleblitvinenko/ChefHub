from django.urls import path

from kitchen.views import (
    index,
    DishTypeListView,
    DishListView,
    CookListView,
    DishUpdateView,
    DishCreateView,
    DishDeleteView, DishDetailView
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
        "dishes/",
        DishListView.as_view(),
        name="dish_list"
    ),
    path(
        "dishes/create/",
        DishCreateView.as_view(),
        name="dish_create"
    ),
    path(
        "dishes/<int:pk>/update/",
        DishUpdateView.as_view(),
        name="dish_update"
    ),
    path(
        "dishes/<int:pk>/delete/",
        DishDeleteView.as_view(),
        name="dish_delete"
    ),
    path(
        "dishes/<int:pk>/",
        DishDetailView.as_view(),
        name="dish_detail"
    ),
    path(
        "cooks/",
        CookListView.as_view(),
        name="cook_list"
    ),
]

from django.urls import path

from kitchen.views import (
    DishTypeListView,
    DishListView,
    CookListView,
    DishUpdateView,
    DishCreateView,
    DishDeleteView,
    DishDetailView,
    DishTypeCreateView,
    DishTypeUpdateView,
    DishTypeDeleteView,
    CookCreateView,
    CookExperienceUpdateView,
    CookDeleteView,
    CookDetailView,
    ToggleAssignToDishView,
    IndexView,
)

app_name = "kitchen"

urlpatterns = [
    path("", IndexView.as_view(), name="index"),
    path("dish_types/", DishTypeListView.as_view(), name="dish_type_list"),
    path("dish_types/create/", DishTypeCreateView.as_view(), name="dish_type_create"),
    path(
        "dish_types/<int:pk>/update/",
        DishTypeUpdateView.as_view(),
        name="dish_type_update",
    ),
    path(
        "dish_types/<int:pk>/delete/",
        DishTypeDeleteView.as_view(),
        name="dish_type_delete",
    ),
    path("dishes/", DishListView.as_view(), name="dish_list"),
    path("dishes/create/", DishCreateView.as_view(), name="dish_create"),
    path("dishes/<int:pk>/update/", DishUpdateView.as_view(), name="dish_update"),
    path("dishes/<int:pk>/delete/", DishDeleteView.as_view(), name="dish_delete"),
    path("dishes/<int:pk>/", DishDetailView.as_view(), name="dish_detail"),
    path(
        "dishes/<int:pk>/toggle-assign/",
        ToggleAssignToDishView.as_view(),
        name="toggle_dish_assign",
    ),
    path("cooks/", CookListView.as_view(), name="cook_list"),
    path("cooks/create/", CookCreateView.as_view(), name="cook_create"),
    path(
        "cooks/<int:pk>/update/", CookExperienceUpdateView.as_view(), name="cook_update"
    ),
    path("cooks/<int:pk>/delete/", CookDeleteView.as_view(), name="cook_delete"),
    path("cooks/<int:pk>/", CookDetailView.as_view(), name="cook_detail"),
]

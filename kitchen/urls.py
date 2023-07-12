from django.urls import path

from kitchen.views import index

app_name = "kitchen"

urlpatterns = [
    path("", index, name="index"),
]
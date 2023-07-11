from django.contrib.auth.models import AbstractUser
from django.db import models


class DishType(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.name}"


class Cook(AbstractUser):
    years_of_experience = models.IntegerField()

    class Meta:
        verbose_name = "cook"
        verbose_name_plural = "cooks"

    def __str__(self):
        return f"{self.username} ({self.first_name} {self.last_name})"


class Dish(models.Model):
    name = models.CharField(
        max_length=255,
        unique=True
    )
    description = models.TextField()
    price = models.DecimalField(
        max_digits=5,
        decimal_places=2
    )
    dish_type = models.ForeignKey(
        DishType,
        related_name="dish",
        on_delete=models.CASCADE
    )
    cooks = models.ManyToManyField(
        Cook,
        related_name="dishes"
    )

    class Meta:
        verbose_name = "dish"
        verbose_name_plural = "dishes"

    def __str__(self):
        return f"{self.name} {self.price}"

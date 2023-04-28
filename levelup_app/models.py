from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class UserImage(models.Model):
    image = models.ImageField(upload_to="images")
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, null=True, blank=True, related_name="user_image")

    def __str__(self):
        return f"{self.user.username} {self.image}"


class Product(models.Model):
    name = models.CharField(max_length=150)
    price = models.FloatField(default=0)
    quantity = models.IntegerField(default=1)
    image = models.ImageField(upload_to="images")

    def __str__(self):
        return f"{self.name} {self.price} {self.quantity}"

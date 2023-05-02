from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class UserCreditCard(models.Model):
    name_on_card = models.CharField(max_length=100)
    card_number = models.CharField(max_length=100)
    expire_date = models.DateField()
    cvc_cvv = models.CharField(max_length=10)
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f"{self.name_on_card} {self.card_number} {self.expire_date} {self.cvc_cvv} {self.user}"


class CreditCardMoney(models.Model):
    money = models.FloatField(default=0)
    credit_card = models.OneToOneField(
        UserCreditCard, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f"{self.money} {self.credit_card}"


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
    in_sale = models.BooleanField(default=False)
    provider = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f"{self.name} {self.price} {self.quantity} {self.in_sale} {self.provider}"


class SavedProduct(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    date_saved = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} {self.product.name} {self.date_saved}"


class PurchasedProduct(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    date_purchased = models.DateTimeField(auto_now_add=True)
    quantity = models.IntegerField()
    money_spent = models.FloatField()

    def __str__(self):
        return f"{self.product.name} {self.user} {self.date_purchased} {self.quantity} {self.money_spent}"


class SoldProduct(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True)
    product_provider = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True)
    date_sold = models.DateTimeField(auto_now_add=True)
    quantity = models.IntegerField()
    money_gained = models.FloatField()

    def __str__(self):
        return f"{self.product} {self.product_provider} {self.date_sold} {self.quantity} {self.money_gained}"

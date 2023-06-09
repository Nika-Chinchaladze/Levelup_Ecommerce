from django.contrib import admin

from .models import UserImage, Product, SavedProduct, UserCreditCard, CreditCardMoney, PurchasedProduct, SoldProduct
# Register your models here.


class UserCreditCardAdmin(admin.ModelAdmin):
    list_display = ("name_on_card", "card_number",
                    "expire_date", "cvc_cvv", "user",)


class CreditCardMoneyAdmin(admin.ModelAdmin):
    list_display = ("money", "credit_card",)


class UserImageAdmin(admin.ModelAdmin):
    list_display = ("user", "image",)


class ProductAdmin(admin.ModelAdmin):
    list_display = ("name", "price", "quantity",
                    "image", "in_sale", "provider",)


class SavedProductAdmin(admin.ModelAdmin):
    list_display = ("product", "user", "date_saved",)


class PurchasedProductAdmin(admin.ModelAdmin):
    list_display = ("product", "user", "date_purchased",
                    "quantity", "money_spent",)


class SoldProductAdmin(admin.ModelAdmin):
    list_display = ("product", "product_provider",
                    "date_sold", "quantity", "money_gained",)


admin.site.register(UserCreditCard, UserCreditCardAdmin)
admin.site.register(CreditCardMoney, CreditCardMoneyAdmin)
admin.site.register(UserImage, UserImageAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(SavedProduct, SavedProductAdmin)
admin.site.register(PurchasedProduct, PurchasedProductAdmin)
admin.site.register(SoldProduct, SoldProductAdmin)

from django.contrib import admin

from .models import UserImage, Product
# Register your models here.


class UserImageAdmin(admin.ModelAdmin):
    list_display = ("user", "image",)


class ProductAdmin(admin.ModelAdmin):
    list_display = ("name", "price", "quantity", "image",)


admin.site.register(UserImage, UserImageAdmin)
admin.site.register(Product, ProductAdmin)

from django.contrib import admin

from .models import UserImage, Product, SavedProduct
# Register your models here.


class UserImageAdmin(admin.ModelAdmin):
    list_display = ("user", "image",)


class ProductAdmin(admin.ModelAdmin):
    list_display = ("name", "price", "quantity", "image",)


class SavedProductAdmin(admin.ModelAdmin):
    list_display = ("product", "user", "date_saved",)


admin.site.register(UserImage, UserImageAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(SavedProduct, SavedProductAdmin)

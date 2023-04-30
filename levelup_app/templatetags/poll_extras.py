from django import template
from levelup_app.models import Product

register = template.Library()


@register.filter(name="last_four")
def last_four(value):
    """Returns last 4 characters of string"""
    result = f"**** {value[-4:]}"
    return result


@register.filter(name="greater_than")
def greater_than(value):
    """Returns Boolean"""
    if int(value) > 0:
        return True
    return False


@register.filter(name="product_name")
def product_name(value):
    chosen_product = Product.objects.get(id=int(value))
    return chosen_product.name


@register.filter(name="product_image")
def product_image(value):
    chosen_product = Product.objects.get(id=int(value))
    return chosen_product.image.url

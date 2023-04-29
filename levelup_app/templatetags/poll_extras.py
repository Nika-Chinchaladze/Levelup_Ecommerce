from django import template

register = template.Library()


@register.filter(name="last_four")
def last_four(value):
    """Returns last 4 characters of string"""
    result = f"**** {value[-4:]}"
    return result

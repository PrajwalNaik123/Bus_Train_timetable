from django import template

register = template.Library()

@register.filter(name='split')
def split(value, separator=','):
    """
    Splits a string using the given separator.
    Usage in templates: {{ value|split:"," }}
    """
    if not isinstance(value, str):
        return []
    return value.split(separator)

@register.filter(name='trim')
def trim(value):
    """
    Trims leading and trailing whitespace from a string.
    Usage in templates: {{ value|trim }}
    """
    if isinstance(value, str):
        return value.strip()
    return ''

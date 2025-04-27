from django import template

register = template.Library()

@register.filter(name = 'persian_time')

def persian_time(value):
    pass

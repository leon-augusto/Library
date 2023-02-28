from django import template

register = template.Library()


@register.filter
def show_time(value1, value2):
    return (value1 - value2).days

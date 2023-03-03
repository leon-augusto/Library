from django import template
from datetime import datetime

register = template.Library()


@register.filter
def show_time(value1, value2):
    if all((isinstance(value1, datetime), isinstance(value2, datetime))):
        if (value1 - value2).days == 1:
            return '1 day'
        else:
            return f'{(value1 - value2).days} days'
    else:
        return 'It does not return it yet.'

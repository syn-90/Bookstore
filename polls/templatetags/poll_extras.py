from django import template
import jdatetime

register = template.Library()


@register.filter(name='persian_time')
def persian_time(time):
    result = jdatetime.datetime.fromgregorian(datetime=time).strftime('%Y %B %d')
    if 'Khordad' in result:
        result = result.replace('Khordad', 'خرداد')
    return result


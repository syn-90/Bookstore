from django import template
import jdatetime

register = template.Library()


@register.filter(name='persian_time')
def persian_time(time):
    return jdatetime.datetime.fromgregorian(datetime=time).strftime('%Y/%m/%d')

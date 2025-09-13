import jdatetime
from django import template
from articels_app.models import ArticleCommentModel
from jdatetime import datetime
import datetime
register = template.Library()

@register.filter(name = 'persian_time')
def persian_time(value):
    if isinstance(value, datetime.datetime):
        value = value.date()

        # تبدیل میلادی به جلالی
    date = jdatetime.date.fromgregorian(date=value)
    date = str(date).replace('-', '/')
    return date

@register.filter(name = 'filter_by_publish')
def filter_by_publish(value , id):
    result = ArticleCommentModel.objects.filter(is_publish=True ,article__id=id)
    return len(result)

@register.filter(name="number_seprator")
def number_seprator(value=0):
    return "{:,}".format(int(value))

@register.filter(name="price_with_off")
def price_with_off(value, off):
    final_price = int(value - (value * (off / 100)))
    return final_price
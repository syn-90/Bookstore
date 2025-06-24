from django import template
from articels_app.models import ArticleCommentModel
register = template.Library()

@register.filter(name = 'persian_time')
def persian_time(value):
    pass

@register.filter(name = 'filter_by_publish')
def filter_by_publish(value):
    result = ArticleCommentModel.objects.filter(is_publish=True)
    return len(result)
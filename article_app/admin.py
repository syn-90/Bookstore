from django.contrib import admin
from .models import ArticleModel
# Register your models here.


class ArticleAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "craete_at")
    prepopulated_fields = {
        'slug': ['title']
    }


admin.site.register(ArticleModel, ArticleAdmin)
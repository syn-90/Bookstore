from django.contrib import admin
from .models import ArticleModel
# Register your models here.


class ArticleAdmin(admin.ModelAdmin):
    list_display = ("title", "create_at", "author", "is_active")
    list_editable = ("is_active",)
    prepopulated_fields = {
        'slug': ['title']
    }
    def save_model(self, request, obj, form, change):
        if not change:
            obj.author = request.user
            obj.save()
        return super(ArticleAdmin, self).save_model(request, obj, form, change)


admin.site.register(ArticleModel,ArticleAdmin)
from django.contrib import admin
from .models import ProductModel, CategoryModel, AuthorModel
# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    list_display = ("title", "price", "publisher", "is_active")
    list_editable = ("price", "is_active")
    prepopulated_fields = {
        'slug': ['title']
    }

class AuthorAdmin(admin.ModelAdmin):
    list_display = ("name", )
    prepopulated_fields = {
        'slug': ['name']
    }


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {
        'slug': ['title']
    }

admin.site.register(ProductModel, ProductAdmin)
admin.site.register(AuthorModel, AuthorAdmin)
admin.site.register(CategoryModel, CategoryAdmin)
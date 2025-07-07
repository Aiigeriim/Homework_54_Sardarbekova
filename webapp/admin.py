
from django.contrib import admin
from webapp.models import Category, Product


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'title']
    list_display_links = ['id', 'title']
    fields = ['title', 'description']


admin.site.register(Category, CategoryAdmin)


class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'category', 'title', 'price', 'created_at']
    list_display_links = ['id', 'title']
    list_filter = ['created_at', 'category']
    search_fields = ['title']
    fields = ['title', 'price', 'description', 'category', 'created_at', 'image']
    readonly_fields = ['created_at']

admin.site.register(Product, ProductAdmin)

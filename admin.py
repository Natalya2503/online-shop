from django.contrib import admin
from goods.models import Categories, Products

# admin.site.register(Categories)
# admin.site.register(Products)

admin.site.site_header = 'Панель администрирования'

@admin.register(Categories)
class CategoriesAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    list_display_links = ('name')
    list_editable = ('slug')
    ordering = ['name']
    list_per_page = 5

@admin.register(Products)
class ProductsAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'description',
                     'price', 'quantity', 'category')
    list_display_links = ('name')
    list_editable = ('category')
    ordering = ['name']
    list_per_page = 5
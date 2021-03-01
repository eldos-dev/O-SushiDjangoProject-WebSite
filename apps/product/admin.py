from django.contrib import admin

from apps.product.models import Category, Product


class CategoryAdmin(admin.ModelAdmin):
    exclude = ('slug',)
    list_display = ('name', 'slug',)
    list_display_links = ('name',)


class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'price']
    list_display_links = ['id', 'title']


admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)

from django.contrib import admin

from products.models import Product


@admin.register(Product)
class AdminPanel(admin.ModelAdmin):
    list_display = ['title', 'price', 'active']

from django.contrib import admin
from catalog.models import *


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'image', 'price', 'category')
    list_filter = ('category',)
    search_fields = ('name', 'description')


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'phone')
    list_filter = ('name',)
    search_fields = ('name', 'phone')
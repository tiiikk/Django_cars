from django.contrib import admin

from .models import Category, Car


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['pk', 'name']
    search_fields = ['name']


class CarAdmin(admin.ModelAdmin):
    list_display = ['pk', 'name', 'category']
    search_fields = ['name']


admin.site.register(Category, CategoryAdmin)
admin.site.register(Car, CarAdmin)

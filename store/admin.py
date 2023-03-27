from django.contrib import admin

# Register your models here.
from .models import Member, Product, Category, Decoration, Order
class AdminProduct(admin.ModelAdmin):
    list_display = ['name', 'price', 'category']


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']

admin.site.register(Member)
admin.site.register(Product,AdminProduct)
admin.site.register(Category)
admin.site.register(Decoration)
admin.site.register(Order)
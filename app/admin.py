from django.contrib import admin
from .models import Category, FoodName, Order

admin.site.register(Category)
admin.site.register(FoodName)
admin.site.register(Order)
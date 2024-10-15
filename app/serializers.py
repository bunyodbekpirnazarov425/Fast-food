from rest_framework import serializers
from .models import Category, FoodName, Order

class CategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Category
        fields = ['url', 'id', 'name']


class FoodNameSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = FoodName
        fields = ['url', 'id', 'name', 'price', 'category']
        extra_kwargs = {
            'url': {'view_name': 'foodname-detail'}  # Bu yerda URL nomi to'g'ri ko'rsatilgan bo'lishi kerak
        }


class OrderSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Order
        fields = ['url', 'id', 'user', 'food_items', 'ordered_at']




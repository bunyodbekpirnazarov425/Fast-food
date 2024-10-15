from django.urls import path
from .views import CategoryListView, FoodNameListView, OrderListView

urlpatterns = [
    path('categories/', CategoryListView.as_view(), name='category-list'),
    path('categories/<int:pk>/', CategoryListView.as_view(), name='category-detail'),
    path('food-name/', FoodNameListView.as_view(), name='foodname-list'),
    path('food-name/<int:pk>/', FoodNameListView.as_view(), name='foodname-detail'),
    path('orders/', OrderListView.as_view(), name='order-list'),
    path('orders/<int:pk>/', OrderListView.as_view(), name='order-detail'),
]

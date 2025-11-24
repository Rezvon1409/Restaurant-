from django.urls import path
from .views import *

urlpatterns = [
    path("restaurants/", RestaurantListCreateAPIView.as_view(), name="restaurant-list"),
    path("restaurants/<int:pk>/", RestaurantDetailAPIView.as_view(), name="restaurant-detail"),
    path("zones/", DeliveryZoneListCreateAPIView.as_view(), name="zone-list"),
    path("zones/<int:pk>/", DeliveryZoneDetailAPIView.as_view(), name="zone-detail"),
    path("categories/", CategoryListCreateAPIView.as_view(), name="category-list"),
    path("categories/<int:pk>/", CategoryDetailAPIView.as_view(), name="category-detail"),
    path("foods/", FoodListCreateAPIView.as_view(), name="food-list"),
    path("foods/<int:pk>/", FoodDetailAPIView.as_view(), name="food-detail"),
    path("addons/", AddonListCreateAPIView.as_view(), name="addon-list"),
    path("addons/<int:pk>/", AddonDetailAPIView.as_view(), name="addon-detail"),
    path("promocodes/", PromocodeListCreateAPIView.as_view(), name="promocode-list"),
    path("promocodes/<int:pk>/", PromocodeDetailAPIView.as_view(), name="promocode-detail"),
    path("orders/", OrderListCreateAPIView.as_view(), name="order-list"),
    path("orders/<int:pk>/", OrderDetailAPIView.as_view(), name="order-detail"),
    path("order-items/", OrderItemListCreateAPIView.as_view(), name="orderitem-list"),
    path("order-items/<int:pk>/", OrderItemDetailAPIView.as_view(), name="orderitem-detail"),
    path("order-item-addons/", OrderItemAddOnListCreateAPIView.as_view(), name="orderitemaddon-list"),
    path("order-item-addons/<int:pk>/", OrderItemAddOnDetailAPIView.as_view(), name="orderitemaddon-detail"),
]

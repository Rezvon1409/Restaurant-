from rest_framework import serializers
from .models import *


class RestaurantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurant
        fields = ("id", "title", "address", "phone", "open_time", "close_time", "delivery_base_price")


class DeliveryZoneSerializer(serializers.ModelSerializer):
    class Meta:
        model = DeliveryZone
        fields = ("id", "title", "price")


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ("id", "title")


class FoodSerializer(serializers.ModelSerializer):
    class Meta:
        model = Food
        fields = ("id", "category", "title", "description", "price", "available", "is_popular", "created_at")


class AddonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Addon
        fields = ("id", "title", "extra_price")


class PromocodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Promocode
        fields = ("id", "code", "discount_percent", "valid_until")


class OrderItemAddOnSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItemAddOn
        fields = ("id", "order_item", "addon")


class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = ("id", "order", "food", "quantity", "price_at_order", "addons")


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ("id","user","phone","address","zone","payment_method","status","promo","delivery_price","total_price","created_at","items",)

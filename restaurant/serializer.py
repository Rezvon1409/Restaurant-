from rest_framework import serializers
from .models import *


class RestaurantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurant
        fields = "__all__"  


class DeliveryZoneSerializer(serializers.ModelSerializer):
    class Meta:
        model = DeliveryZone
        fields = ("id", "title", "price")


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ("id", "title", "image")   


class FoodSerializer(serializers.ModelSerializer):
    class Meta:
        model = Food
        fields = "__all__"  



class AddonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Addon
        fields = ("id", "title", "extra_price", "image")   



class PromocodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Promocode
        fields = ("id", "code", "discount_percent", "valid_until")


class OrderItemAddOnSerializer(serializers.ModelSerializer):
    addon = AddonSerializer(read_only=True)

    class Meta:
        model = OrderItemAddOn
        fields = ("id", "order_item", "addon")


class OrderItemSerializer(serializers.ModelSerializer):
    food = FoodSerializer(read_only=True)
    addons = OrderItemAddOnSerializer(many=True, read_only=True)

    class Meta:
        model = OrderItem
        fields = ("id", "order", "food", "quantity", "price_at_order", "addons")


class OrderSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(many=True, read_only=True)
    zone = DeliveryZoneSerializer(read_only=True)
    promo = PromocodeSerializer(read_only=True)

    class Meta:
        model = Order
        fields = ("id","user","phone","address","zone","payment_method","status","promo","delivery_price","total_price","created_at","items",)

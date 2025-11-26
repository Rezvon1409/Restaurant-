from rest_framework import serializers
from .models import *


class RestaurantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurant
        fields = "__all__"


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ("id", "user", "avatar", "default_address", "default_phone", "favorite_foods")


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ("id", "user", "food", "restaurant", "rating", "comment", "created_at")


class CartItemSerializer(serializers.ModelSerializer):
    food = serializers.StringRelatedField(read_only=True)
    addons = serializers.StringRelatedField(many=True, read_only=True)

    class Meta:
        model = CartItem
        fields = ("id", "cart", "food", "quantity", "addons")


class CartSerializer(serializers.ModelSerializer):
    items = CartItemSerializer(many=True, read_only=True)

    class Meta:
        model = Cart
        fields = ("id", "user", "created_at", "items")


class PaymentTransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = PaymentTransaction
        fields = ("id", "order", "method", "amount", "status", "transaction_id", "created_at")


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
    payment = PaymentTransactionSerializer(read_only=True)

    class Meta:
        model = Order
        fields = ("id","user","phone","address","zone","payment_method","status","promo","delivery_price", "total_price","created_at","items","payment",)

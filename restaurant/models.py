from django.db import models
from accounts.models import CustomUser


class Restaurant(models.Model):
    title = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    phone = models.CharField(max_length=20)
    open_time = models.TimeField()
    close_time = models.TimeField()
    delivery_base_price = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return self.title



class DeliveryZone(models.Model):
    title = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return self.title



class Category(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title



class Food(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="foods")
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    available = models.BooleanField(default=True)
    is_popular = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title



class Addon(models.Model):
    title = models.CharField(max_length=100)
    extra_price = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return self.title



class Promocode(models.Model):
    code = models.CharField(max_length=50, unique=True)
    discount_percent = models.PositiveIntegerField()
    valid_until = models.DateField()

    def __str__(self):
        return self.code



class Order(models.Model):
    PAYMENT_CHOICES = (
        ("cash", "Cash"),
        ("card", "Card"),
    )
    STATUS_CHOICES = (
        ("pending", "Pending"),
        ("processing", "Processing"),
        ("delivered", "Delivered"),
        ("cancelled", "Cancelled"),
    )

    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="orders")
    phone = models.CharField(max_length=20)
    address = models.CharField(max_length=200)
    zone = models.ForeignKey(DeliveryZone, on_delete=models.SET_NULL, null=True)
    payment_method = models.CharField(max_length=20, choices=PAYMENT_CHOICES)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="pending")
    promo = models.ForeignKey(Promocode, on_delete=models.SET_NULL, null=True, blank=True)
    delivery_price = models.DecimalField(max_digits=6, decimal_places=2, default=0)
    total_price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order {self.id} by {self.user.username}"



class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name="items")
    food = models.ForeignKey(Food, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    price_at_order = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return f"{self.quantity} x {self.food.title}"


class OrderItemAddOn(models.Model):
    order_item = models.ForeignKey(OrderItem, on_delete=models.CASCADE, related_name="addons")
    addon = models.ForeignKey(Addon, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.addon.title} for {self.order_item.food.title}"

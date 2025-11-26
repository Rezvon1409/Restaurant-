from django.db import models
from accounts.models import CustomUser
from django.core.exceptions import ValidationError


class Restaurant(models.Model):
    title = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    phone = models.CharField(max_length=20)
    open_time = models.TimeField()
    close_time = models.TimeField()
    delivery_base_price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(upload_to="restaurants/", blank=True, null=True)

    def __str__(self):
        return self.title


class Profile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name="profile")
    avatar = models.ImageField(upload_to="profiles/", blank=True, null=True)
    default_address = models.CharField(max_length=200, blank=True, null=True)
    default_phone = models.CharField(max_length=20, blank=True, null=True)
    favorite_foods = models.ManyToManyField("Food", blank=True)

    def __str__(self):
        return f"Profile of {self.user.username}"


class Review(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    food = models.ForeignKey("Food", on_delete=models.CASCADE, related_name="reviews", null=True, blank=True)
    restaurant = models.ForeignKey("Restaurant", on_delete=models.CASCADE, related_name="reviews", null=True, blank=True)
    rating = models.PositiveIntegerField(default=1)
    comment = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def clean(self):
        if not self.food and not self.restaurant:
            raise ValidationError("Review must be linked to either a Food or a Restaurant.")

    def __str__(self):
        return f"Review by {self.user.username} ({self.rating})"


class Cart(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="cart")
    created_at = models.DateTimeField(auto_now_add=True)

    def calculate_total(self):
        subtotal = sum([item.food.price * item.quantity for item in self.items.all()])
        addons_total = sum([
            addon.extra_price
            for item in self.items.all()
            for addon in item.addons.all()
        ])
        return subtotal + addons_total


class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name="items")
    food = models.ForeignKey("Food", on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    addons = models.ManyToManyField("Addon", blank=True)

    def __str__(self):
        return f"{self.quantity} x {self.food.title}"


class PaymentTransaction(models.Model):
    STATUS_CHOICES = (
        ("pending", "Pending"),
        ("success", "Success"),
        ("failed", "Failed"),
    )

    order = models.OneToOneField("Order", on_delete=models.CASCADE, related_name="payment")
    method = models.CharField(max_length=50)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="pending")
    transaction_id = models.CharField(max_length=100, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Payment for Order {self.order.id} - {self.status}"


class DeliveryZone(models.Model):
    title = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return self.title


class Category(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to="categories/", blank=True, null=True)

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
    image = models.ImageField(upload_to="foods/", blank=True, null=True)

    def __str__(self):
        return self.title


class Addon(models.Model):
    title = models.CharField(max_length=100)
    extra_price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(upload_to="addons/", blank=True, null=True)

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

    def calculate_total(self):
        subtotal = sum([item.quantity * item.price_at_order for item in self.items.all()])
        addons_total = sum([
            addon.addon.extra_price
            for item in self.items.all()
            for addon in item.addons.all()
        ])
        subtotal += addons_total
        if self.promo:
            subtotal -= subtotal * (self.promo.discount_percent / 100)
        if self.zone:
            self.delivery_price = self.zone.price
        return subtotal + self.delivery_price

    def save(self, *args, **kwargs):
        self.total_price = self.calculate_total()
        super().save(*args, **kwargs)


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name="items")
    food = models.ForeignKey(Food, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    price_at_order = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return f"{self.quantity} x {self.food.title}"

    def save(self, *args, **kwargs):
        if not self.price_at_order:
            self.price_at_order = self.food.price
        super().save(*args, **kwargs)
        self.order.save()


class OrderItemAddOn(models.Model):
    order_item = models.ForeignKey(OrderItem, on_delete=models.CASCADE, related_name="addons")
    addon = models.ForeignKey(Addon, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.addon.title} for {self.order_item.food.title}"

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        self.order_item.order.save()

    def delete(self, *args, **kwargs):
        super().delete(*args, **kwargs)
        self.order_item.order.save()

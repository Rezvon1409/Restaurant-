from django.contrib import admin
from .models import *

admin.site.register(Restaurant)
admin.site.register(DeliveryZone)
admin.site.register(Category)
admin.site.register(Food)
admin.site.register(Addon)
admin.site.register(Promocode)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(OrderItemAddOn)

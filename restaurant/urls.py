from django.urls import path
from .views import *


urlpatterns = [
    path("restaurants/", RestaurantListCreateAPIView.as_view()),
    path("restaurants/<int:pk>/", RestaurantDetailAPIView.as_view()),
    path("profiles/<int:pk>/", ProfileDetailAPIView.as_view()),
    path("reviews/", ReviewListCreateAPIView.as_view()),
    path("reviews/<int:pk>/", ReviewDetailAPIView.as_view()),
    path("carts/", CartListCreateAPIView.as_view()),
    path("carts/<int:pk>/", CartDetailAPIView.as_view()),
    path("payments/", PaymentTransactionListCreateAPIView.as_view()),
    path("payments/<int:pk>/", PaymentTransactionDetailAPIView.as_view()),
    path("zones/", DeliveryZoneListCreateAPIView.as_view()),
    path("zones/<int:pk>/", DeliveryZoneDetailAPIView.as_view()),
    path("categories/", CategoryListCreateAPIView.as_view()),
    path("categories/<int:pk>/", CategoryDetailAPIView.as_view()),
    path("foods/", FoodListCreateAPIView.as_view()),
    path("foods/<int:pk>/", FoodDetailAPIView.as_view()),
    path("addons/", AddonListCreateAPIView.as_view()),
    path("addons/<int:pk>/", AddonDetailAPIView.as_view()),
    path("promocodes/", PromocodeListCreateAPIView.as_view()),
    path("promocodes/<int:pk>/", PromocodeDetailAPIView.as_view()),
    path("orders/", OrderListCreateAPIView.as_view()),
    path("orders/<int:pk>/", OrderDetailAPIView.as_view()),
    path("order-items/", OrderItemListCreateAPIView.as_view()),
    path("order-items/<int:pk>/", OrderItemDetailAPIView.as_view()),
    path("orderitem-addons/", OrderItemAddOnListCreateAPIView.as_view()),
    path("orderitem-addons/<int:pk>/", OrderItemAddOnDetailAPIView.as_view()),
]

from rest_framework import generics, permissions
from drf_yasg.utils import swagger_auto_schema
from rest_framework.parsers import MultiPartParser, FormParser
from .models import *
from .serializer import *

class RestaurantListCreateAPIView(generics.ListCreateAPIView):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer
    parser_classes = [MultiPartParser, FormParser]
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    @swagger_auto_schema(tags=["Restaurant"])
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    @swagger_auto_schema(tags=["Restaurant"])
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)


class RestaurantDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer
    parser_classes = [MultiPartParser, FormParser]
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    @swagger_auto_schema(tags=["Restaurant"])
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)


class DeliveryZoneListCreateAPIView(generics.ListCreateAPIView):
    queryset = DeliveryZone.objects.all()
    serializer_class = DeliveryZoneSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    @swagger_auto_schema(tags=["DeliveryZone"])
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    @swagger_auto_schema(tags=["DeliveryZone"])
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)


class DeliveryZoneDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = DeliveryZone.objects.all()
    serializer_class = DeliveryZoneSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    @swagger_auto_schema(tags=["DeliveryZone"])
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)


class CategoryListCreateAPIView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    parser_classes = [MultiPartParser, FormParser]
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    @swagger_auto_schema(tags=["Category"])
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    @swagger_auto_schema(tags=["Category"])
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)


class CategoryDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    parser_classes = [MultiPartParser, FormParser]
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    @swagger_auto_schema(tags=["Category"])
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)


class FoodListCreateAPIView(generics.ListCreateAPIView):
    queryset = Food.objects.all()
    serializer_class = FoodSerializer
    parser_classes = [MultiPartParser, FormParser]
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    @swagger_auto_schema(tags=["Food"])
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    @swagger_auto_schema(tags=["Food"])
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)


class FoodDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Food.objects.all()
    serializer_class = FoodSerializer
    parser_classes = [MultiPartParser, FormParser]
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    @swagger_auto_schema(tags=["Food"])
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)


class AddonListCreateAPIView(generics.ListCreateAPIView):
    queryset = Addon.objects.all()
    serializer_class = AddonSerializer
    parser_classes = [MultiPartParser, FormParser]
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    @swagger_auto_schema(tags=["Addon"])
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    @swagger_auto_schema(tags=["Addon"])
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)


class AddonDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Addon.objects.all()
    serializer_class = AddonSerializer
    parser_classes = [MultiPartParser, FormParser]
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    @swagger_auto_schema(tags=["Addon"])
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)


class PromocodeListCreateAPIView(generics.ListCreateAPIView):
    queryset = Promocode.objects.all()
    serializer_class = PromocodeSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    @swagger_auto_schema(tags=["Promocode"])
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    @swagger_auto_schema(tags=["Promocode"])
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)


class PromocodeDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Promocode.objects.all()
    serializer_class = PromocodeSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    @swagger_auto_schema(tags=["Promocode"])
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)


class OrderListCreateAPIView(generics.ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [permissions.IsAuthenticated]

    @swagger_auto_schema(tags=["Order"])
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    @swagger_auto_schema(tags=["Order"])
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class OrderDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [permissions.IsAuthenticated]

    @swagger_auto_schema(tags=["Order"])
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)


class OrderItemListCreateAPIView(generics.ListCreateAPIView):
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer
    permission_classes = [permissions.IsAuthenticated]

    @swagger_auto_schema(tags=["OrderItem"])
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    @swagger_auto_schema(tags=["OrderItem"])
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)


class OrderItemDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer
    permission_classes = [permissions.IsAuthenticated]

    @swagger_auto_schema(tags=["OrderItem"])
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)


class OrderItemAddOnListCreateAPIView(generics.ListCreateAPIView):
    queryset = OrderItemAddOn.objects.all()
    serializer_class = OrderItemAddOnSerializer
    permission_classes = [permissions.IsAuthenticated]

    @swagger_auto_schema(tags=["OrderItemAddOn"])
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

from django.shortcuts import render

from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated
from .models import ClientOrders

from .serialers import CreateOrderSerializer, UserOrderListSerializer


class CreateUserOrderView(CreateAPIView):
    serializer_class = CreateOrderSerializer

    permission_classes = (IsAuthenticated,)

    """assign user to order"""

    def perform_create(self, serializer):
        return serializer.save(owner=self.request.user)


class UserOrderListView(ListAPIView):
    serializer_class = UserOrderListSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        return ClientOrders.objects.filter(owner=self.request.user)


class OrdersRetrieveUpdateDeleteView(RetrieveUpdateDestroyAPIView):
    serializer_class = CreateOrderSerializer
    permission_classes = (IsAuthenticated,)
    lookup_field = 'id'

    def get_queryset(self):
        return ClientOrders.objects.filter(owner=self.request.user)

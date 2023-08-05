from rest_framework import viewsets
from .. models import Cart
from .cart_serializer import CartSerializer
from rest_framework.permissions import IsAuthenticated


class CartViewset(viewsets.ModelViewSet):
    serializer_class=CartSerializer
    queryset=Cart.objects.all().select_related('user').prefetch_related('product')
    permission_classes = [IsAuthenticated]
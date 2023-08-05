from rest_framework import viewsets
from ..models import Product, ProductImage
from .product_serializer import ProductSerializer,ProductImageSerialier

from rest_framework.permissions import IsAuthenticated
from rest_framework.parsers import MultiPartParser


class ProductViewset(viewsets.ModelViewSet):
    serializer_class=ProductSerializer
    queryset=Product.objects.all().select_related('user')
    permission_classes = [IsAuthenticated]

class ProductImageViewset(viewsets.ModelViewSet):
    serializer_class=ProductImageSerialier
    queryset=ProductImage.objects.all()
    parser_classes = [MultiPartParser]
    permission_classes = [IsAuthenticated]    
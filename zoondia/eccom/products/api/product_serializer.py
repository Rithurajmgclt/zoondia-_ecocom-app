from rest_framework import serializers
from ..models import Product, ProductImage


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model =Product
        fields = '__all__'


class ProductImageSerialier(serializers.ModelSerializer):
    class Meta:
        model=ProductImage
        fields = '__all__'



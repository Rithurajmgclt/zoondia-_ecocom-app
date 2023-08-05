from django.db import models
from django.contrib.auth.models import User


# Create your models here
class Product(models.Model):
    user     = models.ForeignKey(User,on_delete=models.CASCADE)
    name     = models.CharField(max_length=30)
    price    = models.FloatField()
    quantity = models.IntegerField()
    status   = models.BooleanField(default=True)

class ProductImage(models.Model):
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    image   = models.ImageField(upload_to='images/product')  


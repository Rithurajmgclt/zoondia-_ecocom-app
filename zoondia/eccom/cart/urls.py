from django.urls import path,include
from rest_framework import routers
from .api.cart_views import CartViewset

router = routers.DefaultRouter()


router.register('cart', CartViewset)



urlpatterns = [
    path('', include(router.urls)),
]
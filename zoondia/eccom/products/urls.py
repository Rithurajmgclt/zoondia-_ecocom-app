from django.urls import path,include
from rest_framework import routers
from .api.proct_views import ProductImageViewset,ProductViewset

router = routers.DefaultRouter()


router.register('productimage', ProductImageViewset)
router.register('product',ProductViewset)


urlpatterns = [
    path('', include(router.urls)),
]
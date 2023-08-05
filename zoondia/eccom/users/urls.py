from django.urls import path,include
from rest_framework import routers
from .api.user_views import UserViewSet,GroupViewset

router = routers.DefaultRouter()


router.register(r'user', UserViewSet)
router.register('groups',GroupViewset)


urlpatterns = [
    path('', include(router.urls)),
]
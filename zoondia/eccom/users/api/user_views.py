from rest_framework import viewsets
from django.contrib.auth.models import User,Group
from .user_serializer import UserSerializer,GroupSerializer
from ..permission import IsAuthenticatedReadOnly
from rest_framework.permissions import IsAuthenticated

class UserViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing user instances.
    """
    serializer_class = UserSerializer
    queryset = User.objects.all()
    # permission_classes=[IsAuthenticatedReadOnly]s
class GroupViewset(viewsets.ModelViewSet):
    serializer_class=GroupSerializer
    queryset=Group.objects.all()
    http_method_names= ['get']
    permission_classes = [IsAuthenticated]

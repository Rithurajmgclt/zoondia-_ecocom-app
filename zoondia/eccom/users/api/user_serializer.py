import re
from rest_framework import serializers
from django.contrib.auth.models import User,Group



class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model=Group
        fields = ['id','name']





class UserSerializer(serializers.ModelSerializer):
    role_details = serializers.SerializerMethodField()
    role = serializers.ListField(child=serializers.IntegerField(),required=True,write_only=True)
    is_staff = serializers.BooleanField(default=True,write_only=True)
    password = serializers.CharField(required=True,write_only=True)
    confirm_password = serializers.CharField(required=True,write_only=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'is_staff','password','confirm_password','role','role_details']
    def create(self, validated_data):
        password = validated_data.pop('password')
        confirm_password = validated_data.pop('confirm_password')
        role = validated_data.pop('role')
        print(validated_data)
        if password != confirm_password:
            raise serializers.ValidationError("Passwords do not match.")
        user =  User.objects.create_user(**validated_data)
        if user:
            user.set_password(password)
        if role:
            groups = Group.objects.filter(pk__in=role)
            user.groups.set(groups)
        user.save()
        return user
    def update(self, instance, validated_data):
        user = instance
        user.username = validated_data.get('username', user.username)
        user.email = validated_data.get('email', user.email)
        user.first_name = validated_data.get('first_name', user.first_name)
        user.last_name = validated_data.get('last_name', user.last_name)
        user.save()
        if validated_data.get("password"):
            user.set_password(validated_data.get("password"))
        if validated_data.role:
            role =validated_data.get("role")
            groups = Group.objects.filter(pk__in=role)
            user.groups.set(groups)    
        user.save()
    
        return user 
    def get_role_details(self, obj):
        try:
            return Group.objects.values_list('id', 'name').filter(user=obj)
        except:
            return None
class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model=Group
        fields = ['id','name']


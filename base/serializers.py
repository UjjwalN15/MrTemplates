from rest_framework import serializers
from django.utils.timezone import now
from .models import *
from .validators import validate_password
from .emails import *
from django.core.exceptions import ValidationError
from django.contrib.auth.models import Group


import random

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ('id','email', 'password','role')

    def validate_password(self, value):
        try:
            validate_password(value)
        except ValidationError as e:
            raise serializers.ValidationError(e.messages)
        return value

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)

class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()


class RefreshTokenSerializer(serializers.Serializer):
    refresh = serializers.CharField()
    
class GroupsSerializer(serializers.ModelSerializer):
    def to_representation(self, instance):
    # Get the default representation from the parent class
        representation = super().to_representation(instance)

        # Add the permission names to the representation
        representation['permissions'] = [permission.name for permission in instance.permissions.all()]

        return representation
    class Meta:
        model=Group
        fields = '__all__'
        
class ThemeSerializer(serializers.ModelSerializer):
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        if instance.package_id:
            # You can use the package's serializer to get all fields
            from .serializers import PackageSerializer
            package_data = PackageSerializer(instance.package_id).data
            representation['package_id'] = package_data
        else:
            representation['package_id'] = None
        return representation

    class Meta:
        model = Theme
        fields = '__all__'
        
class PackageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Package
        fields = '__all__'
        
class StoreCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = StoreCategory
        fields = '__all__'
        
class StoreSerializer(serializers.ModelSerializer):
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        if instance.user_id:
            # You can use the package's serializer to get all fields
            from .serializers import PackageSerializer
            user_data = UserSerializer(instance.user_id).data
            representation['user_id'] = user_data
        else:
            representation['user_id'] = None
        if instance.theme_id:
            # You can use the package's serializer to get all fields
            from .serializers import PackageSerializer
            theme_data = ThemeSerializer(instance.theme_id).data
            representation['theme_id'] = theme_data
        else:
            representation['theme_id'] = None
        if instance.store_category_id:
            # You can use the package's serializer to get all fields
            from .serializers import PackageSerializer
            store_category_data = StoreCategorySerializer(instance.store_category_id).data
            representation['store_category_id'] = store_category_data
        else:
            representation['store_category_id'] = None
        return representation
    class Meta:
        model = Store
        fields = '__all__'
        
class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = '__all__'
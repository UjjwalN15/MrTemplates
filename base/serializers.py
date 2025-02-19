from rest_framework import serializers
from django.utils.timezone import now
from .models import User
from .validators import validate_password
from .emails import *
from django.core.exceptions import ValidationError
from django.contrib.auth.models import Group


import random

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ('email', 'password','role')

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
from .models import *
from rest_framework import serializers
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    full_name = serializers.SerializerMethodField('get_full_name')

    class Meta:
        model = User
        exclude = ('is_superuser', 'is_staff')

    def get_full_name(self, obj):
        return "{} {}".format(obj.first_name, obj.last_name)


class AddressSerializer(serializers.ModelSerializer):
    """Serializes an Address object"""
    class Meta:
        model = Address
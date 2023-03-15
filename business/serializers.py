from rest_framework import serializers
from .models import *


class BusinessSerializer(serializers.ModelSerializer):
    class Meta:
        model = Business
        fields = (
            'name',
            'image',
            'description',
            'category',
            'phone',
            'city',
            'address',
            'active',
            'code',
            'id',
        )
        extra_kwargs = {
            "admin": {"read_only": True},
            "active": {"read_only": True},
            "code": {"read_only": True},
        }





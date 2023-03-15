from rest_framework import serializers
from django.conf import settings
from .models import *
from rest_framework.authtoken.models import *
from django.contrib.auth.models import User
from rest_framework_simplejwt.views import TokenObtainPairView

class UserCreateSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(style={'input_type': 'password'}, write_only=True)

    class Meta:
        model = User
        fields = ['email','username','password', 'password2',]
        extra_kwargs = {'password': {'write_only': True}, }

    def save(self):
        user = User(
            email=self.validated_data['email'],
            username=self.validated_data['username'],
        )
        password = self.validated_data['password'],
        password2 = self.validated_data['password2'],
        if password != password2:
            raise serializers.ValidationError({'password':"Password Must Match"})
        user.set_password(self.validated_data['password'])
        user.save()
        token = Token.objects.create(user=user)
        return user

class BookedSessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookedSession
        fields = "__all__"

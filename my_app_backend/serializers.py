from rest_framework import serializers
from .models import LoginCredentials

class CredentialsSerializer(serializers.ModelSerializer):
    class Meta:
        model = LoginCredentials
        fields = ['id', 'email', 'password']
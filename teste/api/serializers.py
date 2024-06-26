from rest_framework import serializers
from .models import Home

class HomeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Home
        fields = ('id', 'code', 'password', 'mistakes', 'spaces', 'tips', 'created_at')
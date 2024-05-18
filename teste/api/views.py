from django.shortcuts import render
from rest_framework import generics
from .models import Home
from .serializers import HomeSerializer

class HomeView(generics.CreateAPIView):
    queryset = Home.objects.all()
    serializer_class = HomeSerializer

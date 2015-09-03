from django.shortcuts import render
from mainsite.serializers import UserSerializer
from rest_framework import viewsets
from django.contrib.auth.models import User

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer

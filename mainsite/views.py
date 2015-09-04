from django.shortcuts import render
from mainsite.serializers import UserSerializer, SessionTypeSerializer
from rest_framework import viewsets
from django.contrib.auth.models import User
from mainsite.models import SessionType

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer

class SessionTypeViewSet(viewsets.ModelViewSet):
    queryset = SessionType.objects.all()
    serializer_class = SessionTypeSerializer

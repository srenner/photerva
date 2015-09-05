from django.shortcuts import render
from mainsite.serializers import UserSerializer, SessionTypeSerializer, CustomerSerializer
from rest_framework import viewsets
from django.contrib.auth.models import User
from mainsite.models import SessionType, Customer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer

class SessionTypeViewSet(viewsets.ModelViewSet):
    queryset = SessionType.objects.all()#filter(user=self.request.user)
    serializer_class = SessionTypeSerializer

class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()#filter(user=self.request.user)
    serializer_class = CustomerSerializer

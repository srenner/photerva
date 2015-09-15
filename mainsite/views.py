from django.shortcuts import render
from mainsite.serializers import UserSerializer
from mainsite.serializers import SessionTypeSerializer
from mainsite.serializers import CustomerSerializer
from mainsite.serializers import PhoneSerializer
from mainsite.serializers import SessionSerializer
from mainsite.serializers import LocationSerializer
from mainsite.serializers import AddressSerializer
from rest_framework import viewsets
from django.contrib.auth.models import User
from mainsite.models import SessionType, Customer, Phone, Session, Location
from mainsite.models import Address

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer

class SessionTypeViewSet(viewsets.ModelViewSet):
    queryset = SessionType.objects.all()#filter(user=self.request.user)
    serializer_class = SessionTypeSerializer

class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()#filter(user=self.request.user)
    serializer_class = CustomerSerializer

class PhoneViewSet(viewsets.ModelViewSet):
    queryset = Phone.objects.all()
    serializer_class = PhoneSerializer

class SessionViewSet(viewsets.ModelViewSet):
    queryset = Session.objects.all()
    serializer_class = SessionSerializer

class LocationViewSet(viewsets.ModelViewSet):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer

class AddressViewSet(viewsets.ModelViewSet):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer

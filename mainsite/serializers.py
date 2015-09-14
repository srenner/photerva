from django.contrib.auth.models import User
from rest_framework import serializers
from mainsite.models import SessionType, Customer, Phone, Location

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')

class SessionTypeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = SessionType
        fields = ('name', 'notes', 'base_price', 'shoot_time', 'edit_time', 'user')

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        #depth = 2
        phones = serializers.StringRelatedField(many=True, required=False)
        fields = ('name', 'notes', 'user', 'phones')

class PhoneSerializer(serializers.ModelSerializer):
    class Meta:
        model = Phone
        fields = ('name', 'phone', 'ext', 'location', 'customer')

class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = ('name', 'notes', 'user')

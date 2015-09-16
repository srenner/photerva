from django.contrib.auth.models import User
from rest_framework import serializers
from mainsite.models import SessionType, Customer, Phone, Session, Location, Address

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')

class SessionTypeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = SessionType
        fields = ('name', 'notes', 'base_price', 'shoot_time', 'edit_time', 'owner')

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        #depth = 2
        phones = serializers.StringRelatedField(many=True, required=False)
        fields = ('name', 'notes', 'owner', 'phones')

class PhoneSerializer(serializers.ModelSerializer):
    class Meta:
        model = Phone
        fields = ('name', 'phone', 'ext', 'location', 'customer')

class SessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Session
        #locations = serializers.StringRelatedField(many=True, required=False)
        fields = ('datetime', 'backup_datetime', 'notes', 'quoted_price', 'final_price', 'expenses', 'shoot_time', 'edit_time', 'owner')

class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = ('name', 'notes', 'owner')

class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = ('name', 'address1', 'address2', 'city', 'state', 'zip')

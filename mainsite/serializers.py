from django.contrib.auth.models import User
from rest_framework import serializers
<<<<<<< HEAD
from mainsite.models import SessionType, Customer, Phone, Session, Location
=======
from mainsite.models import SessionType, Customer, Phone, Location
>>>>>>> 82b67223f4e5f08792e3d28d3a1510795016c297

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

class SessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Session
        #locations = serializers.StringRelatedField(many=True, required=False)
        fields = ('datetime', 'backup_datetime', 'notes', 'quoted_price', 'final_price', 'expenses', 'shoot_time', 'edit_time', 'user')

class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = ('name', 'notes', 'user')

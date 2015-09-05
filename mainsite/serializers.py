from django.contrib.auth.models import User
from rest_framework import serializers
from mainsite.models import SessionType, Customer

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')

class SessionTypeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = SessionType
        fields = ('name', 'notes', 'base_price', 'shoot_time', 'edit_time', 'user')

class CustomerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Customer
        fields = ('name', 'notes', 'user')

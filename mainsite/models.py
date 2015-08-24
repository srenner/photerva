from django.db import models
from django.contrib.auth.models import User
from django.db.models.fields.related import ForeignKey

#########PARENT CLASSES WE ARE MOST INTERESTED IN##########

class Location(models.Model):
    name = models.CharField(max_length = 100)
    notes = models.CharField()
    user = models.ForeignKey(User)
    
class Customer(models.Model):
    name = models.CharField(max_length = 100)
    notes = models.CharField()
    user = models.ForeignKey(User)

class SessionType(models.Model):
    name = models.CharField(max_length = 100)
    notes = models.CharField()
    base_price = models.DecimalField()
    shoot_time = models.TimeField()
    edit_time = models.TimeField()
    user = models.ForeignKey(User)

class Session(models.Model):
    datetime = models.DateTimeField()
    backup_datetime = models.DateTimeField()
    notes = models.CharField()
    quoted_price = models.DecimalField()
    final_price = models.DecimalField()
    expenses = models.DecimalField()
    shoot_time = models.TimeField()
    edit_time = models.TimeField()
    user = models.ForeignKey(User)
    
##########CHILD CLASSES##########

class Phone(models.Model):
    name = models.CharField(max_length = 100)
    phone = models.CharField(max_length = 25)
    ext = models.CharField(max_length = 25)
    
class Email(models.Model):
    name = models.CharField(max_length = 100)
    email = models.CharField(max_length = 200)
    

class Link(models.Model):
    name = models.CharField(max_length = 100)
    url = models.URLField()
    
class Address(models.Model):
    name = models.CharField(max_length = 100)
    address1 = models.CharField(max_length = 100)
    address2 = models.CharField(max_length = 100)
    city = models.CharField(max_length = 100)
    state = models.CharField(max_length = 100)
    zip = models.CharField(max_length = 100)    


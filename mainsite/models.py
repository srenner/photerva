from django.db import models
from django.contrib.auth.models import User
from django.db.models.fields.related import ForeignKey

#########PARENT CLASSES WE ARE MOST INTERESTED IN##########

class Location(models.Model):
    name = models.CharField(max_length=100)
    notes = models.TextField()
    user = models.ForeignKey(User)

class Customer(models.Model):
    name = models.CharField(max_length=100)
    notes = models.TextField()
    user = models.ForeignKey(User)

    def __str__(self):
        return self.name

class SessionType(models.Model):
    name = models.CharField(max_length=100)
    notes = models.TextField()
    base_price = models.DecimalField(max_digits=8, decimal_places=2)
    shoot_time = models.TimeField()
    edit_time = models.TimeField()
    user = models.ForeignKey(User)

class Session(models.Model):
    datetime = models.DateTimeField()
    backup_datetime = models.DateTimeField()
    notes = models.TextField()
    quoted_price = models.DecimalField(max_digits=8, decimal_places=2)
    final_price = models.DecimalField(max_digits=8, decimal_places=2)
    expenses = models.DecimalField(max_digits=8, decimal_places=2)
    shoot_time = models.TimeField()
    edit_time = models.TimeField()
    user = models.ForeignKey(User)

##########CHILD CLASSES##########

class Phone(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=25)
    ext = models.CharField(max_length=25, blank=True, null=True)
    location = models.ForeignKey('Location', blank=True, null=True)
    customer = models.ForeignKey('Customer', related_name='phones', blank=True, null=True)

class Email(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=200)
    location = models.ForeignKey('Location', blank=True, null=True)
    customer = models.ForeignKey('Customer', blank=True, null=True)

class Link(models.Model):
    name = models.CharField(max_length=100)
    url = models.URLField()
    location = models.ForeignKey('Location', blank=True, null=True)
    customer = models.ForeignKey('Customer', blank=True, null=True)
    session = models.ForeignKey('Session', blank=True, null=True)

class Address(models.Model):
    name = models.CharField(max_length=100)
    address1 = models.CharField(max_length=100)
    address2 = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zip = models.CharField(max_length=100)
    location = models.ForeignKey('Location', blank=True, null=True)
    customer = models.ForeignKey('Customer', blank=True, null=True)
    session = models.ForeignKey('Session', blank=True, null=True)

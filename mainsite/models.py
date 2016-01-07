from django.db import models
from django.contrib.auth.models import User
from django.db.models.fields.related import ForeignKey

#########PARENT CLASSES WE ARE MOST INTERESTED IN##########

class Customer(models.Model):
    name = models.CharField(max_length=100)
    notes = models.TextField()
    owner = models.ForeignKey(User)
    def __str__(self):
        return self.name

class SessionType(models.Model):
    name = models.CharField(max_length=100)
    notes = models.TextField()
    base_price = models.DecimalField(max_digits=8, decimal_places=2)
    shoot_time = models.TimeField()
    edit_time = models.TimeField()
    owner = models.ForeignKey(User)
    def __str__(self):
        return self.name + " ($" + str(self.base_price) + ")"

class Session(models.Model):
    datetime = models.DateTimeField()
    backup_datetime = models.DateTimeField(null=True, blank=True)
    notes = models.TextField()
    quoted_price = models.DecimalField(max_digits=8, decimal_places=2)
    final_price = models.DecimalField(max_digits=8, decimal_places=2)
    expenses = models.DecimalField(max_digits=8, decimal_places=2)
    shoot_time = models.TimeField()
    edit_time = models.TimeField()
    owner = models.ForeignKey(User)
    customer = models.ForeignKey('Customer')
    def __str__(self):
        return str(self.datetime)

##########CHILD CLASSES##########

class Phone(models.Model):
    phone = models.CharField(max_length=25)
    ext = models.CharField(max_length=25, blank=True, null=True)
    customer = models.ForeignKey('Customer', related_name='phones', blank=True, null=True)
    owner = models.ForeignKey(User)
    def __str__(self):
        return self.phone

class EmailAddress(models.Model):
    name = models.CharField(max_length=100)
    email_address = models.CharField(max_length=200)
    customer = models.ForeignKey('Customer', blank=True, null=True)
    owner = models.ForeignKey(User)
    class Meta:
        verbose_name_plural = "Email addresses"
    def __str__(self):
        return self.email_address

class Link(models.Model):
    name = models.CharField(max_length=100)
    url = models.URLField()
    customer = models.ForeignKey('Customer', blank=True, null=True)
    session = models.ForeignKey('Session', blank=True, null=True)
    owner = models.ForeignKey(User)
    def __str__(self):
        return self.name

class Address(models.Model):
    name = models.CharField(max_length=100)
    address1 = models.CharField(max_length=100)
    address2 = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zip = models.CharField(max_length=100)
    customer = models.ForeignKey('Customer', related_name='addresses', blank=True, null=True)
    session = models.ForeignKey('Session', related_name='addresses', blank=True, null=True)
    owner = models.ForeignKey(User)
    class Meta:
        verbose_name_plural = "Addresses"
    def __str__(self):
        return self.name

from django.contrib import admin
from .models import Customer, SessionType, Session
from .models import Phone, EmailAddress, Link, Address

admin.site.register(Customer)
admin.site.register(SessionType)
admin.site.register(Session)

admin.site.register(Phone)
admin.site.register(EmailAddress)
admin.site.register(Link)
admin.site.register(Address)

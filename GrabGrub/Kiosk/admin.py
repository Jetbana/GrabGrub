from django.contrib import admin
from .models import Food, Order, User, Customer
from django.contrib.admin.models import LogEntry

LogEntry.objects.all().delete()
admin.site.register(User)
admin.site.register(Customer)
admin.site.register(Food)
admin.site.register(Order)
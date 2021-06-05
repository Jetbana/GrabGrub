from django.db import models
from django.db.models.fields import DateTimeField
from django.utils import timezone

class User(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    objects = models.Manager()

    def __str__(self):
        return str(self.pk) + ": " + self.username

    def getUsername(self):
        return self.username
    
    def getPassword(self):
        return self.password

class Customer(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=300)
    city = models.CharField(max_length=300)

    def getName(self):
        return self.name

    def getAddress(self):
        return self.address

    def getCity(self):
        return self.city 

    def __str__(self):
        return str(self.pk) + ": " + self.name + " - " + self.city + ", " + self.address


class Food(models.Model):
    name = models.CharField(max_length=300)
    description = models.CharField(max_length=300)
    price = models.FloatField()
    created_at = DateTimeField(auto_now=True,blank=True, null=True)

    def getName(self):
        return self.name

    def getDesc(self):
        return self.description

    def getPrice(self):
        return str(self.price)

    def __str__(self):
        return str(self.pk) + ": " + self.name + " - P" + str(self.price) + ", " + self.description + ". Created at " + str(self.created_at)

class Order(models.Model):
    PAYMENT_OPTIONS =(
        ('CASH','Cash'),
        ('CARD','Card')
    )
    food = models.ForeignKey(Food, on_delete=models.CASCADE)
    qty = models.FloatField()
    ordered_at = models.DateTimeField(auto_now=True,blank=True,null=True)
    cust_order = models.ForeignKey(Customer, on_delete=models.CASCADE)
    payment_mode = models.CharField(max_length=4,choices=PAYMENT_OPTIONS)

    def getMode(self):
        return self.payment_mode

    def getQuantity(self):
        return str(self.qty)

    def __str__(self):
        return str(self.pk) + ": " + str(self.food) + "(" + str(self.qty) + "). For" + str(self.cust_order) + ". " + self.payment_mode + " ordered at " + str(self.ordered_at)


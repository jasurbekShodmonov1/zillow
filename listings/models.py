from django.db import models
from django.contrib.auth.models import User
from Users.models import CustomUser

class Property(models.Model):
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=50)
    zip_code = models.CharField(max_length=10)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    bedrooms = models.IntegerField()
    bathrooms = models.DecimalField(max_digits=3, decimal_places=1)
    sqft = models.IntegerField()
    image = models.ImageField(upload_to='property_images/')
    latitude = models.DecimalField(max_digits=9, decimal_places=6)
    longitude = models.DecimalField(max_digits=9, decimal_places=6)

class Listing(models.Model):
    TRANSACTION_TYPE_CHOICES = [
        ('buy', 'Buy'),
        ('rent', 'Rent'),
        ('sell', 'Sell'),
    ]
    property = models.ForeignKey(Property, on_delete=models.CASCADE)
    agent = models.ForeignKey(CustomUser, on_delete=models.CASCADE, default=0)
    transaction_type = models.CharField(max_length=4, choices=TRANSACTION_TYPE_CHOICES)
    list_date = models.DateTimeField(auto_now_add=True)
    is_published = models.BooleanField(default=False)

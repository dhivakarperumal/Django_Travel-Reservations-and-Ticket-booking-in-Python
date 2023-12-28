from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Booking(models.Model):
    name=models.CharField(max_length=200,null=False,blank=False)
    father_name=models.CharField(max_length=200)
    email=models.CharField(max_length=255)
    data_of_birth=models.CharField(max_length=255)
    age=models.IntegerField()
    gender=models.CharField(max_length=200)
    contact=models.CharField(max_length=12,null=False,blank=False)
    address=models.CharField(max_length=500)

    def __str__(self):
        return self.name
    

class Details(models.Model):
    destination_From=models.CharField(max_length=200,null=False,blank=False)
    destination_To=models.CharField(max_length=200,null=False,blank=False)
    dates=models.CharField(max_length=200)
    times=models.CharField(max_length=200)
    how_maney_peoples = models.IntegerField(default=0)
    kits=models.IntegerField(default=0)
    big_peoples=models.IntegerField(default=0)
    ac_non_ac=models.CharField(max_length=200)
    lover_upper_middle=models.CharField(max_length=200)
    

    def __str__(self):
        return self.name
    

class Payments(models.Model):
    upid=models.CharField(max_length=200,null=False,blank=False)
    payment_type_name=models.CharField(max_length=200,null=False,blank=False)
    transection_id=models.CharField(max_length=200)
    amount=models.CharField(max_length=200)
    send_monay_our_name=models.CharField(max_length=200)
    

    def __str__(self):
        return self.name




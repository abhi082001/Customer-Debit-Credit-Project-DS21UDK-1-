from django.db import models
from django.contrib.auth.models import User, auth

# Create your models here.
class customers(models.Model):
    Customer_ID = models.CharField(max_length=70)
    Customer_name = models.CharField(max_length=70)
    Phone_No = models.IntegerField()
    City = models.CharField(max_length=70)
    user = models.ForeignKey(User, on_delete = models.CASCADE)

class transactions(models.Model):
    Customer_ID = models.CharField(max_length=70)
    Amount = models.IntegerField()
    credit_or_debit =  models.CharField(max_length=70)
    Month =  models.CharField(max_length=70)
    Year = models.IntegerField()
    user = models.ForeignKey(User, on_delete = models.CASCADE)
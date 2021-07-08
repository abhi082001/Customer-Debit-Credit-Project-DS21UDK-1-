from django.db import models
from django.contrib.auth.models import User, auth

# Create your models here.
class Merchant(models.Model):
    Merchant_Name = models.CharField(max_length=70)
    Business_Name = models.CharField(max_length=70)
    GSTIN = models.CharField(max_length=70)
    user = models.CharField(max_length=70)

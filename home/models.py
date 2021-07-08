from django.db import models
from django.contrib.auth.models import User, auth
# Create your models here.
class sample(models.Model):
    
    user = models.ForeignKey(User, on_delete = models.CASCADE)


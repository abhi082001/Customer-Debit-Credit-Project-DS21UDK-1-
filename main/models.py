from django.db import models
from django.contrib.auth.models import User, auth

CD_choices= (
    ('Credit','Credit'),
    ('Debit','Debit')
)
Month_choices= (
    
    ('January','January'),
    ('February','February'),
    ('March', 'March'),
    ('April','April'),
    ('May','May'),
    ('June','June'),
    ('July','July'),
    ('August','August'),
    ('September','September'),
    ('October','October'),
    ('November','November'),
    ('December','December')
)
Year_choices = (
    (2020,2020),
    (2021,2021),
    (2022,2022),
    (2023,2023),
    (2024,2024),
    (2025,2025),
    (2026,2026),
    (2027,2027),
    (2028,2028),
    (2029,2029),
    (2030,2030),
    (2031,2031)
)
# Create your models here.
class customers(models.Model):
    Customer_ID = models.CharField(max_length=70)
    Customer_name = models.CharField(max_length=70)
    Phone_No = models.IntegerField()
    City = models.CharField(max_length=70)
    user = models.ForeignKey(User, on_delete = models.CASCADE)

class transactions(models.Model):
    CustomerID = models.CharField(max_length=70)
    Amount = models.IntegerField()
    credit_or_debit =  models.CharField(choices = CD_choices,max_length=70,default='Credit')
    Month =  models.CharField(max_length=70,choices = Month_choices)
    Year = models.IntegerField(choices = Year_choices)
    user = models.ForeignKey(User, on_delete = models.CASCADE)
from django.contrib import admin

# Register your models here.
from .models import customers, transactions
admin.site.register(customers)
admin.site.register(transactions)
from django import forms
from .models import customers, transactions
from accounts.models import Merchant

class customerentry(forms.ModelForm):
    class Meta:
        model = customers
        fields = ['Customer_name','Phone_No','City']
        
        widgets = {
            'Customer_name': forms.TextInput(attrs={'class':'form-control'}),
            'Phone_No': forms.NumberInput(attrs={'class':'form-control'}),
            'City': forms.TextInput(attrs={'class':'form-control'})
        }

class customertrans(forms.ModelForm):
    class Meta:
        model = transactions
        fields = ['Amount']
        
        widgets = {
            'Amount': forms.NumberInput(attrs={'class':'form-control'}),
            #'credit_or_debit': forms.TextInput(attrs={'class':'form-control'}),
            #'Month': forms.TextInput(attrs={'class':'form-control'}),
            #'Year': forms.NumberInput(attrs={'class':'form-control'}),
        }

class merchantupdate(forms.ModelForm):
    class Meta:
        model = Merchant
        fields = ['Merchant_Name','Business_Name','GSTIN']
        
        widgets = {
            'Merchant_Name': forms.TextInput(attrs={'class':'form-control'}),
            'Business_Name': forms.TextInput(attrs={'class':'form-control'}),
            'GSTIN': forms.TextInput(attrs={'class':'form-control'}),
            
        }

class customerupdate(forms.ModelForm):
    class Meta:
        model = customers
        fields = ['Customer_name','Phone_No','City']
        
        widgets = {
            'Customer_name': forms.TextInput(attrs={'class':'form-control'}),
            'Phone_No': forms.NumberInput(attrs={'class':'form-control'}),
            'City': forms.TextInput(attrs={'class':'form-control'})
        }

class transupdate(forms.ModelForm):
    class Meta:
        model = transactions
        fields = ['Amount','credit_or_debit','Month','Year']
        
        widgets = {
            'Amount': forms.NumberInput(attrs={'class':'form-control'}),
            'credit_or_debit': forms.TextInput(attrs={'class':'form-control'}),
            
        }
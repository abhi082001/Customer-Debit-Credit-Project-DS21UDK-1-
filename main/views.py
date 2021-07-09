from django.shortcuts import render, HttpResponseRedirect
from django.contrib.auth.models import User, auth
from .models import customers, transactions
from .forms import customerentry, customertrans 
from django.db.models import Sum
from .utils import get_plot_bar, get_plot_pie
from django.contrib import messages
from datetime import date
import datetime
import uuid

global val
def val():
    return None

def user_input(request):
    if request.method == 'POST':
        
        fm = customerentry(request.POST)
        if fm.is_valid():
            if request.user.is_authenticated:
                log_user = request.user
            else:
                return HttpResponseRedirect('accounts/login')
            test = uuid.uuid4()
            test = str(test)
            cn = fm.cleaned_data['Customer_name']
            pn = fm.cleaned_data['Phone_No']
            ci = fm.cleaned_data['City']
            reg = customers(Customer_ID=str(cn)+'-'+test[:6],Customer_name=cn,Phone_No=pn,City=ci,user=request.user)
            reg.save()
            fm = customerentry()
            stud = customers.objects.filter(user=log_user)
    
    else:
        fm = customerentry()
        if request.user.is_authenticated:
                log_user = request.user
        else:
            return HttpResponseRedirect('accounts/login')
        stud = customers.objects.filter(user=log_user)   

    sval = None 
    
    if request.GET.get('id'):
        
        sval = request.GET.get('id')
        #stud1 = stud.filter(Month=sval)
        global val
        def val():
            return sval 
    
    if sval!=None:
        return HttpResponseRedirect('cust_trans')
    return render(request,'cutomer_entry.html',{'form':fm,'stu':stud,'f':1})     
        
def cust_table(request):
    if request.user.is_authenticated:
        log_user = request.user
    else:
        return HttpResponseRedirect('accounts/login')
    
    stud = customers.objects.filter(user=log_user)
    stud = stud.order_by('Customer_name')   
    return render(request,'cust_table.html',{'stu':stud})

def cust_trans(request):
    if request.user.is_authenticated:
        log_user = request.user
    else:
        return HttpResponseRedirect('accounts/login')
    sval = val()
    stud = customers.objects.filter(user=log_user)
    stud1 = stud
    if sval!=None:
        stud1 = stud.filter(Customer_ID=sval)
        if len(stud1)==0:
            stud1 = stud
            stud1 = stud.filter(Customer_name=sval)
            if len(stud1)==0:
                stud1 = stud
                stud1 = stud.filter(City=sval)
    if sval=='all':
        stud1 = stud

    if request.method == 'POST':
        fm = customertrans(request.POST)
        if fm.is_valid():
            if request.user.is_authenticated:
                log_user = request.user
            else:
                return HttpResponseRedirect('accounts/login')
            
            am = fm.cleaned_data['Amount']
            cd = fm.cleaned_data['credit_or_debit']
            mo = fm.cleaned_data['Month']
            ye = fm.cleaned_data['Year']
            reg = transactions(Customer_ID=str(stud1.Customer_ID),Amount=am,credit_or_debit=cd,Month=mo,Year=ye,user=request.user)
            reg.save()
            fm = customertrans()
            stud_t = transactions.objects.filter(user=log_user)
    
    else:
        fm = customertrans()
        if request.user.is_authenticated:
                log_user = request.user
        else:
            return HttpResponseRedirect('accounts/login')
        stud = customers.objects.filter(user=log_user) 
    return render(request,'cust_trans.html',{'stu':stud1,'form':fm})  

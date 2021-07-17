from django.shortcuts import render, HttpResponseRedirect
from django.contrib.auth.models import User, auth
from .models import customers, transactions
from .forms import customerentry, customertrans, merchantupdate, customerupdate,transupdate
from accounts.models import Merchant
from django.db.models import Sum
from .utils1 import get_plot_bar, get_plot_pie, get_plot_line, get_plot_bar1, get_plot_line1,get_plot_count
from django.contrib import messages
from datetime import date
import datetime
import uuid
from .filters import OrderFilter, OrderFilter1, OrderFilter2,OrderFilter3

global val
def val():
    return -1
global v2
def v2():
    return -1
def user_input(request):
    if request.user.is_authenticated:
        log_user = request.user
    else:
        return HttpResponseRedirect('accounts/login')
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
            cn = cn.upper()
            ci = ci.upper()
            
            reg = customers(Customer_ID='CU'+test[:6],Customer_name=cn,Phone_No=pn,City=ci,user=request.user)
            reg.save()
            messages.info(request, 'Added successfilly')
            fm = customerentry()
            stud = customers.objects.filter(user=log_user)
    
    else:
        fm = customerentry()
        if request.user.is_authenticated:
                log_user = request.user
        else:
            return HttpResponseRedirect('accounts/login')
        stud = customers.objects.filter(user=log_user)   

    sval = -1
    
    if request.GET.get('id'):
        
        sval = request.GET.get('id')
        #stud1 = stud.filter(Month=sval)
        global val
        def val():
            return sval 
    
    if sval!=-1:
        return HttpResponseRedirect('cust_trans')
    if request.user.is_superuser:
        return render(request,'cutomer_entry.html',{'form':fm,'stu':stud,'f':1,'sval':sval})   
    return render(request,'cutomer_entry.html',{'form':fm,'stu':stud,'f':1})
        
def cust_table(request):
    if request.user.is_authenticated:
        log_user = request.user
    else:
        return HttpResponseRedirect('accounts/login')
    
    #stud = customers.objects.filter(user=log_user)
    stud = customers.objects.order_by('user','Customer_name')   
    return render(request,'cust_table.html',{'stu':stud})

def mycust_table(request):
    if request.user.is_authenticated:
        log_user = request.user
    else:
        return HttpResponseRedirect('accounts/login')
    
    stud = customers.objects.filter(user=log_user)
    stud = stud.order_by('Customer_name')   
    return render(request,'mycust_table.html',{'stu':stud})

def trans_table(request):
    if request.user.is_authenticated:
        log_user = request.user
    else:
        return HttpResponseRedirect('accounts/login')
    
    stud = transactions.objects.filter()
    myFilter = OrderFilter2(request.GET, queryset=stud)
    stud = myFilter.qs
    stud = stud.order_by('user','-Year','Month')
    s = ['All']
    if len(stud)>0:  
        s = [x.user for x in stud]
    if (request.GET.get('user')!= None and request.GET.get('user')!= ''):
        return render(request,'trans_table.html',{'myFilter':myFilter,'stu':stud,'s':str(s[0])+"'s"})
    return render(request,'trans_table.html',{'myFilter':myFilter,'stu':stud,'s':'All'})

def trans_table1(request):
    if request.user.is_authenticated:
        log_user = request.user
    else:
        return HttpResponseRedirect('accounts/login')
    
    stud = transactions.objects.filter()
    myFilter = OrderFilter2(request.GET, queryset=stud)
    stud = myFilter.qs
    stud = stud.order_by('user','-Year','Month')
    s = ['All']
    if len(stud)>0:  
        s = [x.user for x in stud]
    if (request.GET.get('user')!= None and request.GET.get('user')!= ''):
        return render(request,'trans_table1.html',{'myFilter':myFilter,'stu':stud,'s':str(s[0])+"'s"})
    return render(request,'trans_table1.html',{'myFilter':myFilter,'stu':stud,'s':'All'})

def cust_trans(request):
    if request.user.is_authenticated:
        log_user = request.user
    else:
        return HttpResponseRedirect('accounts/login')
    global v2
    def v2():
        return -1
    today = date.today()
    m=today.month
    d = today.day
    y = today.year
    datetime.datetime.now()
    sval = val()
    stud = customers.objects.filter()
    #if len(stud) == 0:
    #    return HttpResponseRedirect('user_input')
    stud1 = stud
    if sval!=-1:
        stud1 = stud.filter(Customer_ID=sval)
        if len(stud1)==0:
            sval = sval.upper()
            stud1 = stud
            stud1 = stud.filter(Customer_name=sval)
            if len(stud1)==0:
                stud1 = stud
                stud1 = stud.filter(City=sval)
    
    s = [str(x.Customer_ID) for x in stud1]
    if request.method == 'POST':
        
        savevalue2 = None        
        if request.POST.get('month'):
            
            savevalue2 = request.POST.get('month')

        savevalue3 = None        
        if request.POST.get('year'):
            
            savevalue3 = request.POST.get('year')
        
        savevalue4 = None   
        if request.POST.get('Credit') and request.POST.get('Debit'):
            messages.info(request, 'Please click on one of these buttons')
            return HttpResponseRedirect('/')

        elif request.POST.get('Debit'):
            
            savevalue4 = request.POST.get('Debit')     
        elif request.POST.get('Credit'):
            
            savevalue4 = request.POST.get('Credit')

        
        
        fm = customertrans(request.POST)
        if fm.is_valid():
            if request.user.is_authenticated:
                log_user = request.user
            else:
                return HttpResponseRedirect('accounts/login')
            
            am = fm.cleaned_data['Amount']
            #cd = fm.cleaned_data['credit_or_debit']
            #mo = fm.cleaned_data['Month']
            #ye = fm.cleaned_data['Year']
            if savevalue2!=None and savevalue3!=None and savevalue4!=None:
                messages.info(request, 'Added successfully')
                reg = transactions(CustomerID=s[0],Amount=am,credit_or_debit=savevalue4,Month=savevalue2,Year=savevalue3,user=request.user)
            else:
                messages.info(request, 'Please enter all values')
                return HttpResponseRedirect('cust_trans')
            reg.save()
            fm = customertrans()
            stud_t = transactions.objects.filter(user=log_user)
    
    else:
        fm = customertrans()
        if request.user.is_authenticated:
                log_user = request.user
        else:
            return HttpResponseRedirect('accounts/login')
    
    
    if len(stud1) == 1:
        
        stud_t = transactions.objects.filter(user=log_user)
        stud_1 = stud_t.filter(credit_or_debit = 'Debit')
        sum_debit = stud_1.aggregate(p1 = Sum('Amount'))
        stud_2 = stud_t.filter(credit_or_debit = 'Credit')
        sum_credit = stud_2.aggregate(p2 = Sum('Amount'))
        if sum_debit['p1'] == None:
            sum_debit['p1'] =0
        if sum_credit['p2'] == None:
            sum_credit['p2'] =0
        sum_diff = int(sum_debit['p1']) - int(sum_credit['p2'])

        stud_t = transactions.objects.filter()
        stud_t_1 = stud_t.filter(CustomerID = s[0])
        myFilter = OrderFilter(request.GET, queryset=stud_t_1)
        stud_t_1 = myFilter.qs
        stud_t_1 = stud_t_1.order_by('-Year','Month')
        stud_1 = stud_t_1.filter(credit_or_debit = 'Debit')
        sum_debit = stud_1.aggregate(p1 = Sum('Amount'))
        stud_2 = stud_t_1.filter(credit_or_debit = 'Credit')
        sum_credit = stud_2.aggregate(p2 = Sum('Amount'))
        if sum_debit['p1'] == None:
            sum_debit['p1'] =0
        if sum_credit['p2'] == None:
            sum_credit['p2'] =0
        sum_diff_1 = int(sum_debit['p1']) - int(sum_credit['p2'])

        stud_t = transactions.objects.filter(user=log_user)
        stud_t_1_ = stud_t.filter(CustomerID = s[0])
        myFilter = OrderFilter(request.GET, queryset=stud_t_1_)
        stud_t_1_ = myFilter.qs
        #stud_t_1 = stud_t_1.order_by('-Year','Month')
        stud_1 = stud_t_1_.filter(credit_or_debit = 'Debit')
        sum_debit = stud_1.aggregate(p1 = Sum('Amount'))
        stud_2 = stud_t_1_.filter(credit_or_debit = 'Credit')
        sum_credit = stud_2.aggregate(p2 = Sum('Amount'))
        if sum_debit['p1'] == None:
            sum_debit['p1'] =0
        if sum_credit['p2'] == None:
            sum_credit['p2'] =0
        sum_diff_2 = int(sum_debit['p1']) - int(sum_credit['p2'])
        if request.POST.get('AllT'):
            fm = customertrans()
            if (request.GET.get('Month')!= None and request.GET.get('Month')!= '') and (request.GET.get('Year')== None or request.GET.get('Year')== ''):
                return render(request,'cust_trans1.html',{'myFilter':myFilter,'stu':stud1,'form':fm,'diff':sum_diff,'diff1':sum_diff_1,'diff2':sum_diff_2,'stut':stud_t_1,'f':int(m),'y':int(y),'s':'**No record in this month/year','m':request.GET.get('Month') + ' month','x':1})
            elif (request.GET.get('Month')== None and request.GET.get('Month')== '') and (request.GET.get('Year')!= None or request.GET.get('Year')!= ''):
                return render(request,'cust_trans1.html',{'myFilter':myFilter,'stu':stud1,'form':fm,'diff':sum_diff,'diff1':sum_diff_1,'stut':stud_t_1,'diff2':sum_diff_2,'f':int(m),'y':int(y),'s':'**No record in this month/year','m':request.GET.get('Year') + ' year','x':1})
            elif (request.GET.get('Year')!= None and request.GET.get('Year')!= '') and (request.GET.get('Month')!= None and request.GET.get('Month')!= ''):
                return render(request,'cust_trans1.html',{'myFilter':myFilter,'stu':stud1,'form':fm,'diff':sum_diff,'diff1':sum_diff_1,'stut':stud_t_1,'diff2':sum_diff_2,'f':int(m),'y':int(y),'s':'**No record in this month/year','m':request.GET.get('Month') + ' month and '+request.GET.get('Year') + ' year','x':1})
            else:
                return render(request,'cust_trans1.html',{'myFilter':myFilter,'stu':stud1,'form':fm,'diff':sum_diff,'diff1':sum_diff_1,'diff2':sum_diff_2,'stut':stud_t_1,'f':int(m),'y':int(y),'s':"**No record in this month/year",'m': 'All','x':1})
        else:
            if (request.GET.get('Month')!= None and request.GET.get('Month')!= '') and (request.GET.get('Year')== None or request.GET.get('Year')== ''):
                return render(request,'cust_trans1.html',{'myFilter':myFilter,'stu':stud1,'form':fm,'diff':sum_diff,'diff1':sum_diff_1,'diff2':sum_diff_2,'f':int(m),'y':int(y),'s':"**Click on 'Customer's All Transactions' button",'m':request.GET.get('Month') + ' month','x':1})
            elif (request.GET.get('Month')== None and request.GET.get('Month')== '') and (request.GET.get('Year')!= None or request.GET.get('Year')!= ''):
                    return render(request,'cust_trans1.html',{'myFilter':myFilter,'stu':stud1,'form':fm,'diff':sum_diff,'diff1':sum_diff_1,'diff2':sum_diff_2,'f':int(m),'y':int(y),'s':"**Click on 'Customer's All Transactions' button",'m':request.GET.get('Year') + ' year','x':1})
            elif (request.GET.get('Year')!= None and request.GET.get('Year')!= '') and (request.GET.get('Month')!= None and request.GET.get('Month')!= ''):
                    return render(request,'cust_trans1.html',{'myFilter':myFilter,'stu':stud1,'form':fm,'diff':sum_diff,'diff1':sum_diff_1,'diff2':sum_diff_2,'f':int(m),'y':int(y),'s':"**Click on 'Customer's All Transactions' button",'m':request.GET.get('Month') + ' month and '+request.GET.get('Year') + ' year','x':1})
            else:
                    return render(request,'cust_trans1.html',{'myFilter':myFilter,'stu':stud1,'form':fm,'diff':sum_diff,'diff1':sum_diff_1,'diff2':sum_diff_2,'f':int(m),'y':int(y),'s':"**Click on 'Customer's All Transactions' button",'m': 'All','x':1})
            return render(request,'cust_trans1.html',{'myFilter':myFilter,'stu':stud1,'form':fm,'diff':sum_diff,'diff1':sum_diff_1,'diff2':sum_diff_2, 'f':int(m),'y':int(y),'s':"**Click on 'Customer's All Transactions' button",'x':1}) 
    if sval == -1:
        return HttpResponseRedirect('user_input')
    return render(request,'cust_trans.html',{'stu':stud1})  

def cust_trans1(request,sval):
    if request.user.is_authenticated:
        log_user = request.user
    else:
        return HttpResponseRedirect('accounts/login')
    today = date.today()
    m=today.month
    d = today.day
    y = today.year
    datetime.datetime.now()
    stud = customers.objects.filter()
    stud1 = stud
    global v2
    def v2():
        return sval
    if sval!=None:
        stud1 = stud.filter(Customer_ID=sval)
        if len(stud1)==0:
            sval = sval.upper()
            stud1 = stud
            stud1 = stud.filter(Customer_name=sval)
            if len(stud1)==0:
                stud1 = stud
                stud1 = stud.filter(City=sval)
    if sval=='all':
        stud1 = stud
    s = [str(x.Customer_ID) for x in stud1]
    if request.method == 'POST':
        savevalue2 = None        
        if request.POST.get('month'):
            
            savevalue2 = request.POST.get('month')

        savevalue3 = None        
        if request.POST.get('year'):
            
            savevalue3 = request.POST.get('year')
        savevalue4 = None   
        if request.POST.get('Credit') and request.POST.get('Debit'):
            messages.info(request, 'Please click on one of these buttons')
            return HttpResponseRedirect('/') 
        
        elif request.POST.get('Debit'):
            
            savevalue4 = request.POST.get('Debit')
            
        elif request.POST.get('Credit'):
            
            savevalue4 = request.POST.get('Credit')
        
        

        fm = customertrans(request.POST)
        if fm.is_valid():
            
            
            am = fm.cleaned_data['Amount']
            #cd = fm.cleaned_data['credit_or_debit']
            #mo = fm.cleaned_data['Month']
            #ye = fm.cleaned_data['Year']
            if savevalue2!=None and savevalue3!=None and savevalue4!=None:
                messages.info(request, 'Added successfully')
                reg = transactions(CustomerID=s[0],Amount=am,credit_or_debit=savevalue4,Month=savevalue2,Year=savevalue3,user=request.user)
            reg.save()
            fm = customertrans()
            stud_t = transactions.objects.filter(user=log_user)
    
    else:
        fm = customertrans()
        if request.user.is_authenticated:
            log_user = request.user
        else:
            return HttpResponseRedirect('accounts/login')
    
    stud_t = transactions.objects.filter(user=log_user)
    stud_1 = stud_t.filter(credit_or_debit = 'Debit')
    sum_debit = stud_1.aggregate(p1 = Sum('Amount'))
    stud_2 = stud_t.filter(credit_or_debit = 'Credit')
    sum_credit = stud_2.aggregate(p2 = Sum('Amount'))
    if sum_debit['p1'] == None:
        sum_debit['p1'] =0
    if sum_credit['p2'] == None:
        sum_credit['p2'] =0
    sum_diff = int(sum_debit['p1']) - int(sum_credit['p2'])

    stud_t = transactions.objects.filter()
    stud_t_1 = stud_t.filter(CustomerID = sval)
    myFilter = OrderFilter(request.GET, queryset=stud_t_1)
    stud_t_1 = myFilter.qs
    stud_t_1 = stud_t_1.order_by('-Year','Month')

    stud_1 = stud_t_1.filter(credit_or_debit = 'Debit')
    sum_debit = stud_1.aggregate(p1 = Sum('Amount'))
    stud_2 = stud_t_1.filter(credit_or_debit = 'Credit')
    sum_credit = stud_2.aggregate(p2 = Sum('Amount'))
    if sum_debit['p1'] == None:
            sum_debit['p1'] =0
    if sum_credit['p2'] == None:
            sum_credit['p2'] =0
    sum_diff_1 = int(sum_debit['p1']) - int(sum_credit['p2'])

    stud_t = transactions.objects.filter(user=log_user)
    stud_t_1_ = stud_t.filter(CustomerID = s[0])
    myFilter = OrderFilter(request.GET, queryset=stud_t_1_)
    stud_t_1_ = myFilter.qs
        #stud_t_1 = stud_t_1.order_by('-Year','Month')
    stud_1 = stud_t_1_.filter(credit_or_debit = 'Debit')
    sum_debit = stud_1.aggregate(p1 = Sum('Amount'))
    stud_2 = stud_t_1_.filter(credit_or_debit = 'Credit')
    sum_credit = stud_2.aggregate(p2 = Sum('Amount'))
    if sum_debit['p1'] == None:
            sum_debit['p1'] =0
    if sum_credit['p2'] == None:
            sum_credit['p2'] =0
    sum_diff_2 = int(sum_debit['p1']) - int(sum_credit['p2'])
    
    if request.POST.get('AllT'):
        fm = customertrans()
        if (request.GET.get('Month')!= None and request.GET.get('Month')!= '') and (request.GET.get('Year')== None or request.GET.get('Year')== ''):
            return render(request,'cust_trans1.html',{'myFilter':myFilter,'stu':stud1,'form':fm,'diff':sum_diff,'diff1':sum_diff_1,'diff2':sum_diff_2,'stut':stud_t_1,'f':int(m),'y':int(y),'s':'**No record in this month/year','m':request.GET.get('Month') + ' month'})
        elif (request.GET.get('Month')== None and request.GET.get('Month')== '') and (request.GET.get('Year')!= None or request.GET.get('Year')!= ''):
            return render(request,'cust_trans1.html',{'myFilter':myFilter,'stu':stud1,'form':fm,'diff':sum_diff,'diff1':sum_diff_1,'diff2':sum_diff_2,'stut':stud_t_1,'f':int(m),'y':int(y),'s':'**No record in this month/year','m':request.GET.get('Year') + ' year'})
        elif (request.GET.get('Year')!= None and request.GET.get('Year')!= '') and (request.GET.get('Month')!= None and request.GET.get('Month')!= ''):
            return render(request,'cust_trans1.html',{'myFilter':myFilter,'stu':stud1,'form':fm,'diff':sum_diff,'diff1':sum_diff_1,'diff2':sum_diff_2,'stut':stud_t_1,'f':int(m),'y':int(y),'s':'**No record in this month/year','m':request.GET.get('Month') + ' month and '+request.GET.get('Year') + ' year'})
        else:
            return render(request,'cust_trans1.html',{'myFilter':myFilter,'stu':stud1,'form':fm,'diff':sum_diff,'diff1':sum_diff_1,'diff2':sum_diff_2,'stut':stud_t_1,'f':int(m),'y':int(y),'s':'**No record in this month/year','m': 'All'})
    else:
            if (request.GET.get('Month')!= None and request.GET.get('Month')!= '') and (request.GET.get('Year')== None or request.GET.get('Year')== ''):
                return render(request,'cust_trans1.html',{'myFilter':myFilter,'stu':stud1,'form':fm,'diff':sum_diff,'diff1':sum_diff_1,'diff2':sum_diff_2,'f':int(m),'y':int(y),'s':"**Click on 'Customer's All Transactions' button",'m':request.GET.get('Month') + ' month'})
            elif (request.GET.get('Month')== None and request.GET.get('Month')== '') and (request.GET.get('Year')!= None or request.GET.get('Year')!= ''):
                    return render(request,'cust_trans1.html',{'myFilter':myFilter,'stu':stud1,'form':fm,'diff':sum_diff,'diff1':sum_diff_1,'diff2':sum_diff_2,'f':int(m),'y':int(y),'s':"**Click on 'Customer's All Transactions' button",'m':request.GET.get('Year') + ' year'})
            elif (request.GET.get('Year')!= None and request.GET.get('Year')!= '') and (request.GET.get('Month')!= None and request.GET.get('Month')!= ''):
                    return render(request,'cust_trans1.html',{'myFilter':myFilter,'stu':stud1,'form':fm,'diff':sum_diff,'diff1':sum_diff_1,'diff2':sum_diff_2,'f':int(m),'y':int(y),'s':"**Click on 'Customer's All Transactions' button",'m':request.GET.get('Month') + ' month and '+request.GET.get('Year') + ' year'})
            else:
                    return render(request,'cust_trans1.html',{'myFilter':myFilter,'stu':stud1,'form':fm,'diff':sum_diff,'diff1':sum_diff_1,'diff2':sum_diff_2,'f':int(m),'y':int(y),'s':"**Click on 'Customer's All Transactions' button",'m': 'All'})
            return render(request,'cust_trans1.html',{'myFilter':myFilter,'stu':stud1,'form':fm,'diff':sum_diff,'diff1':sum_diff_1, 'diff2':sum_diff_2,'f':int(m),'y':int(y),'s':"**Click on 'Customer's All Transactions' button"}) 
    #return render(request,'cust_trans1.html',{'myFilter':myFilter,'stu':stud1,'form':fm,'diff':sum_diff,'diff1':sum_diff_1,'f':int(m),'y':int(y),'s':"**Click on 'All Transactions' button"})

def merch_page(request):
    if request.user.is_authenticated:
        log_user = request.user
    else:
        return HttpResponseRedirect('accounts/login')
    
    stud1 = Merchant.objects.filter(user=log_user)
    stud2 = customers.objects.filter(user=log_user)
    stud2 = stud2.order_by('Customer_name')  
    if request.POST.get('AllC'):
        return render(request, 'merchant_page.html', {'stu1':stud1,'stu2':stud2,'s':'No record'})
    if request.POST.get('AllM'):
        stud2 = customers.objects.filter()
        stud2 = stud2.order_by('user','Customer_name')  
        return render(request, 'merchant_page.html', {'stu1':stud1,'stu2':stud2,'s':'No record'})
    return render(request, 'merchant_page.html', {'stu1':stud1})

def updatedata(request,id):
    if request.user.is_authenticated:
        log_user = request.user
    else:
        return HttpResponseRedirect('accounts/login')
    if request.method == 'POST':
        pi  = Merchant.objects.get(pk = id)
        fm1 = merchantupdate(request.POST, instance = pi)
        if fm1.is_valid():
            fm1.save()
            messages.info(request, 'Updated successfully')
    else:
        pi  = Merchant.objects.get(pk = id)
        fm1 = merchantupdate(instance = pi)
    return render(request,'update.html', {'form':fm1})

def updatedata1(request,id):
    if request.user.is_authenticated:
        log_user = request.user
    else:
        return HttpResponseRedirect('accounts/login')
    if request.method == 'POST':
        pi  = customers.objects.get(pk = id)
        fm1 = customerupdate(request.POST, instance = pi)
        if fm1.is_valid():
            fm1.save()
            messages.info(request, 'Updated successfully')
    else:
        pi  = customers.objects.get(pk = id)
        fm1 = customerupdate(instance = pi)
    return render(request,'update1.html', {'form':fm1})

def updatedata_1(request,id):
    if request.user.is_authenticated:
        log_user = request.user
    else:
        return HttpResponseRedirect('accounts/login')
    if request.method == 'POST':
        pi  = customers.objects.get(pk = id)
        fm1 = customerupdate(request.POST, instance = pi)
        if fm1.is_valid():
            fm1.save()
            messages.info(request, 'Updated successfully')
    else:
        pi  = customers.objects.get(pk = id)
        fm1 = customerupdate(instance = pi)
    return render(request,'update_1.html', {'form':fm1})

def updatedata2(request,id):
    if request.user.is_authenticated:
        log_user = request.user
    else:
        return HttpResponseRedirect('accounts/login')
    if request.method == 'POST':
        pi  = customers.objects.get(pk = id)
        fm1 = customerupdate(request.POST, instance = pi)
        if fm1.is_valid():
            fm1.save()
            messages.info(request, 'Updated successfully')
    else:
        pi  = customers.objects.get(pk = id)
        fm1 = customerupdate(instance = pi)
    return render(request,'update2.html', {'form':fm1})

def updatedata3(request,id):
    if request.user.is_authenticated:
        log_user = request.user
    else:
        return HttpResponseRedirect('accounts/login')
    if request.method == 'POST':
        pi  = transactions.objects.get(pk = id)
        fm1 = transupdate(request.POST, instance = pi)
        if fm1.is_valid():
            fm1.save()
            messages.info(request, 'Updated successfully')
    else:
        pi  = transactions.objects.get(pk = id)
        fm1 = transupdate(instance = pi)
    sval = str(v2())
    return render(request,'update3.html', {'form':fm1,'sval':sval})

def analytics(request):
    if request.user.is_authenticated:
        log_user = request.user
    else:
        return HttpResponseRedirect('accounts/login')
    return render(request, 'analytics.html',{'d':"**select either 'montly' or 'yearly' button to view the respective graphs"})

def analytics_m(request):
    if request.user.is_authenticated:
        log_user = request.user
    else:
        return HttpResponseRedirect('accounts/login')
    #monthly
    if request.user.is_superuser:
        stud = transactions.objects.filter()
        myFilter3 = OrderFilter3(request.GET, queryset=stud)
        stud = myFilter3.qs
        myFilter1 = OrderFilter1(request.GET, queryset=stud)
        stud = myFilter1.qs
    else:
        stud = transactions.objects.filter(user=log_user)
        myFilter1 = OrderFilter1(request.GET, queryset=stud)
        stud = myFilter1.qs
    l=[' ']
    ds = "No record of credit/debit"
    if len(stud)>0:
        ds = "** select one of these three buttons **"
        l = [str(x.user) for x in stud]
    stud_1 = stud.filter(credit_or_debit = 'Credit')
    stud_2 = stud.filter(credit_or_debit = 'Debit')
    P = [x.Month for x in stud_1]
    Q = [int(y.Amount) for y in stud_1]
    p1 = [x.Month for x in stud_2]
    q1 = [int(y.Amount) for y in stud_2]

    d ={}
    for x in P:
        d[x]=0
    i=0
    for x in P:
        d[x] = d[x]+Q[i]
        i+=1
    P = list(d.keys())
    
    Q = list(d.values())

    d1 ={}
    for x in p1:
        d1[x]=0
    i=0
    for x in p1:
        d1[x] = d1[x]+q1[i]
        i+=1
    p1 = list(d1.keys())
    q1 = list(d1.values())

    s_p = set(P)
    s_p1 = set(p1)
    Pup = s_p.union(s_p1)
    Pup = list(Pup)
    d3 = {}
    for k in Pup:
        if (k in P) and (k in p1):
            d3[k] = d1[k]-d[k]
        elif k in P:
            d3[k] = -d[k]
        elif k in p1:
            d3[k] = d1[k]
    p2 = list(d3.keys())
    q2 = list(d3.values()) 
    
    chart1 = get_plot_bar(P,Q,'Credit Amount (rupees)','Months')
    chart2 = get_plot_bar(p1,q1,'Debit Amount (rupees)','Months')
    chart3 = get_plot_bar(p2,q2,'Balance Amount (rupees)','Months')

    chart_1 = get_plot_pie(P,Q)
    chart_2 = get_plot_pie(p1,q1)
    chart_3 = get_plot_pie(['Credit','Debit'],[sum(Q),sum(q1)])
    chart_4 = get_plot_line1(p2,q2,'Balance Amount (rupees)','Months')
    if request.user.is_superuser:
        if (request.GET.get('user')!= None and request.GET.get('user')!= ''):
            if request.POST.get('Credit1'):
                if (request.GET.get('Year')!= None and request.GET.get('Year')!= ''):
                    return render(request,'analytics_month.html',{'myFilter1':myFilter1,'myFilter3':myFilter3,'stu':stud_1,'chart':chart1,'d':'No record of credit','m':request.GET.get('Year')+" year's Monthly Credit bar plot",'l':l[0]})
                return render(request,'analytics_month.html',{'myFilter1':myFilter1,'myFilter3':myFilter3,'stu':stud_1,'chart':chart1,'d':'No record of credit','m':'Monthly Credit bar plot (all years)','l':l[0]})
            if request.POST.get('Debit1'):
                if (request.GET.get('Year')!= None and request.GET.get('Year')!= ''):
                    return render(request,'analytics_month.html',{'myFilter1':myFilter1,'myFilter3':myFilter3,'stu':stud_2,'chart':chart2,'d':'No record of debit','m':request.GET.get('Year')+" year's Montly Debit bar plot",'l':l[0]})
                return render(request,'analytics_month.html',{'myFilter1':myFilter1,'myFilter3':myFilter3,'stu':stud_2,'chart':chart2,'d':'No record of debit','m':"Montly Debit bar plot (all years)",'l':l[0]})
            if request.POST.get('Balance1'):
                if (request.GET.get('Year')!= None and request.GET.get('Year')!= ''):
                    return render(request,'analytics_month.html',{'myFilter1':myFilter1,'myFilter3':myFilter3,'stu':stud,'chart':chart3,'d':'No record of credit/debit','m':request.GET.get('Year')+" year's Monthly Balance bar plot",'l':l[0]})
                return render(request,'analytics_month.html',{'myFilter1':myFilter1,'myFilter3':myFilter3,'stu':stud,'chart':chart3,'d':'No record of credit/debit','m':"Monthly Balance bar plot (all years)",'l':l[0]})
            if request.POST.get('Credit2'):
                if (request.GET.get('Year')!= None and request.GET.get('Year')!= ''):
                    return render(request,'analytics_month.html',{'myFilter1':myFilter1,'myFilter3':myFilter3,'stu':stud_1,'chart':chart_1,'d':'No record of credit','m':request.GET.get('Year')+" year's Monthly Credit percent plot",'l':l[0]})
                return render(request,'analytics_month.html',{'myFilter1':myFilter1,'myFilter3':myFilter3,'stu':stud_1,'chart':chart_1,'d':'No record of credit','m':'Monthly Credit percent plot (all years)','l':l[0]})
            if request.POST.get('Debit2'):
                if (request.GET.get('Year')!= None and request.GET.get('Year')!= ''):
                    return render(request,'analytics_month.html',{'myFilter1':myFilter1,'myFilter3':myFilter3,'stu':stud_2,'chart':chart_2,'d':'No record of debit','m':request.GET.get('Year')+" year's Montly Debit percent plot",'l':l[0]})
                return render(request,'analytics_month.html',{'myFilter1':myFilter1,'myFilter3':myFilter3,'stu':stud_2,'chart':chart_2,'d':'No record of debit','m':"Montly Debit percent plot (all years)",'l':l[0]})
            if request.POST.get('Balance2'):
                if (request.GET.get('Year')!= None and request.GET.get('Year')!= ''):
                    return render(request,'analytics_month.html',{'myFilter1':myFilter1,'myFilter3':myFilter3,'stu':stud,'chart':chart_3,'d':'No record of credit/debit','m':request.GET.get('Year')+" year's Debit-Credit percent in Balance",'l':l[0]})
                return render(request,'analytics_month.html',{'myFilter1':myFilter1,'myFilter3':myFilter3,'stu':stud,'chart':chart_3,'d':'No record of credit/debit','m':"Debit-Credit percent in Balance",'l':l[0]})
            if request.POST.get('Trend'):
                if (request.GET.get('Year')!= None and request.GET.get('Year')!= ''):
                    return render(request,'analytics_month.html',{'myFilter1':myFilter1,'myFilter3':myFilter3,'stu':stud,'chart':chart_4,'d':'No record of credit/debit','m':request.GET.get('Year')+" year's month wise balance trend",'l':l[0]})
                return render(request,'analytics_month.html',{'myFilter1':myFilter1,'myFilter3':myFilter3,'stu':stud,'chart':chart_4,'d':'No record of credit/debit','m':'Month wise balance trend','l':l[0]})

            else:
                return render(request,'analytics_month.html',{'myFilter1':myFilter1,'myFilter3':myFilter3,'d':ds,'chart':False,'l':l[0]})
        else:
            return render(request,'analytics_month.html',{'myFilter1':myFilter1,'myFilter3':myFilter3,'d':"** Select a merchant from merchant filter **",'chart':False})
    else:
        if request.POST.get('Credit1'):
                if (request.GET.get('Year')!= None and request.GET.get('Year')!= ''):
                    return render(request,'analytics_month.html',{'myFilter1':myFilter1,'stu':stud_1,'chart':chart1,'d':'No record of credit','m':request.GET.get('Year')+" year's Monthly Credit bar plot"})
                return render(request,'analytics_month.html',{'myFilter1':myFilter1,'stu':stud_1,'chart':chart1,'d':'No record of credit','m':'Monthly Credit bar plot (all years)'})
        if request.POST.get('Debit1'):
                if (request.GET.get('Year')!= None and request.GET.get('Year')!= ''):
                    return render(request,'analytics_month.html',{'myFilter1':myFilter1,'stu':stud_2,'chart':chart2,'d':'No record of debit','m':request.GET.get('Year')+" year's Montly Debit bar plot"})
                return render(request,'analytics_month.html',{'myFilter1':myFilter1,'stu':stud_2,'chart':chart2,'d':'No record of debit','m':"Montly Debit bar plot (all years)"})
        if request.POST.get('Balance1'):
                if (request.GET.get('Year')!= None and request.GET.get('Year')!= ''):
                    return render(request,'analytics_month.html',{'myFilter1':myFilter1,'stu':stud,'chart':chart3,'d':'No record of credit/debit','m':request.GET.get('Year')+" year's Monthly Balance bar plot"})
                return render(request,'analytics_month.html',{'myFilter1':myFilter1,'stu':stud,'chart':chart3,'d':'No record of credit/debit','m':"Monthly Balance bar plot (all years)"})
        if request.POST.get('Credit2'):
                if (request.GET.get('Year')!= None and request.GET.get('Year')!= ''):
                    return render(request,'analytics_month.html',{'myFilter1':myFilter1,'stu':stud_1,'chart':chart_1,'d':'No record of credit','m':request.GET.get('Year')+" year's Monthly Credit percent plot"})
                return render(request,'analytics_month.html',{'myFilter1':myFilter1,'stu':stud_1,'chart':chart_1,'d':'No record of credit','m':'Monthly Credit percent plot (all years)'})
        if request.POST.get('Debit2'):
                if (request.GET.get('Year')!= None and request.GET.get('Year')!= ''):
                    return render(request,'analytics_month.html',{'myFilter1':myFilter1,'stu':stud_2,'chart':chart_2,'d':'No record of debit','m':request.GET.get('Year')+" year's Montly Debit percent plot"})
                return render(request,'analytics_month.html',{'myFilter1':myFilter1,'stu':stud_2,'chart':chart_2,'d':'No record of debit','m':"Montly Debit percent plot (all years)"})
        if request.POST.get('Balance2'):
                if (request.GET.get('Year')!= None and request.GET.get('Year')!= ''):
                    return render(request,'analytics_month.html',{'myFilter1':myFilter1,'stu':stud,'chart':chart_3,'d':'No record of credit/debit','m':request.GET.get('Year')+" year's Debit-Credit percent in Balance"})
                return render(request,'analytics_month.html',{'myFilter1':myFilter1,'stu':stud,'chart':chart_3,'d':'No record of credit/debit','m':"Debit-Credit percent in Balance"})
        if request.POST.get('Trend'):
                if (request.GET.get('Year')!= None and request.GET.get('Year')!= ''):
                    return render(request,'analytics_month.html',{'myFilter1':myFilter1,'stu':stud,'chart':chart_4,'d':'No record of credit/debit','m':request.GET.get('Year')+" year's month wise balance trend"})
                return render(request,'analytics_month.html',{'myFilter1':myFilter1,'stu':stud,'chart':chart_4,'d':'No record of credit/debit','m':'Month wise balance trend'})

        else:
                return render(request,'analytics_month.html',{'myFilter1':myFilter1,'d':ds,'chart':False})

def analytics_y(request):
    if request.user.is_authenticated:
        log_user = request.user
    else:
        return HttpResponseRedirect('accounts/login')
    #monthly
    if request.user.is_superuser:
        stud = transactions.objects.filter()
        myFilter3 = OrderFilter3(request.GET, queryset=stud)
        stud = myFilter3.qs
        
    else:
        stud = transactions.objects.filter(user=log_user)
    l=[' ']
    ds = "No record of credit/debit"
    if len(stud)>0:
        ds = "** select one of these three buttons **"
        l = [str(x.user) for x in stud]
    
    #stud = transactions.objects.filter(user=log_user)
    stud_1 = stud.filter(credit_or_debit = 'Credit')
    stud_2 = stud.filter(credit_or_debit = 'Debit')
    P = [int(x.Year) for x in stud_1]
    Q = [int(y.Amount) for y in stud_1]
    p1 = [int(x.Year) for x in stud_2]
    q1 = [int(y.Amount) for y in stud_2]

    d ={}
    for x in P:
        x=int(x)
        d[x]=0
    i=0
    for x in P:
        d[x] = d[x]+Q[i]
        i+=1
    P = list(d.keys())
    
    Q = list(d.values())

    d1 ={}
    for x in p1:
        x=int(x)
        d1[x]=0
    i=0
    for x in p1:
        d1[x] = d1[x]+q1[i]
        i+=1
    p1 = list(d1.keys())
    q1 = list(d1.values())

    s_p = set(P)
    s_p1 = set(p1)
    Pup = s_p.union(s_p1)
    Pup = list(Pup)
    d3 = {}
    for k in Pup:
        if (k in P) and (k in p1):
            d3[k] = d1[k]-d[k]
        elif k in P:
            d3[k] = -d[k]
        elif k in p1:
            d3[k] = d1[k]
    p2 = list(d3.keys())
    q2 = list(d3.values()) 

    chart1 = get_plot_bar1(P,Q,'Credit Amount (rupees)','Years')
    chart2 = get_plot_bar1(p1,q1,'Debit Amount (rupees)','Years')
    chart3 = get_plot_bar1(p2,q2,'Balance Amount (rupees)','Years')
    
    chart_1 = get_plot_pie(P,Q)
    chart_2 = get_plot_pie(p1,q1)
    chart_3 = get_plot_pie(['Credit','Debit'],[sum(Q),sum(q1)])
    chart_4 = get_plot_line(p2,q2,'Balance Amount (rupees)','Years')
    if request.user.is_superuser:
        if (request.GET.get('user')!= None and request.GET.get('user')!= ''):
            if request.POST.get('Credit1'):
                return render(request,'analytics_year.html',{'myFilter3':myFilter3,'stu':stud_1,'chart':chart1,'d':'No record of credit','m':'Yearly Credit bar plot','l':l[0]})
            elif request.POST.get('Debit1'):
                return render(request,'analytics_year.html',{'myFilter3':myFilter3,'stu':stud_2,'chart':chart2,'d':'No record of debit','m':'Yearly Debit bar plot','l':l[0]})
            if request.POST.get('Balance1'):
                return render(request,'analytics_year.html',{'myFilter3':myFilter3,'stu':stud,'chart':chart3,'d':'No record of credit/debit','m':'Yearly Balance bar plot','l':l[0]})
            if request.POST.get('Credit2'):
                return render(request,'analytics_year.html',{'myFilter3':myFilter3,'stu':stud_1,'chart':chart_1,'d':'No record of credit','m':'Yearly Credit percent plot','l':l[0]})
            elif request.POST.get('Debit2'):
                return render(request,'analytics_year.html',{'myFilter3':myFilter3,'stu':stud_2,'chart':chart_2,'d':'No record of debit','m':'Yearly Debit percent plot','l':l[0]})
            if request.POST.get('Balance2'):
                return render(request,'analytics_year.html',{'myFilter3':myFilter3,'stu':stud,'chart':chart_3,'d':'No record of credit/debit','m':'Debit-Credit percent in Balance','l':l[0]})
            if request.POST.get('Trend'):
                return render(request,'analytics_year.html',{'myFilter3':myFilter3,'stu':stud,'chart':chart_4,'d':'No record of credit/debit','m':'Year wise balance trend','l':l[0]})
            else:
                return render(request,'analytics_year.html',{'myFilter3':myFilter3,'d':ds,'chart':False,'l':l[0]})
        else:
            return render(request,'analytics_year.html',{'myFilter3':myFilter3,'d':"** select user from merchant filter **",'chart':False})
    else:
        if request.POST.get('Credit1'):
                return render(request,'analytics_year.html',{'stu':stud_1,'chart':chart1,'d':'No record of credit','m':'Yearly Credit bar plot'})
        elif request.POST.get('Debit1'):
                return render(request,'analytics_year.html',{'stu':stud_2,'chart':chart2,'d':'No record of debit','m':'Yearly Debit bar plot'})
        if request.POST.get('Balance1'):
                return render(request,'analytics_year.html',{'stu':stud,'chart':chart3,'d':'No record of credit/debit','m':'Yearly Balance bar plot'})
        if request.POST.get('Credit2'):
                return render(request,'analytics_year.html',{'stu':stud_1,'chart':chart_1,'d':'No record of credit','m':'Yearly Credit percent plot'})
        elif request.POST.get('Debit2'):
                return render(request,'analytics_year.html',{'stu':stud_2,'chart':chart_2,'d':'No record of debit','m':'Yearly Debit percent plot'})
        if request.POST.get('Balance2'):
                return render(request,'analytics_year.html',{'stu':stud,'chart':chart_3,'d':'No record of credit/debit','m':'Debit-Credit percent in Balance'})
        if request.POST.get('Trend'):
                return render(request,'analytics_year.html',{'stu':stud,'chart':chart_4,'d':'No record of credit/debit','m':'Year wise balance trend'})
        else:
                return render(request,'analytics_year.html',{'d':ds,'chart':False})

def delete_data(request, id):
    if request.user.is_authenticated:
        log_user = request.user
    else:
        return HttpResponseRedirect('accounts/login')
    if request.method == 'POST':
        
        pi = transactions.objects.get(pk = id)
        cid = v2()
        pi.delete()
        if cid == None:
            return HttpResponseRedirect('/main/cust_trans')
        else:
            return HttpResponseRedirect('/main/'+cid)

def redirect(request):
    cid = v2()
    if cid == -1:
        return HttpResponseRedirect('/main/cust_trans')
    else:
        return HttpResponseRedirect('/main/'+cid)

def analytics_1(request):
    if request.user.is_authenticated:
        log_user = request.user
    else:
        return HttpResponseRedirect('accounts/login')
    #monthly
    st = customers.objects.filter()
    stud = transactions.objects.filter()
    stud_1 = stud.filter(credit_or_debit = 'Credit')
    stud_2 = stud.filter(credit_or_debit = 'Debit')
    Z = [str(x.Customer_ID) for x in st]
    X = [str(x.CustomerID) for x in stud]
    P = [str(x.CustomerID) for x in stud_1]
    Q = [int(y.Amount) for y in stud_1]
    p1 = [str(x.CustomerID) for x in stud_2]
    q1 = [int(y.Amount) for y in stud_2]

    d ={}
    Y=[]
    for x in Z:
        #x=int(x)
        d[x]=0
    
    for x in X:
        d[x] = d[x]+1
        
    X = list(d.keys())
    
    Y = list(d.values())

    d ={}
    for x in Z:
        #x=int(x)
        d[x]=0
    i=0
    for x in P:
        d[x] = d[x]+Q[i]
        i+=1
    P = list(d.keys())
    
    Q = list(d.values())

    d1 ={}
    for x in Z:
        #x=int(x)
        d1[x]=0
    i=0
    for x in p1:
        d1[x] = d1[x]+q1[i]
        i+=1
    p1 = list(d1.keys())
    q1 = list(d1.values())

    s_p = set(P)
    s_p1 = set(p1)
    Pup = s_p.union(s_p1)
    Pup = list(Pup)
    d3 = {}
    for k in Pup:
        if (k in P) and (k in p1):
            d3[k] = d1[k]-d[k]
        elif k in P:
            d3[k] = -d[k]
        elif k in p1:
            d3[k] = d1[k]
    p2 = list(d3.keys())
    q2 = list(d3.values()) 

    chart1 = get_plot_bar1(P,Q,'Credit Amount (rupees)','CustomerID')
    chart2 = get_plot_bar1(p1,q1,'Debit Amount (rupees)','CustomerID')
    chart3 = get_plot_bar1(p2,q2,'Balance Amount (rupees)','CustomerID')
    
    chart_1 = get_plot_pie(P,Q)
    chart_2 = get_plot_pie(p1,q1)
    chart_3 = get_plot_pie(['Credit','Debit'],[sum(Q),sum(q1)])
    chart_4 = get_plot_line(p2,q2,'Balance Amount (rupees)','CustomerID')
    chart_5 = get_plot_count(X,Y,'CustomerID','Count of transactions')
    if request.POST.get('Credit1'):
        return render(request,'analytics_1.html',{'stu':stud_1,'chart':chart1,'d':'No record','m':'Customer wise Credit bar plot'})
    elif request.POST.get('Debit1'):
        return render(request,'analytics_1.html',{'stu':stud_2,'chart':chart2,'d':'No record','m':'Customer wise Debit bar plot'})
    if request.POST.get('Balance1'):
        return render(request,'analytics_1.html',{'stu':stud,'chart':chart3,'d':'No record','m':'Customer wise Balance bar plot'})
    if request.POST.get('Credit2'):
        return render(request,'analytics_1.html',{'stu':stud_1,'chart':chart_1,'d':'No record','m':'Customer wise Credit percent plot'})
    elif request.POST.get('Debit2'):
        return render(request,'analytics_1.html',{'stu':stud_2,'chart':chart_2,'d':'No record','m':'Customer wise Debit percent plot'})
    if request.POST.get('Balance2'):
        return render(request,'analytics_1.html',{'stu':stud,'chart':chart_3,'d':'No record','m':'Overall Debit-Credit percent in Balance'})
    if request.POST.get('Trend'):
        return render(request,'analytics_1.html',{'stu':stud,'chart':chart_4,'d':'No record','m':'Cutomer wise balance trend'})
    if request.POST.get('CA'):
        return render(request,'analytics_1.html',{'stu':stud,'chart':chart_5,'d':'No record','m':'Cutomer Activity'})
    else:
        return render(request,'analytics_1.html',{'d':"** select one of these six buttons **",'chart':False})

def m_analytics(request):
    if request.user.is_authenticated:
        log_user = request.user
    else:
        return HttpResponseRedirect('accounts/login')
    #monthly
    st = Merchant.objects.filter()
    stud = transactions.objects.filter()
    stud_1 = stud.filter(credit_or_debit = 'Credit')
    stud_2 = stud.filter(credit_or_debit = 'Debit')
    Z = [str(x.user) for x in st]
    X = [str(x.user) for x in stud]
    P = [str(x.user) for x in stud_1]
    Q = [int(y.Amount) for y in stud_1]
    p1 = [str(x.user) for x in stud_2]
    q1 = [int(y.Amount) for y in stud_2]

    d ={}
    Y=[]
    for x in Z:
        #x=int(x)
        d[x]=0
    
    for x in X:
        d[x] = d[x]+1
        
    X = list(d.keys())
    
    Y = list(d.values())

    d ={}
    for x in Z:
        #x=int(x)
        d[x]=0
    i=0
    for x in P:
        d[x] = d[x]+Q[i]
        i+=1
    P = list(d.keys())
    
    Q = list(d.values())

    d1 ={}
    for x in Z:
        #x=int(x)
        d1[x]=0
    i=0
    for x in p1:
        d1[x] = d1[x]+q1[i]
        i+=1
    p1 = list(d1.keys())
    q1 = list(d1.values())

    s_p = set(P)
    s_p1 = set(p1)
    Pup = s_p.union(s_p1)
    Pup = list(Pup)
    d3 = {}
    for k in Pup:
        if (k in P) and (k in p1):
            d3[k] = d1[k]-d[k]
        elif k in P:
            d3[k] = -d[k]
        elif k in p1:
            d3[k] = d1[k]
    p2 = list(d3.keys())
    q2 = list(d3.values()) 

    chart1 = get_plot_bar1(P,Q,'Credit Amount (rupees)','Merchant')
    chart2 = get_plot_bar1(p1,q1,'Debit Amount (rupees)','Merchant')
    chart3 = get_plot_bar1(p2,q2,'Balance Amount (rupees)','Merchant')
    
    chart_1 = get_plot_pie(P,Q)
    chart_2 = get_plot_pie(p1,q1)
    chart_3 = get_plot_pie(['Credit','Debit'],[sum(Q),sum(q1)])
    chart_4 = get_plot_line(p2,q2,'Balance Amount (rupees)','Merchant')
    chart_5 = get_plot_count(X,Y,'Merchant','Count of merchants')
    if request.POST.get('Credit1'):
        return render(request,'m_analytics.html',{'stu':stud_1,'chart':chart1,'d':'No record','m':'Merchant wise Credit bar plot'})
    elif request.POST.get('Debit1'):
        return render(request,'m_analytics.html',{'stu':stud_2,'chart':chart2,'d':'No record','m':'Merchant wise Debit bar plot'})
    if request.POST.get('Balance1'):
        return render(request,'m_analytics.html',{'stu':stud,'chart':chart3,'d':'No record','m':'Merchant wise Balance bar plot'})
    if request.POST.get('Credit2'):
        return render(request,'m_analytics.html',{'stu':stud_1,'chart':chart_1,'d':'No record','m':'Merchant wise Credit percent plot'})
    elif request.POST.get('Debit2'):
        return render(request,'m_analytics.html',{'stu':stud_2,'chart':chart_2,'d':'No record','m':'Merchant wise Debit percent plot'})
    if request.POST.get('Balance2'):
        return render(request,'m_analytics.html',{'stu':stud,'chart':chart_3,'d':'No record','m':'Overall Debit-Credit percent in Balance'})
    if request.POST.get('Trend'):
        return render(request,'m_analytics.html',{'stu':stud,'chart':chart_4,'d':'No record','m':'Merchant wise balance trend'})
    if request.POST.get('CA'):
        return render(request,'m_analytics.html',{'stu':stud,'chart':chart_5,'d':'No record','m':'Merchant Activity'})
    else:
        return render(request,'m_analytics.html',{'d':"** select one of these six buttons **",'chart':False})
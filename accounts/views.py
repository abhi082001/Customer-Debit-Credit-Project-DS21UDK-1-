from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from .models import Merchant
# Create your views here.

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username,password=password)
        
        if user is not None:
           # s = user.username
            auth.login(request, user)
            return redirect("/")
        
        else:
            messages.info(request, 'invalid credentials')
            return redirect('login')

    else:
        return render(request,'login.html')

def register(request):
    #username = None
    if request.method == 'POST':
        
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        business_name = request.POST.get('business_name')
        GSTIN = request.POST.get('gstin')
        username = request.POST.get('username')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        email = request.POST.get('email')

        if first_name == '':
            messages.info(request, 'please give your firstname')
            return redirect('register')
        
        if business_name == '':
            messages.info(request, 'please give your business name')
            return redirect('register')

        if GSTIN == '':
            messages.info(request, 'please give your GSTIN')
            return redirect('register')

        if username == '':
            messages.info(request, 'please give a username')
            return redirect('register')
        
        if password1=='':
            messages.info(request, 'please give a password')
            return redirect('register')
    
        
        if password1==password2:
            if User.objects.filter(username=username).exists():
                messages.info(request,'Username taken')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request,'email taken')
                return redirect('register')
            elif User.objects.filter(password=password1).exists():
                messages.info(request,'password taken')
                return redirect('register')
            else:

                user = User.objects.create_user(username =username, password =password1, email=email, first_name=first_name,last_name = last_name)
                user.save();
                reg = Merchant(Merchant_Name=first_name+' '+last_name,Business_Name=business_name,GSTIN=GSTIN,user=username)
                reg.save();
                print('user created')
                return redirect('login')
            
        
        else:
           messages.info(request,'password not matching...')
           return redirect('register')
        
        

        

    else:
        return render(request,'register.html')

def logout(request):
    auth.logout(request)
    return redirect('/')
    
def logout1(request,s):
    auth.logout(request)
    return redirect('/')

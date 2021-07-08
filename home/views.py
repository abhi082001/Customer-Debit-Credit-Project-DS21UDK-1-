from django.shortcuts import render, HttpResponseRedirect
from .models import sample
# Create your views here.

def index(request):
    return render(request, 'index.html')
def index1(request):
    reg = sample(user=request.user)
    reg.save()
    return render(request, 'merchant page.html')
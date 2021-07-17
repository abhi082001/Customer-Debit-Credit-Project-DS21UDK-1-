from django.shortcuts import render, HttpResponseRedirect

# Create your views here.

def index(request):
    return render(request, 'index.html')

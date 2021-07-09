
from django.urls import path
from . import views

urlpatterns = [
    #path('',views.base, name='base'),
    path('', views.index, name="index"),
    path('index1', views.index1, name="index1"),
    
]
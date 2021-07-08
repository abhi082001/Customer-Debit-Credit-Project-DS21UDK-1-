from django.urls import path

from . import views
import home
urlpatterns = [
    #path('<s>',home.views.index, name='home'),
    path('register',views.register, name='register'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout')
]
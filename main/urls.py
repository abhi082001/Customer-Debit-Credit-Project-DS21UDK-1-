from django.urls import path

from . import views
import accounts
urlpatterns = [
    path('user_input',views.user_input, name='user_input'),
    path('cust_table',views.cust_table, name='cust_table'),
    path('cust_trans',views.cust_trans, name='cust_trans'),
    path('accounts/logout',accounts.views.logout, name='logout'),
    path('accounts/login',accounts.views.login, name='login'),
    path('accounts/register',accounts.views.register, name='register')
]
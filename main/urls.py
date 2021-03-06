from django.urls import path

from . import views
import accounts
urlpatterns = [
    path('user_input',views.user_input, name='user_input'),
    path('cust_table',views.cust_table, name='cust_table'),
    path('mycust_table',views.mycust_table, name='mycust_table'),
    path('trans_table',views.trans_table, name='trans_table'),
    path('trans_table1',views.trans_table1, name='trans_table1'),
    path('cust_trans',views.cust_trans, name='cust_trans'),
    path('merch_page',views.merch_page, name='merch_page'),
    path('analytics',views.analytics, name='analytics'),
    path('analytics_m',views.analytics_m, name='analytics_m'),
    path('m_analytics',views.m_analytics, name='m_analytics'),
    path('analytics_y',views.analytics_y, name='analytics_y'),
    path('analytics_1',views.analytics_1, name='analytics_1'),
    path('analytics',views.analytics, name='analytics'),
    path('redirect',views.redirect, name='redirect'),
    path('delete/<int:id>/',views.delete_data, name='deletedata'),
    path('<int:id>/',views.updatedata, name='updatedata'),
    path('<int:id>/1',views.updatedata1, name='updatedata1'),
    path('<int:id>/0',views.updatedata_1, name='updatedata_1'),
    path('<int:id>/2',views.updatedata2, name='updatedata2'),
    path('<int:id>/3',views.updatedata3, name='updatedata3'),
    path('<str:sval>/',views.cust_trans1, name='cust_trans1'),
    path('accounts/logout',accounts.views.logout, name='logout'),
    path('accounts/login',accounts.views.login, name='login'),
    path('accounts/register',accounts.views.register, name='register')
]

from django.urls import path
from . import views


urlpatterns = [
 path('', views.dashboard, name='dashboard'),
 path('clients/', views.clients, name='clients'),

 
 path('userlist/', views.userlist, name='userlist'),
 path('userdetails/<str:pk>', views.userDetails, name='userDetails'),
path('userdetails/editclient/<int:pk>', views.editClient, name='editclient'),
path('userdetails/getclient/<int:pk>', views.getClient, name='getclient'),
 
 path('invoices/', views.invoicelist, name='invoices'),
path('invoices//<str:pk>', views.invoiceDetails, name='invoiceDetails'),
 path('subscription/', views.subscription, name='subscription'),
 path('subscription/editsubscription/<int:pk>', views.editSubscriptionPlan, name='editSubscriptionPlan'),
 path('subscription/getsubscription/<int:pk>/',views.getSubscriptionPlan,name="getSubscriptionPlan"),
 path('subscription/<int:pk>',views.subscriptiondetails,name="subscriptiondetails"),
 
 path('subscribers/', views.subscribers, name='subscribers'),
 path('subscribers/<str:pk>', views.subscribersDetails, name='subscribersDetails'),
 path('login/', views.loginuser, name='login'),
path('register/', views.register, name='register'),
path('logout/', views.logoutUSer, name='logout'),
path('account/', views.account, name='account'),
path('unauthorized/',views.unauthorized,name='unauthorized')
]
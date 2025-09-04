
from django.urls import path
from . import views


urlpatterns = [
    
#path('login/', views.loginuser, name='login'),
path('', views.cusDashboard, name='customer_dashboard'),
path('list/', views.cusList, name='customer_list'),
path('list/getlist/<int:pk>/',views.getcustomerdetails,name="getCustomerData"),
path('list/updatelist/<int:pk>',views.updatecustomerdetails,name="updateCustomerData"),
 
path('details/<int:pk>', views.cusDetails, name='customer_Details'),
path('services/', views.serviceList, name='serviceList'),
path('invoicelist/', views.invoiceList, name='invoiceList'),


path('account/',views.useraccount,name="useraccount"),
path('myplan/',views.myplan,name="myplan"),



]
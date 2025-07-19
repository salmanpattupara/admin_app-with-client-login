
from django.shortcuts import render
from admin_app.models import SubscriptionPlan,Subscriber
from .models import Customer, Service, Serviceinvoice
from django.contrib.auth.decorators import login_required,user_passes_test
from admin_app.permission import subscription_required

# Create your views here.


@login_required
def cusDashboard(request):
    return render(request,"index.html")

@subscription_required
@login_required
def cusList(request):
    client=request.user.client
    customer=Customer.objects.select_related('client').filter(client=client)
    active_count=Customer.objects.filter(client=client).count
    inactive_count=0
    context={
        "customers":customer,
        "active_count":active_count,
        "inactive_count":inactive_count,
       
    }
    return render(request,"client-list.html",context)

def cusDetails(request,pk):
    services=Service.objects.filter(customer=pk)
    services_acive_count=services.filter(status="active").count
    customer=Customer.objects.get(id=pk)
   
    context={
        "services":services,
        "customer":customer,
        "services_acive_count":services_acive_count
      
    }
    return render(request,"user-details.html",context)
    
def serviceList(request):
    services=Service.objects.filter(customer__client=request.user.client)
    services_acive_count=services.filter(status="active").count
    customer=Customer.objects.all()
   
    context={
        "services":services,
        "customer":customer,
        "services_acive_count":services_acive_count
      
    }
    return render(request,"services-list.html",context)

def invoiceList(request):
    invoices=Serviceinvoice.objects.filter(service__customer__client=request.user.client)
    
    context={
        "invoices":invoices,
       
       
    }
    return render(request,"invoice-list.html",context)


def useraccount(request):
    
    return render(request, 'accountpage.html', )


def myplan(request):
    client=request.user.client
    print(client)
    subscriptionPlan = SubscriptionPlan.objects.filter(subscriptionAmount__gt=0,is_active=True)
    myplans=Subscriber.objects.filter(client=request.user.client)
    
    active_count = SubscriptionPlan.objects.filter(is_active=True).count()
    inactive_count = SubscriptionPlan.objects.filter(is_active=False).count()
    context={
        "subscriptionPlan":subscriptionPlan,
        "active_count":active_count,
        "inactive_count":inactive_count,
        "myplans":myplans
        
    }
    return render(request,"subscription-list.html",context)
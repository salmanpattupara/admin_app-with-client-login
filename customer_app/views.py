
from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse, JsonResponse
from admin_app.models import SubscriptionPlan,Subscriber
from customer_app.form import Customerform
from .models import Customer, Service, Serviceinvoice
from django.contrib.auth.decorators import login_required,user_passes_test
from admin_app.permission import subscription_required

# Create your views here.



def cusDashboard(request):  
    return render(request,"index.html")

@subscription_required

def cusList(request):
    client=request.user.client
    if request.method=="POST":
        form=Customerform(request.POST)
        if form.is_valid():
           
            new_customer=form.save(commit=False)
            new_customer.client=client
            new_customer.save()    
            return redirect(request.path)
    form=Customerform(request.POST)
    
    customer=Customer.objects.select_related('client').filter(client=client).order_by("-created_at")
    active_count=Customer.objects.filter(client=client).count
    inactive_count=0
    context={
        "customers":customer,
        "active_count":active_count,
        "inactive_count":inactive_count,
        "form":form
       
    }
    return render(request,"client-list.html",context)

def getcustomerdetails(request,pk):
    customer = get_object_or_404(Customer,pk=pk)
    
    return JsonResponse({"id":customer.id,
                         #"client":customer.client,
                         "name":customer.name,
                         "address":customer.address,
                         "contactNumber":customer.contactNumber,
                         "emailId":customer.emailId})
    
def updatecustomerdetails(request,pk):
    customer = get_object_or_404(Customer,pk=pk)
   
  
    if request.method == 'POST':
        form = Customerform(request.POST,instance=customer)
       
       
        if form.is_valid():
            new_customer=form.save(commit=False)
            new_customer.name=form.cleaned_data.get('name')
            new_customer.contactNumber=form.cleaned_data.get('contactNumber')
            new_customer.emailId=form.cleaned_data.get('emailId')
            new_customer.address=form.cleaned_data.get('address')
            
            #new_customer.client=client
            new_customer.save()    
            return JsonResponse({'success': True})
       
        return JsonResponse({'success': False, 'errors': form.errors})
        
    
    else:
        form = Customerform(instance=customer)
        return render(request, 'subscription-list.html', {'form': form})

@subscription_required
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
   
@subscription_required 
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


@subscription_required
def invoiceList(request):
    invoices=Serviceinvoice.objects.filter(service__customer__client=request.user.client)
    
    context={
        "invoices":invoices,
       
       
    }
    return render(request,"invoice-list.html",context)


def useraccount(request):
    
    return render(request, 'accountpage.html', )

@subscription_required
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
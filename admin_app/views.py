from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import get_user_model
from django.db.models import Sum
# Create your views here.
from django.shortcuts import get_object_or_404, render,redirect
from django.http import HttpResponse, JsonResponse
import datetime
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.decorators import login_required,user_passes_test

from .permission import staff_required, subscription_required
from .form import Clientform, CustomUserCreationForm, Subscriberform, SubscriptionplanForm
from .models import Client, ClientBilling, Invoice, Subscriber,SubscriptionPlan, UserDetails
from django.contrib.auth.forms import UserCreationForm




@user_passes_test(lambda u: u.is_staff)
@login_required
def dashboard(request):
    client_count=Client.objects.all().count
    user_count = User.objects.all().count
    billing_count = ClientBilling.objects.all().count() 
    #total = ClientBilling.objects.aggregate(total_amount=Sum("totalAmount"))["total_amount"]
    total=0
    context={
        "client_count":client_count,
        "user_count":user_count,
        "billing_count":billing_count,
        "total":total
    }
    return render(request,"index.html",context)


@user_passes_test(lambda u: u.is_staff)
@login_required
def clients(request):
    
    if request.method=="POST":
        form=Clientform(request.POST)
        if form.is_valid():
            form.save()
            return redirect(request.path)
        
    form=Clientform(request.POST)
    client=Client.objects.all()
    active_count = Client.objects.filter(is_active=True).count()
    inactive_count = Client.objects.filter(is_active=False).count()
    context={
        "clients":client,
        "active_count":active_count,
        "inactive_count":inactive_count,
        "form":form
    }
    return render(request,"client-list.html",context)

@user_passes_test(lambda u: u.is_staff)
@login_required
def editClient(request,pk):
    clientdetails = get_object_or_404(Client,pk=pk)
    clientname=clientdetails.clientName
    print(clientname)
    clientaliasname=clientdetails.clientAliasName
    
    if request.method == 'POST':
        form = Clientform(request.POST, instance=clientdetails)
        
        if form.is_valid():
            client=form.save(commit=False)
            client.clientName=clientname
            client.subscriptionName=clientaliasname
            client.clientContactNumber=form.cleaned_data.get('clientContactNumber')
            client.clientEmailId=form.cleaned_data.get('clientEmailId')
            client.clientPlace=form.cleaned_data.get('clientPlace')
            client.clientAddress=form.cleaned_data.get("clientAddress")
            client.is_active=form.cleaned_data.get("is_active")
            client.save()
            return JsonResponse({'success': True})
        return JsonResponse({'success': False, 'errors': form.errors})
    else:
        form = Clientform(instance=clientdetails)
        return render(request, 'client-list.html', {'form': form,  "clientdetails":clientdetails,})
@user_passes_test(lambda u: u.is_staff)
@login_required
def getClient(request,pk):
    
    client = get_object_or_404(Client,pk=pk)

    return JsonResponse({"id":client.id,"clientName":client.clientName,
                         "clientAliasName":client.clientAliasName,
                         "clientContactNumber":client.clientContactNumber,
                         "clientEmailId":client.clientEmailId,
                         "clientPlace":client.clientPlace,
                         "clientAddress":client.clientAddress,
                         "is_active":client.is_active})
    
    
@user_passes_test(lambda u: u.is_staff)
@login_required

def invoicelist(request):
    invoices=ClientBilling.objects.all().order_by("created_at")
    active_count = ClientBilling.objects.filter(status=True).count()
    inactive_count = ClientBilling.objects.filter(status=False).count()   
    #total = ClientBilling.objects.aggregate(total_amount=Sum("totalAmount"))["total_amount"] or 0
    total=0
    activePlan_count=ClientBilling.objects.filter(subscription__status="active").count()
    pendingPlan_count=ClientBilling.objects.filter(subscription__status="pending").count()
    context={
        "invoices":invoices,
        "active_count":active_count,
        "inactive_count":inactive_count,
        "total":total,
        "activePlan_count":activePlan_count,
        "pendingPlan_count":pendingPlan_count
        
    }
    return render(request,"invoice-list.html",context)

@user_passes_test(lambda u: u.is_staff)
@login_required
def  invoiceDetails(request,pk):
    client =Client.objects.get(id=pk)
    
    invoices=ClientBilling.objects.filter(client=pk)
    
    context={
        "invoices":invoices,
        "client":client
 
    }
    return render(request,"invoice-details.html",context)


User = get_user_model()
@user_passes_test(lambda u: u.is_staff)
def userlist(request):
    users = User.objects.all()
    active_count = User.objects.filter(is_active=True).count()
    inactive_count = User.objects.filter(is_active=False).count()
    print(users.count())
    context={
        "users":users,
        "active_count":active_count,
        "inactive_count":inactive_count
        
    }
    return render(request,"users-list.html",context)

@user_passes_test(lambda u: u.is_staff)
def userDetails(request,pk):
    
    client =Client.objects.get(id=pk)
    users = User.objects.filter(client=pk)
    userscount = User.objects.filter(client=pk).count()
    active_count=User.objects.filter(client=pk,is_active=True).count()
    inactive_count=User.objects.filter(client=pk,is_active=False).count()
    context={
        "users":users,
       "client":client,
       "userscount":userscount,
       "active_count":active_count,
       "inactive_count":inactive_count
    }
    return render(request,"user-details.html",context)

@user_passes_test(lambda u: u.is_staff)
def subscription(request):
    if request.method=="POST":
        form=SubscriptionplanForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(request.path)
        
    form=SubscriptionplanForm(request.POST)
    subscriptionPlan=SubscriptionPlan.objects.all()
    active_count = SubscriptionPlan.objects.filter(is_active=True).count()
    inactive_count = SubscriptionPlan.objects.filter(is_active=False).count()
    context={
        "subscriptionPlan":subscriptionPlan,
        "active_count":active_count,
        "inactive_count":inactive_count,
        "form":form
    }
    return render(request,"subscription-list.html",context)
@user_passes_test(lambda u: u.is_staff)
def getSubscriptionPlan(request,pk):
   
    subscriptionPlan = get_object_or_404(SubscriptionPlan,pk=pk)
    
    return JsonResponse({"id":subscriptionPlan.id,"subscriptionName":subscriptionPlan.subscriptionName,
                         "subscriptionValidity":subscriptionPlan.subscriptionValidity,
                         "subscriptionAmount":subscriptionPlan.subscriptionAmount,
                         "is_active":subscriptionPlan.is_active})

@user_passes_test(lambda u: u.is_staff)
def editSubscriptionPlan(request,pk):
    subscriptionPlan = get_object_or_404(SubscriptionPlan,pk=pk)
    validity=subscriptionPlan.subscriptionValidity
    amount=subscriptionPlan.subscriptionAmount
    if request.method == 'POST':
        form = SubscriptionplanForm(request.POST, instance=subscriptionPlan)
        
        if form.is_valid():
            plan=form.save(commit=False)
            plan.subscriptionName=form.cleaned_data.get('subscriptionName')
            plan.subscriptionValidity=validity
            plan.subscriptionAmount=amount
            plan.is_active=form.cleaned_data.get("is_active")
            plan.save()
            return JsonResponse({'success': True})
        return JsonResponse({'success': False, 'errors': form.errors})
    else:
        form = SubscriptionplanForm(instance=subscriptionPlan)
        return render(request, 'subscription-list.html', {'form': form,  "subscriptionPlan":subscriptionPlan,})
   
   
@user_passes_test(lambda u: u.is_staff) 
def subscriptiondetails(request,pk):
    
    subscriberList=Subscriber.objects.filter(subscribedPlan=pk).order_by('-updated_at')
    plan=SubscriptionPlan.objects.get(id=pk)
    
    context={
        "subscriberList":subscriberList,
        "plan":plan
       
    }
    return render(request,"subscription-Details.html",context)

@user_passes_test(lambda u: u.is_staff)
def subscribers(request):
    if request.method=="POST":
        form=Subscriberform(request.POST)
        if form.is_valid():
            list=form.save(commit=False)
            list.client=form.cleaned_data.get("client")
           
            if Subscriber.objects.filter(client=list.client.id,is_active=True):
                if not Subscriber.objects.filter(client=list.client.id,status="pending"):
                    #chceking aleady active plan is ther or not,if it there thennew plan will add as pending
                    clients=Subscriber.objects.filter(client=list.client).latest('created_at')
                    subscribedPlan=form.cleaned_data.get("subscribedPlan")
                    list.subscriptionStart=clients.subscriptionEnd+datetime.timedelta(days=1)
                    list.subscriptionEnd=list.subscriptionStart+datetime.timedelta(days=int(subscribedPlan.subscriptionValidity))
                    list.status="pending"
                    list.is_active="False"
                    list.save()
                    invoice=ClientBilling(client= list.client,subscription=list,totalAmount=list.subscribedPlan.subscriptionAmount)
                    invoice.save()
                    return redirect(request.path)
                else:
                    
                    messages.error(request, "There is a pending plan already")
            else:
                subscribedPlan=form.cleaned_data.get("subscribedPlan")
                list.subscriptionStart=datetime.date.today()
                list.subscriptionEnd=list.subscriptionStart+datetime.timedelta(days=int(subscribedPlan.subscriptionValidity))
                list.status="active"
                list.save()
                invoice=ClientBilling(client= list.client,subscription=list,totalAmount=list.subscribedPlan.subscriptionAmount)
                invoice.save()
                return redirect(request.path)
    form=Subscriberform(request.POST)
    clients =Client.objects.filter(is_active=True)
    subscribers=Subscriber.objects.all().order_by("status")

    active_count = Subscriber.objects.filter(status="active").count()
    expired_count = Subscriber.objects.filter(status="expired").count()
    pending_count = Subscriber.objects.filter(status="pending").count()
    subscriptionPlans=SubscriptionPlan.objects.filter(is_active=True)

    context={
        "subscribers":subscribers,
        "active_count":active_count,
        "expired_count":expired_count,
        "pending_count":pending_count,
        "clients":clients,
        "subscriptionPlans":subscriptionPlans,
        "form":form
    }
    return render(request,"subscribers-list.html",context)

@user_passes_test(lambda u: u.is_staff)
def subscribersDetails(request,pk):
    
    client =Client.objects.get(id=pk)
    subscribers=Subscriber.objects.filter(client=pk).order_by('-created_at')
    
    for subscriber in subscribers:
        if subscriber.is_active:
            if subscriber.isExpired():
                subscriber.is_active=False
                subscriber.status="expired"
                subscriber.save()
        if subscriber.status=="pending":
            if subscriber.isActive():
                subscriber.is_active=True
                subscriber.status="active"
                subscriber.save()
            else:
                subscriber.is_active=False
                subscriber.status="pending"
                subscriber.save()
                
    context={
        "subscribers":subscribers,
       "client":client
       
    }
    return render(request,"subscriber-Details.html",context)



def loginuser(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            
            login(request, user)
            if user.is_superuser or user.is_staff:
                return redirect('dashboard') 
            else:
                return redirect('customer_dashboard')
                # Change to your landing page
        else:
            messages.error(request, 'Invalid username or password.')
    print("requests denied")
    return render(request, 'page-login.html')


@user_passes_test(lambda u: u.is_staff)
def register(request):
    clients =Client.objects.filter(is_active=True)

    if request.method == "POST":
          
            form = CustomUserCreationForm(request.POST)
            if form.is_valid():
                user = form.save()
                messages.success(request, "user registered successful.")
                return redirect(request.path)
    else:
        print("error")
        form = CustomUserCreationForm()
    
    context={
        "clients":clients,
        "form":form
    }
    return render(request,"page-register.html",context)


def logoutUSer(request):
    logout(request)
    return redirect('login') 




@user_passes_test(lambda u: u.is_staff)
def account(request):
    
    return render(request, 'accountpage.html', )


def unauthorized(request):
    
    return render(request, 'unauthorized-user.html', )
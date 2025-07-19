from django.db import models
from django.contrib.auth.models import AbstractUser
from datetime import timedelta, date


# Create your models here.

class Client(models.Model):
    clientName=models.CharField(max_length=50)
    clientAliasName=models.CharField(max_length=50)
    clientContactNumber=models.CharField(max_length=10)
    clientEmailId=models.EmailField()
    clientPlace=models.CharField(max_length=50)
    clientAddress=models.CharField(max_length=200)
    is_active=models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.clientName
    
    
class SubscriptionPlan(models.Model):
    subscriptionName=models.CharField(max_length=50,default="Monthly",unique=True)
    subscriptionAmount=models.CharField(max_length=20,default="5000")
    subscriptionValidity=models.CharField(max_length=30,default="M")
    is_active=models.BooleanField(default=True)
    
    def __str__(self):
        return self.subscriptionName
    
    def calculateValidaity(self):
        return self.subscriptionValidity
    
    
    
    
    
            
class Subscriber(models.Model):
    plan_status={
        "active":"active",
        "pending":"pending",
        "expired":"expired"
    }
    client=models.ForeignKey(Client,on_delete=models.CASCADE)
    subscribedPlan=models.ForeignKey(SubscriptionPlan,on_delete=models.DO_NOTHING,related_name='subscribedplan')
    subscriptionStart = models.DateField()
    subscriptionEnd = models.DateField()
    is_active=models.BooleanField(default=True)
    status=models.CharField(choices=plan_status,default="active",max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.client.clientName
    def isExpired(self):
        return self.subscriptionEnd < date.today()
    
    def isActive(self,*args):
       
        return self.subscriptionStart <= date.today() <= self.subscriptionEnd
    
     
    
            
    
class ClientBilling(models.Model):
    client=models.ForeignKey(Client,on_delete=models.CASCADE)
    subscription=models.ForeignKey(Subscriber,on_delete=models.DO_NOTHING,unique=True)
    discountAmount=models.CharField(max_length=20,default=0)
    totalAmount=models.CharField(max_length=20,default=0)
    status=models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    

    def __str__(self):
         return self.client.clientName
    def getTotal(self):
        return int(self.totalAmount)-int(self.discountAmount)
   
class Invoice(models.Model):  
    client=models.ForeignKey(Client,on_delete=models.CASCADE)
    subscription=models.ForeignKey(SubscriptionPlan,on_delete=models.DO_NOTHING) 
    
    
    def __str__(self):
        return self.client.clientName
   
   
   
class UserDetails(AbstractUser):
    client=models.ForeignKey(Client,on_delete=models.CASCADE,blank=True,null=True)
    
    
    

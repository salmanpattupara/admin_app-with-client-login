from django.db import models
from django.core.exceptions import ValidationError
from admin_app.models import Client


#validator for phone numer
def validate_phone(value):
    if not value.isdigit() or len(value) != 10:
        raise ValidationError("phonenumber should be 10 digiti")


# Create your models here.

class Customer(models.Model):
    client=models.ForeignKey(Client,on_delete=models.CASCADE)
    name=models.CharField(max_length=50)
    address=models.CharField(max_length=50)
    contactNumber=models.CharField(max_length=10,validators=[validate_phone],unique=True)
    emailId=models.EmailField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name
    
    
class Service(models.Model):
    service_status={
        "active":"active",
        "closed":"closed",
       
    }
    customer=models.ForeignKey(Customer,on_delete=models.CASCADE)
    name=models.CharField(max_length=100)
    description=models.CharField(max_length=250)
    date=models.DateField()
    status=models.CharField(choices=service_status,default="active",max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name
    
    
class Serviceinvoice(models.Model):
    service=models.ForeignKey(Service,on_delete=models.CASCADE)
    description=models.CharField(max_length=250)
    discount=models.PositiveIntegerField(blank=True,default=0)
    tax=models.PositiveBigIntegerField(blank=True,default=0)
    total=models.PositiveIntegerField(default=0)
    paid=models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.service.name
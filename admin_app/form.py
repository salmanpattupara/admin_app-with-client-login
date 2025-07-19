from django import forms
from .models import SubscriptionPlan,Subscriber,Client

from django.contrib.auth.forms import UserCreationForm
from .models import UserDetails

class SubscriptionplanForm(forms.ModelForm):
    
    class Meta:
        model=SubscriptionPlan
        
        fields=["id","subscriptionName","subscriptionAmount","subscriptionValidity","is_active"]
        widgets = {
            'subscriptionName': forms.TextInput(attrs={'class': 'form-control'}),
            'subscriptionAmount': forms.TextInput(attrs={'class': 'form-control'}),
            'subscriptionValidity': forms.TextInput(attrs={'class': 'form-control'}),
           
            # Add more fields and their classes as needed
        }
        
        
        
        
class Subscriberform(forms.ModelForm):
    
    class Meta:
        model=Subscriber
        
        fields=["id","client","subscribedPlan"]
        widgets = {
            'client': forms.Select(attrs={'class': 'form-control'}),
            'subscribedPlan': forms.Select(attrs={'class': 'form-control'}),
            # Add more fields and their classes as needed
        }
        
        
class Clientform(forms.ModelForm):
    
    class Meta:
        model=Client
        
        fields="__all__"
        widgets = {
            'client': forms.Select(attrs={'class': 'form-control'}),
            'subscribedPlan': forms.Select(attrs={'class': 'form-control'}),
            # Add more fields and their classes as needed
        }
        
    
class CustomUserCreationForm(UserCreationForm):
    client = forms.ModelChoiceField(
        queryset=Client.objects.filter(is_active=True),
        required=True,
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    
    class Meta:
        model = UserDetails
        fields = ['username', 'first_name','last_name','email','client' ,'password1', 'password2']
        
    widgets = {
        'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter username', 'required': 'true'}),
        'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First name', 'required': 'true'}),
        'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last name', 'required': 'true'}),
        'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Enter email', 'required': 'true'}),
        'password1': forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Enter password', 'required': 'true'}),
        'password2': forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Confirm password', 'required': 'true'}),
        # Add more fields and their classes as needed
    }
        
from django.http import HttpResponseForbidden
from django.contrib.auth.decorators import user_passes_test

from .models import Subscriber
import datetime
from django.shortcuts import redirect



#helper function for permission decorator 
def has_active_subscription(client):
    
    if client:
        subscribers=Subscriber.objects.filter(client=client,is_active=True).order_by('-created_at')
        for subscriber in subscribers:
            if subscriber.subscriptionStart <=datetime.date.today() <= subscriber.subscriptionEnd:
                return True
            else:
                False
        
   
    

def subscription_required(view_func):
    def _wrapped_view(request, *args, **kwargs):
        if request.user.is_authenticated:
            if not has_active_subscription(request.user.client):
                return HttpResponseForbidden("You need an active subscription.")
            return view_func(request, *args, **kwargs)
        else:
            return redirect("login")
    return _wrapped_view


def staff_required(view_func):
    decorated_view_func = user_passes_test(
        lambda user: user.is_staff,
        login_url='unauthorized'  # or custom forbidden page
    )(view_func)
    return decorated_view_func

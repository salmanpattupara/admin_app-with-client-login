from django.contrib import admin
from .models import Subscriber, UserDetails


from admin_app.models import Client,ClientBilling,SubscriptionPlan,Invoice

# Register your models here.
admin.site.register(SubscriptionPlan)
admin.site.register(Client)
admin.site.register(ClientBilling)
admin.site.register(UserDetails)
admin.site.register(Subscriber)
admin.site.register(Invoice)

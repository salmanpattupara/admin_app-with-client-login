from django.urls import path
from admin_app.api.views import ClientList,SubscriberList,ClientDetails,SubscriptionList


urlpatterns = [
    
     path('client/', ClientList.as_view() ,name="clientlist"),
     path('client/<int:pk>/', ClientDetails.as_view() ,name="clientdetails"),
     path('subscriberlist/',SubscriberList.as_view(),name='subscriberlist'),
     #path('subscriberlist/<int:pk>',SubscriberDetails.as_view(),name='subscriberlist'),
     
     path('subscriptionplan/',SubscriptionList.as_view(),name='subscriptionlist')
    
    
]
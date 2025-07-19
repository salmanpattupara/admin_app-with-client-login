
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics

from admin_app.models import Client ,Subscriber,SubscriptionPlan
from .serializers import Clientserializer,SubscriberSerializer,SubsriptionPlanserializer




class ClientList(generics.ListCreateAPIView):
   queryset = Client.objects.all()
   serializer_class = Clientserializer
   
class ClientDetails(generics.RetrieveAPIView):
   queryset = Client.objects.all()
   serializer_class = Clientserializer

   
   
class SubscriberList(generics.ListAPIView):
   queryset=Subscriber.objects.all()
   serializer_class=SubscriberSerializer
   
class SubscriptionList(generics.ListAPIView):
   queryset=SubscriptionPlan.objects.all()
   serializer_class=SubsriptionPlanserializer
   
   
   
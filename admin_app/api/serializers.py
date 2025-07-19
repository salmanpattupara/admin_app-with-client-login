from rest_framework import serializers

from admin_app.models import Client,Subscriber,SubscriptionPlan




        
        
class SubscriberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscriber
        fields = "__all__"

class Clientserializer(serializers.ModelSerializer):
    subscriber = SubscriberSerializer(many=True, read_only=True)
    class Meta:
        model = Client
        fields = "__all__"

class SubsriptionPlanserializer(serializers.ModelSerializer):
    subscribedplan=SubscriberSerializer(many=True, read_only=True)
    class Meta:
        model = SubscriptionPlan
        fields = "__all__"
from rest_framework import serializers
from main.models import Profile


class ProfileUserSeialazer(serializers.ModelSerializer):
    publication_count = serializers.SerializerMethodField()
    subscriber_count = serializers.SerializerMethodField()
    subscription_count = serializers.SerializerMethodField()
    
    class Meta:
        model = Profile
        fields = [
            'user',
            'publication_count',
            'subscriber_count',
            'subscription_count',
        ]

    def get_publication_count(self, obj):
        return obj.user.publication.filter(deleted=False).count()
        
    def get_subscriber_count(self, obj):
        return obj.user.subscriber.all().count()

    def get_subscription_count(self, obj):
        return obj.subscription.all().count()

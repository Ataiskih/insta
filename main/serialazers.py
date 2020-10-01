from django.contrib.auth import get_user_model
from rest_framework import serializers
from main.models import Profile
User = get_user_model()


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


class UserSeialazer(serializers.ModelSerializer):
    publication_count = serializers.SerializerMethodField()
    subscriber_count = serializers.SerializerMethodField()
    subscription_count = serializers.SerializerMethodField()
    photo = serializers.SerializerMethodField()
    description = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = [
            'username',
            'first_name',
            'last_name',
            'email',
            'publication_count',
            'subscriber_count',
            'subscription_count',
            'photo',
            'description',
        ]

    def get_subscription_count(self, obj):
        return obj.profile.subscription.all().count()

    def get_subscriber_count(self, obj):
        return obj.subscriber.all().count()

    def get_publication_count(self, obj):
        return obj.publication.filter(deleted=False).count()

    def get_description(self, obj):
        return obj.profile.description

    def get_photo(self, obj):
        return obj.profile.photo.url


class UserListSerialazer(serializers.ModelSerializer):
    photo = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = [
            'username',
            'first_name',
            'last_name',
            'photo',
        ]

    def get_photo(self, obj):
        return obj.profile.photo.ur

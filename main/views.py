from django.shortcuts import render
from django.contrib.auth import get_user_model
from rest_framework.generics import (
    RetrieveAPIView, 
    ListAPIView
)
from main.serialazers import (
    ProfileUserSeialazer,
    UserSeialazer,
    UserListSerialazer
)
from main.models import Profile
User = get_user_model()


class ProfileRetriveView(RetrieveAPIView):
    serializer_class = ProfileUserSeialazer
    queryset = Profile.objects.all()


class UserRetriveView(RetrieveAPIView):
    serializer_class = UserSeialazer
    lookup_field = 'username'
    queryset = User.objects.filter(
        is_active=True
    )


class FollowingListView(ListAPIView):
    serializer_class = UserListSerialazer
    
    def get_queryset(self):
        username = self.kwargs['username']
        user = User.objects.get(username=username)
        list_following = user.profile.subscription.all()
        return list_following


class FollowersListView(ListAPIView):
    serializer_class = UserListSerialazer

    def get_queryset(self):
        username = self.kwargs.get('username')
        user = User.objects.get(username=username)
        list_followers = User.objects.filter(
            profile__subscription__in=[user]
        )
        return list_followers

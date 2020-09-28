from django.shortcuts import render
from rest_framework.generics import RetrieveAPIView
from main.serialazers import ProfileUserSeialazer
from main.models import Profile


class ProfileRetriveView(RetrieveAPIView):
    serializer_class = ProfileUserSeialazer
    queryset = Profile.objects.all()

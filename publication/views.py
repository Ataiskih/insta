from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from publication.serialazers import PublicationSerialazer
from publication.models import Publication


class PublicationViewSet(ModelViewSet):
    serializer_class = PublicationSerialazer
    queryset = Publication.objects.all()

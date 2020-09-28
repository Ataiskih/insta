from rest_framework.serializers import ModelSerializer
from publication.models import Publication


class PublicationSerialazer(ModelSerializer):
    class Meta:
        model = Publication
        fields = [
            'id',
            'author',
            'image',
            'description',
            'created',
        ]
        
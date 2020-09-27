from django.contrib import admin
from publication.models import Publication


@admin.register(Publication)
class PublicationAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'image',
        'author',
        'description',
        'created',
        'updated',
        'deleted',
    ]
    fields = [
        'image',
        'author',
        'description',
    ]
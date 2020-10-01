from django.contrib import admin
from main.models import Profile


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = [
        'pk',
        'user',
        'created',
        'updated',
        'deleted',
    ]
    fields = [
        'user',
        'subscription',
    ]
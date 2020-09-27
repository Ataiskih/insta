# Generated by Django 3.1.1 on 2020-09-27 11:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Publication',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255, null=True, verbose_name='Name')),
                ('created', models.DateField(auto_now_add=True, verbose_name='Created date')),
                ('updated', models.DateField(auto_now=True, verbose_name='Updated date')),
                ('deleted', models.BooleanField(default=False, verbose_name='Deleted')),
                ('image', models.ImageField(upload_to='publication_image')),
                ('description', models.TextField(blank=True, max_length=2000, null=True, verbose_name='Description')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='publication', to=settings.AUTH_USER_MODEL, verbose_name='Author')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]

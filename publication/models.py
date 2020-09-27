from django.db import models
from main.models import BaseAbstractModel
from django.contrib.auth import get_user_model
User = get_user_model()


class Publication(BaseAbstractModel):
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="publication",
        verbose_name="Author"
    )
    image = models.ImageField(
        upload_to="publication_image"
    )
    description = models.TextField(
        null=True,
        blank=True,
        max_length=2000,
        verbose_name="Description"
    )

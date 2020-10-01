from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()


# this model like a default fields for another models
class BaseAbstractModel(models.Model):
    name = models.CharField(
        max_length=255,
        blank=True, null=True,
        verbose_name='Name'
    )
    created = models.DateField(
        auto_now_add=True,
        verbose_name='Created date'
    )
    updated = models.DateField(
        auto_now=True,
        verbose_name='Updated date'
    )
    deleted = models.BooleanField(
        default=False,
        verbose_name='Deleted'
    )

    def __str__(self):
        if self.name:
            return self.name
        return f"{self.pk}"

    class Meta:
        abstract = True


class Profile(BaseAbstractModel):
    user = models.OneToOneField(
        User,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name='profile',
        verbose_name='User'
    )
    subscription = models.ManyToManyField(
        User,
        blank=True,
        related_name='subscriber',
        verbose_name='Subscrioption'
    )
    description = models.CharField(
        max_length=5000,
        null=True,
        blank=True,
        verbose_name='About me'
    )
    photo = models.ImageField(
        upload_to='profiles',
        default='/icon/default_icon.jpg/'
    )

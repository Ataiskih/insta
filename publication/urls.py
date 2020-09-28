from django.urls import path
from rest_framework import routers
from publication.views import PublicationViewSet


router = routers.DefaultRouter()
router.register(
    r'publication',
    PublicationViewSet
)
urlpatterns = router.urls

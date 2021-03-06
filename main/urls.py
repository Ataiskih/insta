from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from main.views import (
    ProfileRetriveView,
    UserRetriveView,
    FollowingListView,
    FollowersListView
)


urlpatterns = [
    path('<int:pk>/', ProfileRetriveView.as_view()),
    path('<username>/', UserRetriveView.as_view()),
    path('<username>/following/', FollowingListView.as_view()),
    path('<username>/followers/', FollowersListView.as_view()),
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, docoment_root=settings.MEDIA_ROOT)

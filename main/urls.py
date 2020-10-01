from django.urls import path
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

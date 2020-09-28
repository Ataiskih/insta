from django.urls import path
from main.views import ProfileRetriveView


urlpatterns = [
    path('<int:pk>/', ProfileRetriveView.as_view()),
]
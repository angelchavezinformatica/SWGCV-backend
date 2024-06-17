from django.urls import path

from .views import ClientView, ProfileView

urlpatterns = [
    path(route='all', view=ClientView.as_view()),
    path(route='profile', view=ProfileView.as_view()),
]

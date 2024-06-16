from django.urls import path

from .views import ClientView

urlpatterns = [
    path(route='all', view=ClientView.as_view()),
]

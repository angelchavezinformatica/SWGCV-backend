from django.urls import path

from .views import ProviderView

urlpatterns = [
    path(route='all', view=ProviderView.as_view()),
]

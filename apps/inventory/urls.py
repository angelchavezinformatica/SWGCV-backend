from django.urls import path

from .views import InventoryView

urlpatterns = [
    path(route='all', view=InventoryView.as_view()),
]

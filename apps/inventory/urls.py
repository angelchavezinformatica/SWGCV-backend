from django.urls import path

from .views import InventoryAdminView, InventoryView

urlpatterns = [
    path(route='all', view=InventoryView.as_view()),
    path(route='admin', view=InventoryAdminView.as_view()),
]

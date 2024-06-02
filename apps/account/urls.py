from django.urls import path

from .views import Login, Register

urlpatterns = [
    path(route='login', view=Login.as_view()),
    path(route='register', view=Register.as_view()),
]

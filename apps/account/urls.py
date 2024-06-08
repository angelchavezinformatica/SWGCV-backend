from django.urls import path

from .views import Auth, Login, Register

urlpatterns = [
    path(route='auth', view=Auth.as_view()),
    path(route='login', view=Login.as_view()),
    path(route='register', view=Register.as_view()),
]

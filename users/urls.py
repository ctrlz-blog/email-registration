from django.urls import path

from . import views

from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path("register/", views.create_user, name="user_registration"),
    path("login/", views.Login.as_view(), name="login"),
    path("logout/", LogoutView.as_view(), name="logout")
]
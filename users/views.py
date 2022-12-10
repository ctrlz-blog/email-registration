from django.shortcuts import render
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView
from django.urls import reverse

class UserRegistration(CreateView):
    template_name = "user_registration.html"
    form_class = UserCreationForm

    def get_success_url(self):
        return reverse("login")


class Login(LoginView):
    template_name = "login.html"
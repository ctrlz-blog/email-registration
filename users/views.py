from django.shortcuts import render
from django.contrib.auth.views import LoginView
from django.http import HttpRequest, HttpResponse

def create_user(request: HttpRequest) -> HttpResponse:
    return render(request, "user_registration.html")

class Login(LoginView):
    template_name = "login.html"
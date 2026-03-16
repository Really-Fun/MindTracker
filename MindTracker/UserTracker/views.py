from django.views.generic import TemplateView, CreateView
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.forms import AuthenticationForm
from django.urls import reverse_lazy
from django.shortcuts import render

from UserTracker.forms import RegistrationUserForm


class MainPageView(TemplateView):
    template_name = "UserTracker/main_page.html"


class LoginUserView(LoginView):
    form_class = AuthenticationForm
    template_name = "UserTracker/login.html"
    extra_context = {"title": "Авторизация"}

    def get_success_url(self):
        return reverse_lazy("profile:stats")


class LogoutUserView(LogoutView):

    def get_success_url(self):
        return reverse_lazy("home")


class RegisterUserView(CreateView):
    form_class = RegistrationUserForm
    template_name = "UserTracker/register.html"

    def get_success_url(self):
        return reverse_lazy("profile:stats")


def custom_404_view(request, exception=None):
    return render(request, "404.html", status=404)

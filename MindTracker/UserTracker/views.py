from django.shortcuts import render
from django.views.generic import CreateView, TemplateView, DeleteView
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.forms import AuthenticationForm
from django.urls import reverse_lazy

from UserTracker.models import DailyLog
from UserTracker.forms import RegistrationUserForm


# Create your views here.
class DailyCheckUp(CreateView):
    template_name = "UserTracker/daily_check_up.html"
    model = DailyLog
    fields = ["mood", "took_magnesium", "notes"]

    def get_success_url(self):
        return reverse_lazy("stats")

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class IndexView(TemplateView):
    template_name = "UserTracker/index.html"
    model = DailyLog


class MainPageView(TemplateView):
    template_name = "UserTracker/main_page.html"


class LoginUserView(LoginView):
    form_class = AuthenticationForm
    template_name = "UserTracker/login.html"
    extra_context = {"title": "Авторизация"}

    def get_success_url(self):
        return reverse_lazy("stats")


class LogoutUserView(LogoutView):

    def get_success_url(self):
        return reverse_lazy("home")


class RegisterUserView(CreateView):
    form_class = RegistrationUserForm
    template_name = "UserTracker/register.html"
    success_url = reverse_lazy("stats/")

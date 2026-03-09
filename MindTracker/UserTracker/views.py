from datetime import date, timedelta

from django.shortcuts import render
from django.views.generic import CreateView, TemplateView, ListView, DetailView
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.forms import AuthenticationForm
from django.urls import reverse_lazy

from django.db.models import Avg

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


class CommitView(DetailView):
    template_name = "UserTracker/commit_detail.html"
    model = DailyLog
    slug_url_kwarg = "hash_slug"
    slug_field = "slug"
    context_object_name = "commit"


class IndexView(ListView):
    template_name = "UserTracker/index.html"
    model = DailyLog

    extra_context = {
        "title": "Stats | Mind Tracker",
    }

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user_logs = DailyLog.objects.filter(user=self.request.user).order_by("-date")

        streak = 0
        if user_logs.exists():
            today = date.today()

            last_log = user_logs[0].date
            expected_date = today
            count = 0

            for log in user_logs[1:]:
                if log.date == expected_date:
                    if count == 0:
                        count = 1
                    continue
                elif log.date == (expected_date - timedelta(days=1)):
                    count += 1
                else:
                    break

        magnesium_count = user_logs.filter(took_magnesium=True).count()
        magnesium_percent = int((magnesium_count / len(user_logs)) * 100)

        context["days_in_row"] = count
        context["average_mood"] = user_logs.aggregate(Avg("mood"))["mood__avg"]
        context["magnesium_in_percent"] = magnesium_percent

        return context


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
    success_url = reverse_lazy("stats")

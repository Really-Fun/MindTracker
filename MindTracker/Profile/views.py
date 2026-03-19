from datetime import date, timedelta

from django.http import Http404
from django.views.generic import (
    CreateView,
    ListView,
    DetailView,
    UpdateView,
    TemplateView,
)
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.db.models import Avg
from django.contrib.auth import get_user_model
from rest_framework import generics

from Profile.models import DailyLog
from .serizlizers import CommitsSerializer, UserSerializer


class DailyCheckUp(LoginRequiredMixin, CreateView):
    template_name = "UserTracker/daily_check_up.html"
    model = DailyLog
    fields = ["mood", "took_magnesium", "notes"]

    def get_success_url(self):
        return reverse_lazy("profile:stats")

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class CommitView(LoginRequiredMixin, DetailView):
    template_name = "UserTracker/commit_detail.html"
    model = DailyLog
    slug_url_kwarg = "hash_slug"
    slug_field = "slug"
    context_object_name = "commit"


class IndexView(LoginRequiredMixin, ListView):
    template_name = "UserTracker/index.html"
    model = DailyLog
    paginate_by = 10

    extra_context = {
        "title": "Stats | Mind Tracker",
    }

    def get_queryset(self):
        return DailyLog.objects.filter(user=self.request.user).order_by("-date")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user_logs = DailyLog.objects.filter(user=self.request.user).order_by("-date")

        streak = 0
        count = 0
        if user_logs.exists():
            today = date.today()

            last_log = user_logs[0].date
            expected_date = today
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
        if user_logs:
            magnesium_percent = int((magnesium_count / len(user_logs)) * 100)
        else:
            magnesium_percent = 0

        context["days_in_row"] = count
        context["average_mood"] = user_logs.aggregate(Avg("mood"))["mood__avg"]
        context["magnesium_in_percent"] = magnesium_percent

        return context


class ProfileSettings(LoginRequiredMixin, UpdateView):
    model = get_user_model()
    template_name = "Profile/settings.html"
    fields = ["username", "first_name", "avatar"]

    def get_success_url(self):
        return reverse_lazy("profile:stats")

    def get_object(self, queryset=None):
        return self.request.user


class BestCommitView(LoginRequiredMixin, DetailView):
    template_name = "UserTracker/commit_detail.html"
    model = DailyLog
    context_object_name = "commit"

    def get_object(self, queryset=None):
        best_commit = (
            self.model.objects.filter(user=self.request.user)
            .order_by("-mood", "-took_magnesium", "-date")
            .first()
        )

        if not best_commit:
            raise Http404(
                "У вас пока нет ни одного лога. Ваш лучший коммит еще впереди!"
            )

        return best_commit


class CommitsAPIView(LoginRequiredMixin, generics.ListAPIView):
    serializer_class = CommitsSerializer

    def get_queryset(self):
        return DailyLog.objects.filter(user=self.request.user).order_by("-date")


class UserInfoAPIView(LoginRequiredMixin, generics.ListAPIView):
    serializer_class = UserSerializer

    def get_queryset(self):
        return get_user_model().objects.filter(id=self.request.user.id)

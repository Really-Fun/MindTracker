from django.shortcuts import render
from django.views.generic import CreateView, TemplateView, DeleteView

from UserTracker.models import DailyLog


# Create your views here.
class DailyCheckUp(CreateView):
    template_name = "UserTracker/daily_check_up.html"
    model = DailyLog
    fields = ["mood", "took_magnesium", "notes"]

    success_url = "apply-changes"

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class IndexView(TemplateView):
    template_name = "UserTracker/index.html"
    model = DailyLog


class MainPageView(TemplateView):
    template_name = "UserTracker/main_page.html"

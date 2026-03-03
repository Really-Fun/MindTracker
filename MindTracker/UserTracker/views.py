from django.shortcuts import render
from django.views.generic import CreateView, TemplateView

from UserTracker.models import DailyLog


# Create your views here.
class DailyCheckUp(CreateView):
    template_name = "daily_check_up.html"
    model = DailyLog
    fields = ["mood", "took_magnesium", "notes"]

    success_url = "apply-changes"

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class IndexView(TemplateView):
    template_name = "index.html"


class MainPageView(TemplateView):
    template_name = "main_page.html"

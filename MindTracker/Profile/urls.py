from django.urls import path
from django.views.decorators.cache import cache_page

from Profile import views

app_name = "profile"

urlpatterns = [
    path("", views.IndexView.as_view(), name="stats"),
    path("daily-checkup/", views.DailyCheckUp.as_view(), name="checkup"),
    path("commit/<slug:hash_slug>", views.CommitView.as_view(), name="commit"),
    # path("settings/", views.ProfileSettings.as_view(), name="settings"),
    # path("best-commit/", views.BestCommit.as_view(), name="best-commit"),
]

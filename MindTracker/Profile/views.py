from django.urls import path
from django.views.decorators.cache import cache_page


urlpatterns = [
    path("profile/", views.IndexView.as_view(), name="stats"),
    path("profile/daily-checkup/", views.DailyCheckUp.as_view(), name="checkup"),
    path("profile/commit/<slug:hash_slug>", views.CommitView.as_view(), name="commit"),
    path("profile/settings/", views.ProfileSettings.as_view(), name="settings"),
    path("profile/best-commit/", views.BestCommit.as_view(), name="best-commit"),
]

from django.urls import path
from django.views.decorators.cache import cache_page
from UserTracker import views


urlpatterns = [
    path("/index", views.IndexView.as_view(), name="index"),
    path("/commit", views.DailyCheckUp.as_view(), name="daily-checkup"),
    path("", views.MainPageView.as_view(), name="main"),
]

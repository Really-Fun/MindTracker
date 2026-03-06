from django.urls import path
from django.views.decorators.cache import cache_page
from UserTracker import views


urlpatterns = [
    path("index/", views.IndexView.as_view(), name="index"),
    path("commit/", views.DailyCheckUp.as_view(), name="daily-checkup"),
    path("login/", views.LoginUserView.as_view(), name="login"),
    path("", views.MainPageView.as_view(), name="home"),
]

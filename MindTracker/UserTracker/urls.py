from django.urls import path
from django.views.decorators.cache import cache_page
from UserTracker import views


urlpatterns = [
    path("profile/", views.IndexView.as_view(), name="stats"),
    path("profile/daily-checkup/", views.DailyCheckUp.as_view(), name="checkup"),
    path("profile/commit/<slug:hash_slug>", views.CommitView.as_view(), name="commit"),
    path("login/", views.LoginUserView.as_view(), name="login"),
    path("register/", views.RegisterUserView.as_view(), name="register"),
    path("logout/", views.LogoutUserView.as_view(), name="logout"),
    path("", views.MainPageView.as_view(), name="home"),
]
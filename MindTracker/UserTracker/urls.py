from django.urls import path
from django.views.decorators.cache import cache_page
from UserTracker import views


urlpatterns = [
    path("login/", views.LoginUserView.as_view(), name="login"),
    path("register/", views.RegisterUserView.as_view(), name="register"),
    path("logout/", views.LogoutUserView.as_view(), name="logout"),
    path("", views.MainPageView.as_view(), name="home"),
]

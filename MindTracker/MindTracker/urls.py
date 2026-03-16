from django.conf.urls import handler404
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

import UserTracker.urls
import Profile.urls
from Profile.views import CommitsAPIView
from UserTracker.views import custom_404_view

urlpatterns = [
    path("admin/", admin.site.urls),
    path("profile/", include(Profile.urls)),
    path("", include(UserTracker.urls)),
    path("api/v1/womenlist/", CommitsAPIView.as_view()),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

admin.site.site_header = "Администрирование сайта MindTracker"
admin.site.index_title = "Привилегии"


handler404 = custom_404_view

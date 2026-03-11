from django.contrib import admin

from UserTracker.models import DailyLog, User

admin.site.register(DailyLog)
admin.site.register(User)

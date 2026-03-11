from django.contrib import admin

from UserTracker.models import DailyLog, User


@admin.register(DailyLog)
class DailyLogAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "notes", "date", "slug")
    list_display_links = ("user",)
    ordering = ["date", "id"]

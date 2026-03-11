from django.contrib import admin

from UserTracker.models import DailyLog, User


@admin.register(DailyLog)
class DailyLogAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "notes", "date", "slug", "count_chars")
    list_display_links = ("user",)
    ordering = ["date", "id"]

    @admin.display(description="Количество символов в заметках")
    def count_chars(self, daily_log: DailyLog) -> str:
        return f"{len(daily_log.notes)} символов"

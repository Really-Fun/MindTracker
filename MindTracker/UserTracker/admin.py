from django.contrib import admin

from UserTracker.models import DailyLog, User


@admin.register(DailyLog)
class DailyLogAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "notes", "date", "slug", "count_chars")
    list_display_links = ("user",)
    list_editable = ("notes",)
    ordering = ["date", "id"]
    search_fields = ["notes", "user__username"]
    list_filter = ["mood", "took_magnesium"]
    fields = ["notes", "took_magnesium", "mood"]
    readonly_fields = ["slug", "id", "user"]

    @admin.display(description="Количество символов в заметках", ordering="notes")
    def count_chars(self, daily_log: DailyLog) -> str:
        return f"{len(daily_log.notes)} символов"

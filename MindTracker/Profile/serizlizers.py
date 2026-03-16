from rest_framework import serializers
from .models import DailyLog


class CommitsSerializer(serializers.ModelSerializer):
    class Meta:
        model = DailyLog
        fields = ("user", "mood", "slug", "notes", "")
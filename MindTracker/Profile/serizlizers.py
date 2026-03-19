from rest_framework import serializers
from django.contrib.auth import get_user_model

from .models import DailyLog


class CommitsSerializer(serializers.ModelSerializer):
    class Meta:
        model = DailyLog
        fields = ("user", "mood", "slug", "notes")


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ("username", "first_name", "id")

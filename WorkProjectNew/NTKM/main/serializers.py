from rest_framework import serializers

from .models import Problem, AppUser


class ProblemSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Problem
        fields = "__all__"
        read_only_field = 'add_date'


class AppUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = AppUser
        fields = "__all__"

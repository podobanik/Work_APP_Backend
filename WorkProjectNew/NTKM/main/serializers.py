from rest_framework import serializers

from .models import Problem


class ProblemSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    add_date = serializers.HiddenField(default=0)

    class Meta:
        model = Problem
        fields = "__all__"

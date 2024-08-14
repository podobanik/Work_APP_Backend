from rest_framework import serializers

from .models import Problem, Staff


class ProblemSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Problem
        fields = "__all__"
        read_only_field = 'add_date'


class StaffSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Staff
        fields = "__all__"

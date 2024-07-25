from rest_framework import serializers
from .models import Problem


class ProblemSerializer(serializers.ModelSerializer):

    class Meta:
        model = Problem
        fields = ('pk', 'problem_text', 'staff', 'problem_type', 'problem_status', 'object_of_work', 'control_date')

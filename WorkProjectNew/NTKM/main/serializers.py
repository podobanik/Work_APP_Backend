from rest_framework import serializers
from .models import Problem


class ProblemSerializer(serializers.ModelSerializer):

    class Meta:
        model = Problem
        fields = ('pk', 'problem_text', 'staff', 'problem_status', 'object_of_work', 'problem_type', 'control_date', 'add_date', 'end_date')

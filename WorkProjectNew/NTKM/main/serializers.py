from rest_framework import serializers

from .models import Problem


class ProblemSerializer(serializers.ModelSerializer):
    staff = serializers.PrimaryKeyRelatedField(many=True)
    problem_type = serializers.PrimaryKeyRelatedField(many=True)
    problem_status = serializers.PrimaryKeyRelatedField(many=True)
    object_of_work = serializers.PrimaryKeyRelatedField(many=True)

    class Meta:
        model = Problem
        fields = ['pk', 'problem_text', 'staff', 'problem_type', 'problem_status', 'object_of_work', 'control_date']
    # pk = serializers.IntegerField()
    # problem_text = serializers.CharField(max_length=200)
    # staff = serializers.CharField(source='staff_id.staff_name', max_length=200)
    # problem_type = serializers.CharField(source='problem_type_id.problem_type_text', max_length=200)
    # problem_status = serializers.CharField(source='problem_status_id.problem_status_text', max_length=200)
    # object_of_work = serializers.CharField(source='object_of_work_id.object_of_work_text', max_length=200)
    # control_date = serializers.DateField()
    #
    # def create(self, validated_data):
    #     return Problem.objects.create(**validated_data)
    #
    # def update(self, instance, validated_data):
    #     instance.problem_text = validated_data.get('problem_text', instance.problem_text)
    #     instance.staff_id = validated_data.get('staff', instance.staff_id)
    #     instance.problem_type_id = validated_data.get('problem_type', instance.problem_type_id)
    #     instance.problem_status_id = validated_data.get('problem_status', instance.problem_status_id)
    #     instance.object_of_work_id = validated_data.get('object_of_work', instance.object_of_work_id)
    #     instance.control_date = validated_data.get('control_date', instance.control_date)
    #     instance.save()
    #     return instance

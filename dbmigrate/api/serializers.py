from rest_framework import serializers

from .models import Department, Job, Employee


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = "__all__"

    # def create(self, validated_data):
    #     instance = About.objects.create()
    #     for k, v in validated_data.items():
    #         setattr(instance, k, v)
    #     instance.save()
    #     return instance

    # def update(self, instance, validated_data):
    #     instance, validated_data = handle_file_field(
    #         instance, validated_data, "about_image", self.Meta.save_dir, mode="update"
    #     )
    #     return super().update(instance, validated_data)


class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = "__all__"


class JobSerializer(serializers.ModelSerializer):
    class Meta:
        model = Job
        fields = "__all__"

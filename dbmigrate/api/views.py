from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework import status

from core.views import CustomListCreateAPIView, CSVFileUploadListCreateAPIView
from .models import Employee, Department, Job
from .serializers import EmployeeSerializer, DepartmentSerializer, JobSerializer


class EmployeeListCreateView(CSVFileUploadListCreateAPIView):
    serializer_class = EmployeeSerializer
    csv_fields = ["id", "name", "datetime", "department", "job"]

    def clean_row(self, row):
        row["department"] = None if not row["department"] and not row["department"].strip().strip('"') else int(row["department"].strip().strip('"'))
        row["job"] = None if not row["job"] and not row["job"].strip().strip('"') else int(row["job"].strip().strip('"'))
        row["datetime"] = None if not row["datetime"] or not row["datetime"].strip().strip('"') else row["datetime"]
        return row

    def __init__(self, instance_type="employees", **kwargs):
        super().__init__(instance_type=instance_type, **kwargs)


class DepartmentListCreateView(CSVFileUploadListCreateAPIView):
    serializer_class = DepartmentSerializer
    csv_fields = ["id", "department"]

    def __init__(self, instance_type="departments", **kwargs):
        super().__init__(instance_type=instance_type, **kwargs)


class JobListCreateView(CSVFileUploadListCreateAPIView):
    serializer_class = JobSerializer
    csv_fields = ["id", "job"]
    queryset = Job.objects.all()

    def __init__(self, instance_type="jobs", **kwargs):
        super().__init__(instance_type=instance_type, **kwargs)

from django.db import models

# Create your models here.
class Department(models.Model):
    id = models.IntegerField(primary_key=True, null=False, blank=False)
    department = models.CharField(null=True, blank=True, max_length=80)


class Job(models.Model):
    id = models.IntegerField(primary_key=True, null=False, blank=False)
    job = models.CharField(null=True, blank=True, max_length=80)


class Employee(models.Model):
    id = models.IntegerField(primary_key=True, null=False, blank=False, unique=True)
    name = models.CharField(max_length=80, null=True, blank=True)
    datetime = models.DateTimeField(null=True, blank=True)
    department = models.ForeignKey(Department, related_name="department_id", on_delete=models.CASCADE, null=True, blank=True)
    job = models.ForeignKey(Job, related_name="job_id", on_delete=models.CASCADE, null=True, blank=True)


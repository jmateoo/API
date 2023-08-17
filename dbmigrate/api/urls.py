from django.urls import path

from . import views

app_name = "api"
urlpatterns = [
    path("employee", views.EmployeeListCreateView.as_view(), name="employee_list_create"),
    # path("<int:pk>", views.AboutRetrieveUpdateDestroyView.as_view(), name="detail"),
    path("department", views.DepartmentListCreateView.as_view(), name="department_list_create"),
    path("job", views.JobListCreateView.as_view(), name="job_list_create"),
]

from django.shortcuts import render
from rest_framework.generics import (
    CreateAPIView,
    ListAPIView,
    ListCreateAPIView,
    RetrieveAPIView,
    RetrieveUpdateAPIView,
    RetrieveUpdateDestroyAPIView,
)
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import FileUploadParser, MultiPartParser

# Create your views here.


def wrap_response(response, instance_type):
    if getattr(response, "data", None) is not None and "message" not in response.data and response.status_code != 204:
        new_data = response.data
        response_data = {
            "message": "success",
            "status_code": response.status_code,
            instance_type: new_data,
        }
        response.data = response_data
    return response


def enumerate_response(response):
    if getattr(response, "data", None) is not None and type(response.data) == list and "message" not in response.data:
        enumerated_data = response.data.copy()
        for idx, _ in enumerate(enumerated_data):
            enumerated_data[idx]["sl"] = idx + 1
        response.data = enumerated_data
    return response


class CustomRetrieveAPIView(RetrieveAPIView):
    # permission_classes = [CustomPermission]

    def __init__(self, instance_type=None, **kwargs):
        self.instance_type = instance_type
        super().__init__(**kwargs)

    def get(self, request, *args, **kwargs):
        response = super().get(request, *args, **kwargs)
        return wrap_response(response, self.instance_type)


class CustomRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    # permission_classes = [CustomPermission]

    def __init__(self, instance_type=None, **kwargs):
        self.instance_type = instance_type
        super().__init__(**kwargs)

    def get(self, request, *args, **kwargs):
        response = super().get(request, *args, **kwargs)
        return wrap_response(response, self.instance_type)

    def patch(self, request, *args, **kwargs):
        response = super().patch(request, *args, **kwargs)
        return wrap_response(response, self.instance_type)

    def put(self, request, *args, **kwargs):
        response = super().put(request, *args, **kwargs)
        return wrap_response(response, self.instance_type)

    def delete(self, request, *args, **kwargs):
        response = super().delete(request, *args, **kwargs)
        return wrap_response(response, self.instance_type)

    def perform_destroy(self, instance):
        serializer = self.get_serializer(instance)
        serializer.cleanup(instance)
        super().perform_destroy(instance)


class CustomCreateAPIView(CreateAPIView):
    # permission_classes = [CustomPermission]

    def __init__(self, instance_type=None, **kwargs):
        self.instance_type = instance_type
        super().__init__(**kwargs)

    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)
        return wrap_response(response, self.instance_type)


class CustomListAPIView(ListAPIView):
    # permission_classes = [CustomPermission]

    def __init__(self, instance_type=None, **kwargs):
        self.instance_type = instance_type
        super().__init__(**kwargs)

    def get(self, request, *args, **kwargs):
        response = super().get(request, *args, **kwargs)
        return wrap_response(response, self.instance_type)


class CustomListCreateAPIView(ListCreateAPIView):
    # permission_classes = [CustomPermission]

    def __init__(self, instance_type=None, **kwargs):
        self.instance_type = instance_type
        super().__init__(**kwargs)

    def get(self, request, *args, **kwargs):
        response = super().get(request, *args, **kwargs)
        return wrap_response(response, self.instance_type)

    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)
        return wrap_response(response, self.instance_type)


class EnumeratedListCreateAPIView(ListCreateAPIView):
    # permission_classes = [CustomPermission]

    def __init__(self, instance_type=None, **kwargs):
        self.instance_type = instance_type
        super().__init__(**kwargs)

    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)
        return wrap_response(response, self.instance_type)

    def get(self, request, *args, **kwargs):
        response = super().get(request, *args, **kwargs)
        return wrap_response(enumerate_response(response), self.instance_type)


class CustomRetrieveUpdateAPIView(RetrieveUpdateAPIView):
    # permission_classes = [CustomPermission]

    def __init__(self, instance_type=None, **kwargs):
        self.instance_type = instance_type
        super().__init__(**kwargs)

    def get(self, request, *args, **kwargs):
        response = super().get(request, *args, **kwargs)
        return wrap_response(response)

    def patch(self, request, *args, **kwargs):
        response = super().patch(request, *args, **kwargs)
        return wrap_response(response)

    def put(self, request, *args, **kwargs):
        response = super().put(request, *args, **kwargs)
        return wrap_response(response, self.instance_type)


class CustomAPIView(APIView):
    # permission_classes = [CustomPermission]

    def __init__(self, instance_type=None, **kwargs):
        self.instance_type = instance_type
        super().__init__(**kwargs)

    # def get(self, request, *args, **kwargs):
    #     response = Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
    #     return wrap_response(response, self.instance_type)

    # def post(self, response, *args, **kwargs):
    #     response = Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
    #     return wrap_response(response, self.instance_type)

    # def patch(self, response, *args, **kwargs):
    #     response = Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
    #     return wrap_response(response, self.instance_type)

    # def put(self, response, *args, **kwargs):
    #     response = Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
    #     return wrap_response(response, self.instance_type)

    # def delete(self, response, *args, **kwargs):
    #     response = Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
    #     return wrap_response(response, self.instance_type)


class CSVFileUploadListCreateAPIView(CustomAPIView):
    parser_classes = (MultiPartParser, )
    serializer_class = None
    csv_fields = []

    def clean_row(self, row):
        return row

    def post(self, request, *args, **kwargs):
        try:
            content = request.FILES["file"].read().decode()
            rows = []
            for line in content.splitlines():
                if not line.strip():
                    continue
                row = self.clean_row(dict(zip(self.csv_fields, line.strip().split(","))))
                rows.append(row)
            serializer = self.serializer_class(data=rows, many=True)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            response = Response(
                {
                    "message": "Data migrated",
                    "success": True
                }, status=status.HTTP_201_CREATED
            )
        except Exception as e:
            response = Response(
                {
                    "message": str(e),
                    "success": False
                }, status=status.HTTP_400_BAD_REQUEST
            )
        # return wrap_response(response, self.instance_type)
        message = "Database migrated successfully" if response.status_code==status.HTTP_201_CREATED else "Invalid CSV file"
        return render(request, "result.html", context={"message": message, "success": response.data["success"]})
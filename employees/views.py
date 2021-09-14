from django.shortcuts import render
from rest_framework import generics
from .models import *
from .serializers import *
from .filters import *
from django_filters import rest_framework as filters
from rest_framework.pagination import PageNumberPagination
# Create your views here.

class Page(PageNumberPagination):
    page_size = 10


class DepartmentListView(generics.ListCreateAPIView):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer

class DepartmentDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer

class EmployeesListView(generics.ListCreateAPIView):
    queryset= Employee.objects.all()
    serializer_class = EmployeeSerializer
    filter_backends= [filters.DjangoFilterBackend]
    filterset_class =  EmployeesFilter
    pagination_class = Page


class EmployeesDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset= Employee.objects.all()
    serializer_class = EmployeeSerializer
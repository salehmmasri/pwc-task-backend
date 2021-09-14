import django_filters as filters
from .models import Employee

class EmployeesFilter(filters.FilterSet):
    departments = filters.CharFilter(field_name='department__name', lookup_expr='exact')
    email = filters.CharFilter(field_name='email', lookup_expr='icontains')
    name = filters.CharFilter(field_name='name', lookup_expr='icontains')
    

   

    class Meta():
        model = Employee
        fields=['departments','email','name']

from django.urls import path
from .views import DepartmentDetailView, DepartmentListView, EmployeesDetailView, EmployeesListView


urlpatterns = [
    path('empolyees/',EmployeesListView.as_view(), name='EmployeesListView'),
    path('empolyees/<int:pk>',EmployeesDetailView.as_view(), name='EmployeesListView'),
    path('department/',DepartmentListView.as_view(), name='DepartmentListView'),
    path('department/<int:pk>',DepartmentDetailView.as_view(), name='DepartmentListView'),

]
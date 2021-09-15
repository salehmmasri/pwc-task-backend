from django.urls import path
from .views import DepartmentDetailView, DepartmentListView,EmployeesListAllView, EmployeesDetailView, EmployeesListView


urlpatterns = [
    path('empolyees/',EmployeesListView.as_view(), name='EmployeesListView'),
    path('empolyees/all',EmployeesListAllView.as_view(), name='EmployeesListAllView'),
    path('empolyees/<int:pk>',EmployeesDetailView.as_view(), name='EmployeesListView'),
    path('department/',DepartmentListView.as_view(), name='DepartmentListView'),
    path('department/<int:pk>',DepartmentDetailView.as_view(), name='DepartmentListView'),

]
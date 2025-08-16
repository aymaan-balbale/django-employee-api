from django.urls import path
from .views import (
    DepartmentListCreateAPIView, DepartmentRetrieveUpdateDestroyAPIView,
    EmployeeListCreateAPIView, EmployeeRetrieveUpdateDestroyAPIView,
    AttendanceListCreateAPIView, AttendanceRetrieveUpdateDestroyAPIView,
    analytics_view, # <-- The missing import
)

urlpatterns = [
    # The missing URL path for the chart
    path('analytics/', analytics_view, name='analytics'),

    # Existing API paths
    path('departments/', DepartmentListCreateAPIView.as_view(), name='department-list-create'),
    path('departments/<int:pk>/', DepartmentRetrieveUpdateDestroyAPIView.as_view(), name='department-detail'),
    path('employees/', EmployeeListCreateAPIView.as_view(), name='employee-list-create'),
    path('employees/<int:pk>/', EmployeeRetrieveUpdateDestroyAPIView.as_view(), name='employee-detail'),
    path('attendance/', AttendanceListCreateAPIView.as_view(), name='attendance-list-create'),
    path('attendance/<int:pk>/', AttendanceRetrieveUpdateDestroyAPIView.as_view(), name='attendance-detail'),
]
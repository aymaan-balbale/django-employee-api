import json
from django.shortcuts import render
from django.db.models import Count
from rest_framework import generics
from .models import Department, Employee, Attendance
from .serializers import DepartmentSerializer, EmployeeSerializer, AttendanceSerializer
from rest_framework.permissions import IsAuthenticated
from .permissions import IsHRorAdminUser

# For Department
class DepartmentListCreateAPIView(generics.ListCreateAPIView):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer

class DepartmentRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer

# For Employee
class EmployeeListCreateAPIView(generics.ListCreateAPIView):
    queryset = Employee.objects.select_related('department').all()
    serializer_class = EmployeeSerializer

    def get_permissions(self):
        """
        Instantiates and returns the list of permissions that this view requires.
        """
        if self.request.method == 'POST':
            # For POST requests, only HR or Admin can create.
            return [IsHRorAdminUser()]
        # For GET requests, any authenticated user can view.
        return [IsAuthenticated()]

class EmployeeRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Employee.objects.select_related('department').all()
    serializer_class = EmployeeSerializer

# For Attendance
class AttendanceListCreateAPIView(generics.ListCreateAPIView):
    queryset = Attendance.objects.select_related('employee').all()
    serializer_class = AttendanceSerializer

class AttendanceRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Attendance.objects.select_related('employee').all()
    serializer_class = AttendanceSerializer

def analytics_view(request):
    # Query to count employees in each department
    department_data = Department.objects.annotate(employee_count=Count('employees')).values('name', 'employee_count')

    # Prepare data for Chart.js
    dept_labels = [data['name'] for data in department_data]
    employee_counts = [data['employee_count'] for data in department_data]

    context = {
        'dept_labels': json.dumps(dept_labels),
        'employee_counts': json.dumps(employee_counts),
    }
    return render(request, 'employees/analytics.html', context)

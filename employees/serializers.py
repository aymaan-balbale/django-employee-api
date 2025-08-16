from rest_framework import serializers
from .models import Department, Employee, Attendance

class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = ['id', 'name']

class EmployeeSerializer(serializers.ModelSerializer):
    # This adds the department's name for easier reading
    department_name = serializers.CharField(source='department.name', read_only=True)

    class Meta:
        model = Employee
        fields = ['id', 'name', 'email', 'phone_number', 'department', 'department_name', 'position', 'salary', 'date_joined']

class AttendanceSerializer(serializers.ModelSerializer):
    # This adds the employee's name for easier reading
    employee_name = serializers.CharField(source='employee.name', read_only=True)

    class Meta:
        model = Attendance
        fields = ['id', 'employee', 'employee_name', 'date', 'status', 'check_in_time', 'check_out_time']
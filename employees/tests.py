from django.test import TestCase
from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth.models import User, Group
from .models import Department, Employee

class EmployeeAPITests(APITestCase):
    def setUp(self):
        # This method runs before every single test
        self.hr_group = Group.objects.create(name='HR')
        self.employee_group = Group.objects.create(name='Employee')

        # Create users
        self.hr_user = User.objects.create_user(username='hruser', password='password123')
        self.hr_user.groups.add(self.hr_group)

        self.employee_user = User.objects.create_user(username='empuser', password='password123')
        self.employee_user.groups.add(self.employee_group)

        # Create a department and an employee for testing GET requests
        self.department = Department.objects.create(name='Test Engineering')
        self.employee = Employee.objects.create(
            name='Test Employee',
            email='test@example.com',
            department=self.department,
            position='Tester',
            salary=60000

            
        )
    # Add these methods inside the EmployeeAPITests class

    def test_hr_can_list_employees(self):
        """
        Ensure a user in the HR group can view the list of employees.
        """
        # Authenticate as the HR user
        self.client.force_authenticate(user=self.hr_user)
        # Make the API call
        response = self.client.get('/api/employees/')
        # Check that the request was successful
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # Check that our test employee is in the response
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['name'], 'Test Employee')

    def test_employee_cannot_create_employee(self):
        """
        Ensure a regular employee cannot create a new employee record.
        """
        self.client.force_authenticate(user=self.employee_user)
        data = {
            'name': 'New Hire',
            'email': 'new@example.com',
            'department': self.department.id,
            'position': 'Newbie',
            'salary': 50000
        }
        response = self.client.post('/api/employees/', data)
        # We expect a "Forbidden" error
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_hr_can_create_employee(self):
        """
        Ensure an HR user CAN create a new employee record.
        """
        self.client.force_authenticate(user=self.hr_user)
        data = {
            'name': 'New Hire',
            'email': 'new@example.com',
            'department': self.department.id,
            'position': 'Newbie',
            'salary': 50000
        }
        response = self.client.post('/api/employees/', data, format='json')
        # We expect a "Created" success status
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        # Check that the employee count has increased to 2
        self.assertEqual(Employee.objects.count(), 2)    
# Create your tests here.

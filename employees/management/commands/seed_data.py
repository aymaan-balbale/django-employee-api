import random
from django.core.management.base import BaseCommand
from faker import Faker
from employees.models import Department, Employee, Attendance
from django.utils import timezone
from datetime import timedelta

class Command(BaseCommand):
    help = 'Seeds the database with dummy data'

    def handle(self, *args, **kwargs):
        self.stdout.write(self.style.SUCCESS('Starting to seed the database...'))

        # Clean up old data
        Attendance.objects.all().delete()
        Employee.objects.all().delete()
        Department.objects.all().delete()

        fake = Faker()

        # Create Departments
        departments = ['Human Resources', 'Engineering', 'Marketing', 'Sales', 'Finance']
        dept_objects = [Department.objects.create(name=d) for d in departments]
        self.stdout.write(self.style.SUCCESS(f'{len(dept_objects)} departments created.'))

        # Create Employees
        employees = []
        for _ in range(50): # Create 50 employees
            employee = Employee.objects.create(
                name=fake.name(),
                email=fake.unique.email(),
                phone_number=fake.phone_number(),
                department=random.choice(dept_objects),
                position=random.choice(['Manager', 'Developer', 'Analyst', 'Intern']),
                salary=random.randint(50000, 120000),
                date_joined=fake.date_between(start_date='-2y', end_date='today')
            )
            employees.append(employee)
        self.stdout.write(self.style.SUCCESS(f'{len(employees)} employees created.'))

        # Create Attendance Records for the last 30 days
        today = timezone.now().date()
        for employee in employees:
            for i in range(30):
                date = today - timedelta(days=i)
                status = random.choice(['Present', 'Present', 'Present', 'Absent', 'Leave'])
                check_in = None
                check_out = None
                if status == 'Present':
                    check_in = fake.time_object(end_datetime=None)
                    check_out = (timezone.datetime.combine(date, check_in) + timedelta(hours=random.randint(7, 9))).time()

                Attendance.objects.create(
                    employee=employee,
                    date=date,
                    status=status,
                    check_in_time=check_in,
                    check_out_time=check_out
                )
        self.stdout.write(self.style.SUCCESS('Attendance records created.'))
        self.stdout.write(self.style.SUCCESS('Database seeding complete!'))
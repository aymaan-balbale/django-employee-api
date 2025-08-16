
# Employee Management System API

## Overview

A complete Django application providing a REST API for managing employees, departments, and attendance. It includes database seeding, role-based authentication, unit tests, and a simple data visualization dashboard.

## Features

- **Backend:** Django 4.x, Django REST Framework
- **Database:** SQLite (for development)
- **API Documentation:** Swagger UI (`drf-yasg`)
- **Testing:** Automated unit tests for API endpoints.
- **Visualization:** Chart.js for an employee analytics dashboard.

## Local Setup Instructions

1.  **Clone the repository:**
    ```bash
    git clone <your-repository-link>
    cd <repository-folder-name>
    ```

2.  **Create and activate a virtual environment:**
    ```bash
    python -m venv venv
    # On Windows:
    venv\Scripts\activate
    ```

3.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Apply database migrations:**
    ```bash
    python manage.py migrate
    ```

5.  **Seed the database with dummy data:**
    ```bash
    python manage.py seed_data
    ```

6.  **Create a superuser to access the admin panel:**
    ```bash
    python manage.py createsuperuser
    ```

## Running the Application

1.  **Start the development server:**
    ```bash
    python manage.py runserver
    ```

2.  **Access Key URLs:**
    - **Admin Panel:** `http://127.0.0.1:8000/admin/`
    - **Swagger UI:** `http://127.0.0.1:8000/swagger/`
    - **Analytics Chart:** `http://127.0.0.1:8000/api/analytics/`
=======
# django-employee-api


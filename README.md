Task List - Django Web App

Overview

This is a simple task management web application built using Django. Users can create, update, search, and delete tasks. The app also includes user authentication (login/logout) and task categorization.

Features

User Authentication: Sign up, log in, and log out.

Task Management: Add, view, search, and delete tasks.

Categories: Organize tasks by category.

Search Functionality: Find tasks by title.

Installation

Prerequisites

Ensure you have the following installed:

Python (>=3.8)

Django (latest stable version)

Git (for version control)

Steps to Run the Project

Clone the repository:git clone https://github.com/yourusername/todolist.git
cd todolist

Create a virtual environment and activate it:
python -m venv myenv

source myenv/bin/activate  # macOS/Linux
myenv\Scripts\activate  # Windo

Install dependencies:
pip install -r requirements.txt

Apply migrations:
python manage.py migrate

Run the development server:
python manage.py runserver

Open http://127.0.0.1:8000/ in your browser.

Project Structure
todolist/                     # Root project directory
│── manage.py                 # Django management script
│── db.sqlite3                # SQLite database (if using SQLite)
│── myenv/                     # Virtual environment (optional)
│
├── todolist/                 # Main project directory
│   │── __init__.py           
│   │── settings.py           # Django settings
│   │── urls.py               # Project-level URL configuration
│   │── asgi.py
│   │── wsgi.py
│
├── todo/                     # Application directory
│   │── migrations/           # Database migrations
│   │── __init__.py
│   │── admin.py              # Django admin configurations
│   │── apps.py
│   │── models.py             # Database models
│   │── tests.py
│   │── views.py              # Views (business logic)
│   │── urls.py               # URL patterns for the app
│
├── templates/                # HTML templates
│   │── base.html             # Base template
│   │── login.html            # Login page
│   │── signup.html           # Signup page
│   │── task_list.html        # Task list page
│   │── logout.html        # Logout confirmation page
│
└── README.md                 # Project documentation

Usage

Login with your credentials.

Add a task by filling out the form.

Delete a task using the delete button.

Search for tasks using the search bar.

License

This project is licensed under the MIT License.

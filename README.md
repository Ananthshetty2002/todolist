# Task List - Django Web App

## Overview

This is a simple task management web application built using Django. Users can create, update, search, and delete tasks. The app also includes user authentication (login/logout) and task categorization.

## Features

- **User Authentication:** Sign up, log in, and log out.
- **Task Management:** Add, view, search, and delete tasks.
- **Categories:** Organize tasks by category.
- **Search Functionality:** Find tasks by title.

## Installation

### Prerequisites
Ensure you have the following installed:

- Python (>=3.8)
- Django (latest stable version)
- Git (for version control)

### Steps to Run the Project

1. Clone the repository:
   ```sh
   git clone https://github.com/yourusername/todolist.git
   cd todolist
   ```

2. Create a virtual environment and activate it:
   ```sh
   python -m venv myenv
   
   # macOS/Linux
   source myenv/bin/activate  
   
   # Windows
   myenv\Scripts\activate  
   ```

3. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```

4. Apply migrations:
   ```sh
   python manage.py migrate
   ```

5. Run the development server:
   ```sh
   python manage.py runserver
   ```

6. Open [http://127.0.0.1:8000/](http://127.0.0.1:8000/) in your browser.

## Project Structure
```
  todolist/                     # Root directory
  │── manage.py                 # Django management script
  │── db.sqlite3                # Database (if using SQLite)
  │── myenv/                    # Virtual environment (optional)
  │
  ├── todolist/                 # Main project directory
  │   ├── __init__.py           # Package initialization
  │   ├── settings.py           # Django settings
  │   ├── urls.py               # Project-level URLs
  │   ├── asgi.py, wsgi.py      # Deployment files
  │
  ├── todo/                     # App directory
  │   ├── __init__.py           # Package initialization
  │   ├── migrations/           # Database migrations
  │   ├── admin.py              # Admin configurations
  │   ├── models.py             # Database models
  │   ├── views.py              # Views (business logic)
  │   ├── urls.py               # App-level URLs
  │
  ├── templates/                # HTML templates
  │   ├── base.html, login.html, signup.html, task_list.html, logout.html
  │
  ├── static/                   # Static files (CSS, JS, images)
  │   ├── css/
  │   ├── js/
  │   ├── images/
  │
  └── README.md                 # Project documentation
```

## Usage

1. Login with your credentials.
2. Add a task by filling out the form.
3. Delete a task using the delete button.
4. Search for tasks using the search bar.

## License

This project is licensed under the MIT License.

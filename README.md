# 📝 Task List - Django Web App

## 📌 Overview

This is a simple task management web application built using **Django**. Users can create, update, search, and delete tasks. The app also includes **user authentication** and **task categorization**.

---

## 🚀 Features

* **User Authentication**: Sign up, log in, and log out
* **Task Management**: Add, view, search, and delete tasks
* **Categories**: Organize tasks by category
* **Search Functionality**: Find tasks by title

---

## ⚙️ Installation

### ✅ Prerequisites

Make sure the following are installed:

* Python (≥ 3.8)
* Django (latest stable version)
* Git

### 🛠️ Steps to Run the Project

1. **Clone the repository**

   ```bash
   git clone https://github.com/yourusername/todolist.git
   cd todolist
   ```

2. **Create and activate a virtual environment**

   * **macOS/Linux**:

     ```bash
     python -m venv myenv
     source myenv/bin/activate
     ```
   * **Windows**:

     ```cmd
     python -m venv myenv
     myenv\Scripts\activate
     ```

3. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Apply migrations**

   ```bash
   python manage.py migrate
   ```

5. **Run the development server**

   ```bash
   python manage.py runserver
   ```

6. Open your browser and go to:
   [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

---

## 🗂️ Project Structure

```
todolist/
│
├── manage.py
├── db.sqlite3
├── myenv/                     # Virtual environment (optional)
│
├── todolist/                  # Django project settings
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
│
├── todo/                      # Main app
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── tests.py
│   ├── views.py
│   ├── urls.py
│   └── migrations/
│
├── templates/                 # HTML Templates
│   ├── base.html
│   ├── login.html
│   ├── signup.html
│   ├── task_list.html
│   └── logout.html
│
└── README.md
```

---

## 💡 Usage

1. Log in with your credentials
2. Add tasks using the task form
3. Delete tasks with the delete button
4. Search tasks using the search bar

---

## 📄 License

This project is licensed under the [MIT License](LICENSE).



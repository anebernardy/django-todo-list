# To-Do List
[![Python](https://img.shields.io/badge/Python-3.14-blue)](https://www.python.org/) [![Django](https://img.shields.io/badge/Django-6.1-green)](https://www.djangoproject.com/)

A task management application built with Django to practice CRUD operations, forms, templates, and automated tests.


## Requirements

- Python 3.14+
- Git
- pip

## Features

- Create, edit and delete tasks
- Set task deadlines
- Validate deadlines when creating tasks
- Complete pending tasks
- Prevent editing completed tasks
- Use automated tests for forms and task actions

## Technologies

- Python
- Django
- Bootstrap


## Setup

1. Clone the repository and enter the project directory:
```bash
git clone https://github.com/anebernardy/django-todo-list.git
cd django-todo-list
```


2. Create and activate a virtual environment:
```bash
# macOS/Linux
python3 -m venv .venv
source .venv/bin/activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Create the environment file:
Copy `.env.example` to `.env` and set the values for your environment.

```env
DJANGO_SECRET_KEY=your-local-secret-key
DJANGO_DEBUG=True
DJANGO_ALLOWED_HOSTS=localhost,127.0.0.1
```

5. Apply the migrations:
```bash
python manage.py migrate
```

6. Start the development server:
```bash
python manage.py runserver
```

Open the application at [http://127.0.0.1:8000](http://127.0.0.1:8000/).


## Tests

Run the test suite with:
```bash
python manage.py test todo
```

---
This project was initially based on a [YouTube tutorial](https://www.youtube.com/watch?v=MsUL3Pgofl4&t=28s).
The application was adapted and extended with additional features, including deadline validation, task completion through POST requests, restrictions on editing completed tasks, and automated tests.

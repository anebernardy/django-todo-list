# Django To-Do List

A simple to-do list web application built with Django.

## Tech Stack
- Python
- Django
- SQLite

## Installation

1. Clone the repository
```bash
git clone https://github.com/your-username/django-todo-list.git
cd django-todo-list
```

2. Create and activate a virtual environment
```bash
python3 -m venv .venv
source .venv/bin/activate
```

3. Install dependencies
```bash
pip install -r requirements.txt
```

4. Create a .env filed based on .env.example
```bash
cp .env.example .env
```

5. Run migrations
```bash
python manage.py migrate
```

6. Start the development server
```bash
python manage.py runserver
```

Open:
http://127.0.0.1:8000

---
Based on a YouTube tutorial: 
https://www.youtube.com/watch?v=MsUL3Pgofl4&t=28s
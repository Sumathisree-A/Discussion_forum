# 🗣️ Django Discussion Forum

A fully functional threaded discussion forum built with Django and PostgreSQL. This project supports user authentication, threaded conversations, moderation tools, and follows Django best practices.

---

## 🚀 Features

- User registration, login, logout
- User profiles with bio
- Forum categories and threads
- Threaded discussions with replies
- Post creation and moderation
- Pagination for threads
- Admin-only moderation tools
- Class-based views (CBVs)
- PostgreSQL backend

---

## 🛠️ Tech Stack

- Python 3.8+
- Django 4.x
- PostgreSQL
- HTML/CSS (Bootstrap optional)
- Git for version control

---

## ⚙️ Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/Sumathisree-A/discussion_forum.git
cd discussion-forum
```

### 2. Create Virtual Environment

```bash
python -m venv venv
venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4.Configure PostgreSQL

```python
update Settings.py
DATABASES = {
  'default': {
    'ENGINE': 'django.db.backends.postgresql',
    'NAME': 'your_db_name',
    'USER': 'your_db_user',
    'PASSWORD': 'your_password',
    'HOST': 'localhost',
    'PORT': '5432',
  }
}
```
### 5. Run migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 6.Create Superuser

```bash
python manage.py createsuperuser
```

### 7. start server

```bash
python manage.py runserver
```
📄 License

This project is for educational purposes only.

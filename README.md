# StrayScan 🐾

StrayScan is a Django-based web application for **detecting** and **monitoring** stray animals.  
It allows users to report sightings, upload images, and track stray animals while providing an admin dashboard for management.

---

## 🧱 Features

- User registration, login, and profile management  
- Reporting a new stray (uploading images, specifying location, description)  
- Viewing list / map of reported strays  
- Admin dashboard for reviewing and validating reports  
- Notifications or status updates to report submitters  
- Photo handling, geolocation, filtering, search  

---
## 📁 Project Structure

```plaintext
StrayScan/
├── manage.py
├── strayscan/ # Main Django project folder
│ ├── settings.py
│ ├── urls.py
│ ├── wsgi.py
│ └── asgi.py
├── users/ # Example app: user management
│ ├── models.py
│ ├── views.py
│ ├── urls.py
│ ├── templates/
│ └── static/
├── reports/ # Example app: stray reports
│ ├── models.py
│ ├── views.py
│ ├── urls.py
│ ├── templates/
│ └── static/
├── media/ # Uploaded images
├── static/ # Collected static files
├── templates/ # Shared HTML templates
├── requirements.txt
└── README.md
```
---

## 🔧 Requirements & Setup

### Prerequisites

- Python 3.x  
- Django  
- Other dependencies (Pillow, Django REST Framework, etc.)  
- A database (SQLite, PostgreSQL, etc.)

### Installation & Running Locally

1. Clone the repo:  
   ```bash
   git clone https://github.com/vinzhenryyy/StrayScan.git
   cd StrayScan

2. (Optional) Create and activate a virtual environment:
   ```bash
    python -m venv venv
    source venv/bin/activate   # On Windows: venv\Scripts\activate
3. Install dependencies:
   ```bash
    pip install -r requirements.txt
4. Apply migrations:
   ```bash
    python manage.py migrate
5. (Optional) Create a superuser:
   ```bash
   python manage.py createsuperuser
6. Run the server:
   ```bash
   python manage.py runserver

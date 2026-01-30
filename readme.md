# Django Boilerplate v1

A reusable Django boilerplate project with a custom User model, admin enhancements, reusable models, static setup, and basic authentication endpoints (register, login, logout).  
This v1 release is **stable for starting new Django projects**. v2 will add Django REST Framework (DRF), JWT, and email verification.

---

## Features (v1)

- Custom User model 
- Fields: email, username, phone_number, avatar, is_verified, status, is_active, is_deleted, uuid, timestamps  
- Soft-delete support for models and users  
- Admin enhancements:
  - Avatar preview in admin
  - Soft-delete & restore actions
  - Filters and search
- Reusable models:
  - `TimeStampedModel` (created_at, updated_at)
  - `SoftDeleteModel` (soft-delete functionality)
  - `UUIDModel` (unique UUID for models)
  - `StatusModel` (active/inactive/status field)
- Static files setup with `/static/`  
- Logging to `/logs/django.log`  
- Basic authentication endpoints:
  - Register
  - Login
  - Logout

---

## Requirements

- Python 3.11+  
- Django 5.x  
- Pillow (for avatar/media support)  
- Whitenoise (for static files)
- SQLite (default, can switch to PostgreSQL later)  

---

## Installation

1. **Clone the repository**
```bash
git clone https://github.com/<username>/django-boilerplate.git
cd django-boilerplate
```

2. **Create and activate a virtual environment**
```bash
python -m venv venv
# Linux / macOS
source venv/bin/activate
# Windows
venv\Scripts\activate
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

4. **Set up environment variables**
```bash
cp .env.example .env
```

Edit `.env` with your settings (SECRET_KEY, DEBUG = True/False, database, etc.)

5. **Apply database migrations**
```bash
python manage.py makemigrations
python manage.py migrate
```

6. **Create a superuser**
```bash
python manage.py createsuperuser
```

7. **Run the development server**
```bash
python manage.py runserver
```

Visit `http://127.0.0.1:8000/admin` for the admin panel.

---

## Usage

- The boilerplate is ready to start building new Django apps.
- Users can extend the custom User model or add apps using the `apps/` folder.
- Soft-deleted users cannot log in; soft-deleted objects are hidden in admin by default.

---

## Next Steps (v2)

- Django REST Framework (DRF) integration
- JWT or token-based authentication
- Email verification / account activation
- Password reset & change endpoints
- PostgreSQL support
- Testing setup (pytest, fixtures, factories)

---

## Contributing

- Fork the repository and create a new branch for your feature/fix
- Submit a pull request
- Ensure new features are backward-compatible with v1

---

## License

MIT License

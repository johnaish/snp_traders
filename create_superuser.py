# create_superuser.py
import os
import django
from django.contrib.auth import get_user_model

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "myproject.settings")
django.setup()

User = get_user_model()

# Use environment variables for credentials for security
ADMIN_USERNAME = os.environ.get("ADMIN_USERNAME", "admin")
ADMIN_EMAIL = os.environ.get("ADMIN_EMAIL", "admin@example.com")
ADMIN_PASSWORD = os.environ.get("ADMIN_PASSWORD", "admin123")

if not User.objects.filter(username=ADMIN_USERNAME).exists():
    User.objects.create_superuser(ADMIN_USERNAME, ADMIN_EMAIL, ADMIN_PASSWORD)
    print(f"Superuser '{ADMIN_USERNAME}' created successfully.")
else:
    print(f"Superuser '{ADMIN_USERNAME}' already exists.")

#!/usr/bin/env python
import os
import sys

def main():
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'snp_traders.settings')

    # --- AUTO CREATE SUPERUSER ON RENDER STARTUP ---
    try:
        import django
        django.setup()
        from django.contrib.auth import get_user_model
        User = get_user_model()

        import create_superuser

        if not User.objects.filter(username="admin").exists():
            User.objects.create_superuser(
                username="admin",
                email="admin@example.com",
                password="admin123!"
            )
            print("✅ Superuser created: admin / admin123")
        else:
            print("ℹ️ Superuser already exists, skipping creation.")
    except Exception as e:
        # Will fail during manage.py collectstatic, ignore silently
        print(f"(Auto superuser setup skipped: {e})")

    # --- NORMAL DJANGO EXECUTION ---
    from django.core.management import execute_from_command_line
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()


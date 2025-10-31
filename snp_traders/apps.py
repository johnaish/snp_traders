from django.apps import AppConfig

class SnpTradersConfig(AppConfig):
    name = 'snp_traders'

    def ready(self):
        from django.contrib.auth.models import User
        if not User.objects.filter(username='admin').exists():
            User.objects.create_superuser('admin', 'admin@example.com', 'Admin123!')
            print("✅ Superuser created: admin / Admin123!")

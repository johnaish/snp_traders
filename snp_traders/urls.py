from django.contrib import admin
from django.urls import path
from django.contrib.auth.models import User
from django.http import HttpResponse

def create_admin(request):
    if not User.objects.filter(username="admin").exists():
        User.objects.create_superuser("admin", "admin@example.com", "Admin123!")
        return HttpResponse("✅ Superuser created: admin / Admin123!")
    return HttpResponse("⚠️ Admin user already exists")

urlpatterns = [
    path('create-admin/', create_admin),
    path('admin/', admin.site.urls),
]

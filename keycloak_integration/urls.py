from django.urls import path, include
from .views import get_keycloak_token
from django.contrib import admin

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('keycloak_Integration.urls')),
]

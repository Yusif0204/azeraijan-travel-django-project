from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),          # Админка
    path('', include('main.urls')),  
    path('accounts/', include('allauth.urls')),# Связываем с адресами нашего модуля
]
from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .views import City, Place  # Импортируем таблицы из нашего единого файла views

@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    list_display = ('name', 'region', 'population')

@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    list_display = ('name', 'city', 'category')
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_page, name='home'),                                 # Главная страница
    path('city/<int:city_id>/', views.city_detail_page, name='city_detail'), # Страница города
]
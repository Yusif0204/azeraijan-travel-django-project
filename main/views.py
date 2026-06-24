from django.shortcuts import render

# Create your views here.
from django.db import models
from django.shortcuts import render, get_object_or_404

# ===================================================
# ТАБЛИЦЫ БАЗЫ ДАННЫХ (Описываем города и места)
# ===================================================

class City(models.Model):
    """Таблица городов Азербайджана"""
    name = models.CharField(max_length=100, verbose_name="Название города")
    region = models.CharField(max_length=100, verbose_name="Регион")
    tagline = models.CharField(max_length=255, verbose_name="Слоган")
    description = models.TextField(verbose_name="Описание")
    population = models.CharField(max_length=50, verbose_name="Население")
    best_time = models.CharField(max_length=100, verbose_name="Лучшее время для визита")
    accent = models.CharField(max_length=7, default="#00afca", verbose_name="HEX-цвет акцента")
    image_url = models.URLField(max_length=500, blank=True, verbose_name="Ссылка на фото города")

    class Meta:
        verbose_name = "Город"
        verbose_name_plural = "Города"

    def __str__(self):
        return self.name


class Place(models.Model):
    """Таблица интересных мест (отели, рестораны, музеи)"""
    CATEGORY_CHOICES = [
        ('museum', 'Музей 🏛️'),
        ('hotel', 'Отель 🏨'),
        ('restaurant', 'Ресторан 🍽️'),
        ('nature', 'Природа 🌳'),
        ('history', 'История 🏰'),
    ]

    city = models.ForeignKey(City, on_delete=models.CASCADE, related_name='places', verbose_name="Город")
    name = models.CharField(max_length=150, verbose_name="Название места")
    description = models.TextField(verbose_name="Описание места")
    category = models.CharField(max_length=30, choices=CATEGORY_CHOICES, verbose_name="Категория")
    image_url = models.URLField(max_length=500, blank=True, verbose_name="Ссылка на фото места")

    class Meta:
        verbose_name = "Интересное место"
        verbose_name_plural = "Интересные места"

    def __str__(self):
        return self.name


# ===================================================
# ЛОГИКА СТРАНИЦ (Что показывать пользователю)
# ===================================================

def home_page(request):
    """Логика Главной страницы: берем из базы все города и отдаем в HTML"""
    cities = City.objects.all()
    return render(request, 'main/index.html', {'cities': cities})


def city_detail_page(request, city_id):
    """Логика Страницы города: берем один город по его ID и все его места"""
    city = get_object_or_404(City, id=city_id)
    places = city.places.all()
    return render(request, 'main/city_detail.html', {'city': city, 'places': places})
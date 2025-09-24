# Импорт стандартных компонентов Django
from django.shortcuts import render  # Функция для рендеринга шаблонов
from django import template  # Модуль для работы с шаблонами
from django.http import HttpResponse  # Класс для создания HTTP-ответов

# Определение представления (view) для главной страницы
def home(request):
    # Рендеринг шаблона static_handler.html и возврат ответа
    return render(request, 'templates/static_handler.html')

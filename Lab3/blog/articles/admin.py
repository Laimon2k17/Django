from django.contrib import admin
from .models import Article

# Класс для настройки отображения модели Article в админ-панели
class ArticleAdmin(admin.ModelAdmin):
    # Поля, которые будут отображаться в списке статей в админ-панели
    list_display = ('title', 'author', 'get_excerpt', 'created_date')

# Это связывает модель с настройками отображения в админке
admin.site.register(Article, ArticleAdmin)
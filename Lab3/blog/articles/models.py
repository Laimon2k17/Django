from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User

class Article(models.Model):
    # Заголовок статьи с максимальной длиной 200 символов
    title = models.CharField(max_length=200)
    
    # Связь с моделью User: каждая статья принадлежит одному автору.
    # on_delete=models.CASCADE гарантирует удаление всех статей пользователя при удалении его аккаунта.
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    
    # Основной текст статьи без ограничения длины
    text = models.TextField()
    
    # Дата создания статьи. Автоматически устанавливается при создании записи.
    created_date = models.DateField(auto_now_add=True)

    def __str__(self):
       # Строковое представление статьи в формате 'автор: заголовок
        return "%s: %s" % (self.author.username, self.title)

    def get_excerpt(self):
       # Если текст длиннее 140 символов, добавляет многоточие в конец.
        return self.text[:140] + "..." if len(self.text) > 140 else self.text
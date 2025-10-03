from django.shortcuts import render, redirect, get_object_or_404
from django.http import Http404
from .models import Article
from django.contrib.auth.decorators import login_required

# Функция для архива статей (должна была быть из предыдущих работ)
def archive(request):
    posts = Article.objects.all().order_by('created_date')
    return render(request, 'archive.html', {"posts": posts})

# Функция для просмотра отдельной статьи
def get_article(request, article_id):
    try:
        post = Article.objects.get(id=article_id)
        return render(request, 'article.html', {"post": post})
    except Article.DoesNotExist:
        raise Http404

# Функция для создания новой статьи (для лабораторной работы №5)
@login_required
def create_post(request):
    if request.method == "POST":
        # Обработка данных формы
        form = {
            'text': request.POST["text"],
            'title': request.POST["title"]
        }
        
        # Проверка на заполненность полей
        if form["text"] and form["title"]:
            # Проверка уникальности заголовка
            if Article.objects.filter(title=form["title"]).exists():
                form['errors'] = "Статья с таким заголовком уже существует"
                return render(request, 'create_post.html', {'form': form})
            
            # Создание новой статьи
            article = Article.objects.create(
                text=form["text"],
                title=form["title"],
                author=request.user
            )
            return redirect('get_article', article_id=article.id)
        else:
            # Если поля не заполнены
            form['errors'] = "Не все поля заполнены"
            return render(request, 'create_post.html', {'form': form})
    else:
        # Отображение пустой формы для GET-запроса
        return render(request, 'create_post.html', {})
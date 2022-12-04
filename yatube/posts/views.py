from django.http import HttpResponse
from django.shortcuts import render
 
 
def index(request):
    template = 'posts/index.html'
    title = 'Yatube главная страница'
    context = {
        'title': title,
        'text': 'Главная страница'
    }
    return render(request, template, context)
 
 
def group_list(request):
    template = 'posts/group_list.html'
    title = 'Yatube cписок групп'
    context = {
        'title': title,
        'text': 'Здесь будет информация о группах проекта Yatube'
    }
    return render(request, template, context)
 
 
def group_posts(request, slug):
    return HttpResponse(f'Пост №: {slug}')
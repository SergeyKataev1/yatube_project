from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse('Главная страница Ятуба')


def group_posts(request, slug):
    return HttpResponse(f'Пост СЛАГ Ятуба под любым названием на латинице с цифрами: {slug}')

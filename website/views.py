from django.shortcuts import render


def index(request):
    context = {'title': 'Главная страница'}
    return render(request, 'website/homepage.html', context=context)
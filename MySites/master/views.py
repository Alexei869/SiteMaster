from django.shortcuts import render

posts = [
    {
        'author': 'Пользователь 1',
        'title': 'первая заявка',
        'content': 'Содержание первой заявки.',
        'date_posted': '12 июня, 2023'
    },
    {
        'author': 'Пользователь 2',
        'title': 'вторая заявка',
        'content': 'Содержание второй заявки.',
        'date_posted': '13 июня, 2023'
    }
]


def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'master/home.html', context)


def about(request):
    return render(request, 'master/about.html', {'title': 'О сайте Master'})

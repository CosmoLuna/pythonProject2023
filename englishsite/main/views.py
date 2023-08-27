from django.shortcuts import render
from django.http import HttpResponse
from .models import Tiles


def index(request):
    return render(request, 'main/index.html')


def about(request):
    return render(request, 'main/about.html')


def resources(request):
    return render(request, 'main/resources.html')


def learn(request):
    return render(request, 'main/learn.html')


def c_books(request):
    books = Tiles.objects.all()
    return render(request, 'main/c_books.html', {'books': books})


def r_books(request):
    return render(request, 'main/r_books.html')


def games(request):
    return render(request, 'main/games.html')


def dialogues(request):
    return render(request, 'main/dialogues.html')


def terms(request):
    return render(request, 'main/terms.html')


def vocabulary(request):
    return render(request, 'main/vocabulary.html')

from django.shortcuts import render
from django.http import HttpResponse
from .models import Tiles
from .models import RBooks

from django.core.mail import send_mail
from django.conf import settings

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
    rbooks = RBooks.objects.all()
    return render(request, 'main/r_books.html', {'rbooks': rbooks})


def games(request):
    return render(request, 'main/games.html')


def dialogues(request):
    return render(request, 'main/dialogues.html')


def terms(request):
    return render(request, 'main/terms.html')


def vocabulary(request):
    return render(request, 'main/vocabulary.html')


def classes(request):
    # if request.method == "POST":
    #     message_name = request.POST['message-name']
    #     message_email = request.POST['message-email']
    #     message = request.POST['message']
    #
    #     send_mail(
    #         'Online classes',
    #         message,
    #         message_email,
    #         ['my@gmail.com'],
    #         fail_silently=False
    #     )
    #
    #     return render(request, 'main/classes.html')
    # else:
    #     return render(request, 'main/classes.html')
    return render(request, 'main/classes.html')


def texts(request):
    return render(request, 'main/texts.html')


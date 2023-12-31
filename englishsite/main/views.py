from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import *

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
    games = Game.objects.all()
    return render(request, 'main/games.html', {'games': games})


def dialogues(request):
    dialogues = Dialogue.objects.all()
    return render(request, 'main/dialogues.html', {'dialogues': dialogues})


def terms(request):
    return render(request, 'main/terms.html')


def vocabulary(request):
    voc = Voc.objects.all()
    return render(request, 'main/vocabulary.html', {'voc': voc})


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


def show_dialogue(request, dialogue_id):

    dialogue = get_object_or_404(Dialogue, pk=dialogue_id)

    context = {
        'dialogue': dialogue,
        'title': dialogue.title,
    }

    return render(request, 'main/dialogue.html', context=context)


def show_voc(request, voc_id):

    voc = get_object_or_404(Voc, pk=voc_id)
    word = Word.objects.all()

    context = {
        'voc': voc,
        'title': voc.title,
        'word': word,
        'cat_selected': voc.id,
    }

    return render(request, 'main/voc.html', context=context)


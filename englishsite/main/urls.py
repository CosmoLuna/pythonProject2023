from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('about-us', views.about, name='about'),
    path('resources', views.resources, name='resources'),
    path('learn', views.learn, name='learn'),
    path('resources/course-books', views.c_books, name='c_books'),
    path('resources/books-to-read', views.r_books, name='r_books'),
    path('resources/games', views.games, name='games'),
    path('learn/dialogues', views.dialogues, name='dialogues'),
    path('learn/vocabulary', views.vocabulary, name='vocabulary'),
    path('terms-and-conditions', views.terms, name='terms'),
    path('online-classes', views.classes, name='classes'),
    path('learn-texts', views.texts, name='texts'),
]

from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('about-us', views.about, name='about'),
    path('resources', views.resources, name='resources'),
    path('learn', views.learn, name='learn'),
    path('course-books', views.c_books, name='c_books'),
    path('books-to-read', views.r_books, name='r_books'),
    path('games', views.games, name='games'),
    path('dialogues', views.dialogues, name='dialogues'),
]

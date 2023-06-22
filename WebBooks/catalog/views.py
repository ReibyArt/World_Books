from django.shortcuts import render
from django.http import HttpResponse
from .models import Book, Author, BookInstance, Genre
from django.views import generic

def index(request):
    # Генерация "количеств" некоторых главных обьектов
    num_books = Book.objects.all().count()
    num_instances = BookInstance.objects.all().count()

    # Доступность книги (Статус - На складе)
    num_instances_available = BookInstance.objects.filter(status__exact=2).count()
    # Авторы книг
    num_authors = Author.objects.count()

    # Отрисовка HTML-шаблона index.html с данными внутри переменной context
    return render(request, 'index.html',
                  context={'num_books': num_books,
                           'num_instances': num_instances,
                           'num_instances_available': num_instances_available,
                           'num_authors': num_authors},
                            # 'num_visits': num_visits},
                  )

class BookListView(generic.ListView):
    model = Book

class BookDetailView(generic.DetailView):
    model = Book





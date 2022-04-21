from multiprocessing import context
from turtle import title
from django.shortcuts import redirect, render
from django.http import HttpResponse
from .models import Book, Author
from .forms import BookForm
from django.db import models
import os


def index(request):
    books = Book.objects.all()
    return render(request, 'books/index.html', context={'books': books})


def detail(request, id):
    book = Book.objects.get(id=id)
    # print(Author.objects.get(id=book.authors_id).id)

    book = {
        'title': book.title,
        'author': Author.objects.get(id=book.authors_id),
        'image': os.path.basename(book.image.url),
    }
    return render(request, 'books/detail.html', context={'book': book})


def getAuthor(request, id):
    author = Author.objects.get(id=id)
    author = {
        'first_name': author.first_name,
        'last_name': author.last_name,
        'books': author.books()
    }
    return render(request, 'books/author.html', context={'author': author})


def createBook(request):
    if request.method == 'POST':
        if (request.POST['title'] and request.POST['authors'] and request.POST['published_date'] and request.POST['price'] and request.POST['appropriate'] and request.POST['image']):
            book = Book.objects.create(
                title=request.POST['title'],
                authors_id=request.POST['authors'],
                published_date=request.POST['published_date'],
                price=request.POST['price'],
                appropriate=request.POST['appropriate'],
                image=request.POST['image'],
            )
            book.save()
            return redirect('/books', id=book.id)
    else:
        form = BookForm()
        return render(request, 'books/create.html', {'form': form})


def updateBook(request, id):
    book = Book.objects.get(id=id)
    if request.method == 'POST':
        if (request.POST['title'] and request.POST['authors'] and request.POST['published_date'] and request.POST['price'] and request.POST['appropriate'] and request.POST['image']):
            book = Book.objects.create(
                title=request.POST['title'],
                authors_id=request.POST['authors'],
                published_date=request.POST['published_date'],
                price=request.POST['price'],
                appropriate=request.POST['appropriate'],
                image=request.POST['image'],
            )
            book.save()
            return redirect('/books')
    else:
        form = BookForm(instance=book)
        return render(request, 'books/create.html', {'form': form})




def deleteBook(request, id):
    book = Book.objects.get(id=id)
    book.delete()
    return redirect('/books')

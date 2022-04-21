from django.urls import path
from .views import index, detail , getAuthor, createBook , updateBook , deleteBook

urlpatterns = [
    path('', index, name='index'),
    path('<int:id>/', detail, name='detail'),
    path('new/', createBook, name='create'),
    path('author/<int:id>/', getAuthor, name='detail'),
    path('update/<int:id>/', updateBook, name='updateBook'),
    path('delete/<int:id>/', deleteBook, name='deleteBook'),
]

from datetime import date
from tkinter import Widget
from django import forms
from .models import Book, Author



class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'authors', 'published_date', 'price', 'appropriate', 'image']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'authors': forms.SelectMultiple(attrs={'class': 'form-control'}),
            'published_date': forms.DateInput(attrs={'class': 'form-control'}),
            'price': forms.NumberInput(attrs={'class': 'form-control'}),
            'appropriate': forms.Select(attrs={'class': 'form-control'}),
            'image': forms.FileInput(attrs={'class': 'form-control'}),
        }



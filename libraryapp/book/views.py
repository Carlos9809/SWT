from django.shortcuts import render, redirect
from .models import Book
from .forms import BookCreate
from django.http import HttpResponse
#DataFlair
def index(request):
    libros = Book.objects.all()
    return render(request, 'libreria.html', {'todo': libros})

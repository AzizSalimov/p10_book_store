from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic import ListView

from books.models import Book


# Create your views here.
class HomeView(ListView):
    queryset = Book.objects.order_by("-id")
    template_name = 'home.html'
    context_object_name = 'books'



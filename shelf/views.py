from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

from django.views.generic import ListView, DetailView, View, TemplateView
from .models import Author, Book


"""class MainPageView(View):
    def get(self, request, *args, **kwargs):
        return HttpResponse('OK - klasa')"""

class MainPageView(TemplateView):
    template_name = 'index.html'


index_view = MainPageView.as_view()
#def index_view(requests, *args, **kwargs):
#    return HttpResponse('OK - funkcja')

class AuthorListView(ListView):
    model = Author


class AuthorDetailView(DetailView):
    model = Author


class BookListView(ListView):
    model = Book


class BookDetailView(DetailView):
    model = Book
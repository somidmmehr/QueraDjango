from django.http import HttpResponse
from django.shortcuts import render
from .models import *


# Create your views here.
def index(request):
    return HttpResponse("Welcome to library!")


def book_detail(request, book_id):
    try:
        book = Book.objects.get(pk=book_id)
    except Book.DoesNotExist:
        book = None
    context = {"book": book}
    return render(request, "book_detail.html", context=context)


def book_list(request):
    return render(request, "book_list.html", context={"books": Book.objects.all()})

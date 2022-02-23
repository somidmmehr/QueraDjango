from .models import *
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.views.decorators.csrf import csrf_exempt


# Create your views here.
def signup_view(request, name):
    return HttpResponse(f'Signup Completed! {name}')


def last_online(request):
    count = int(count) if (count := request.GET.get("count", 10)) != '' else 1
    people = Person.people.latest_logins(count).values_list('name', flat=True)
    splitter = '<br/>'
    response = splitter.join(map(str, people))
    return HttpResponse(response)


@csrf_exempt
def show_book(request):
    book_id = request.POST.get('book_id') or 2
    book = get_object_or_404(Book.objects.using("MySQL"), id=book_id)
    return HttpResponse(f'کتاب {book.name}')

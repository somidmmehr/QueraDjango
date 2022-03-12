from .models import *
from .forms import BookForm
from django.views.generic import *
from django.http import HttpResponse
from django.urls import reverse, reverse_lazy
from django.shortcuts import render, get_object_or_404
from django.views.decorators.csrf import csrf_exempt


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


class Users(ListView):
    queryset = Person.people.all()
    paginate_by = 2


class BookMixin:
    model = Book
    form_class = BookForm
    success_url = reverse_lazy('book-list')


class Books(BookMixin, ListView):
    pass


class NewBook(BookMixin, CreateView):
    template_name = 'first_app/book-create.html'


class EditBook(BookMixin, UpdateView):
    template_name = 'first_app/book-update.html'


class ShowBook(BookMixin, DetailView):
    template_name = 'first_app/book_detail.html'


class DeleteBook(BookMixin, DeleteView):
    template_name = 'first_app/book-delete.html'

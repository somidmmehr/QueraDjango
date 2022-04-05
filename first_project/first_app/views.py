from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LogoutView, LoginView
from django.utils.decorators import method_decorator
from .models import *
from .forms import BookForm, UserRegistration, LoginForm
from django.views.generic import *
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.shortcuts import render, get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate, login as dj_login


def home(request):
    return render(request, "first_app/index.html")


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


@method_decorator(login_required(login_url='/login/'), name='dispatch')
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


class Register0(View):
    def get(self, request):
        return render(request, 'first_app/registeration.html', context={'form': UserRegistration()})

    def post(self, request):
        form = UserRegistration(request.POST)
        if form.is_valid():
            user = form.save()
            dj_login(request, user)
            return HttpResponseRedirect(reverse_lazy('index'), status=200)
        else:
            return render(request, 'first_app/registeration.html', context={'form': form, 'message': form.errors})


class Register(FormView):
    template_name = 'first_app/registeration.html'
    success_url = reverse_lazy('index')
    form_class = UserRegistration

    def form_valid(self, form):
        user = form.save()
        dj_login(self.request, user)
        return super().form_valid(form)


@method_decorator(login_required(login_url='/login/'), name='dispatch')
class Logout(LogoutView):
    def get_next_page(self):
        url = self.request.GET.get('next')
        return url if url else reverse_lazy('index')


class Login(LoginView):
    template_name = 'first_app/login.html'
    authentication_form = LoginForm
    redirect_authenticated_user = True

    def get_success_url(self):
        url = self.request.GET.get('next')
        return url if url else reverse_lazy('index')

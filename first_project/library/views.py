from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from .models import *
from .forms import *
from django.views.decorators.csrf import csrf_exempt


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


@csrf_exempt
def signup(request):
    if request.method == "GET":
        return render(request, "signup.html", context={})
    elif request.method == "POST":
        test = {"email": "",
                "first_name": "sayyid omid",
                "last_name": "mousavi mehr",
                "password": "1234",
                "username": "mosavimehr"}

        form = SignUpForm(request.POST)
        state = form.is_valid()
        return JsonResponse({"error": form.errors, "POST": request.POST, "validity": state})


@csrf_exempt
def form(request):
    if request.method == "GET":
        sign_up_form = SignUpForm()
        return render(request, "form.html", context={'form': sign_up_form})
    if request.method == "POST":
        sign_up_form = SignUpForm(request.POST)
        if sign_up_form.is_valid():
            return render(request, "form.html", context={'message': "success"})
        else:
            return render(request, "form.html", context={'message': sign_up_form.errors, 'form': sign_up_form})


def signup2(request):
    if request.method == "GET":
        sign_form = SignUpForm2()
        return render(request, 'signup2.html', context={'form': sign_form})
    if request.method == "POST":
        sign_form = SignUpForm2(request.POST)
        if sign_form.is_valid():
            person = sign_form.save(commit=False)
            person.save(using="MySQL")
            return render(request, 'signup2.html', context={})
        else:
            return render(request, 'signup2.html', context={'form': sign_form})

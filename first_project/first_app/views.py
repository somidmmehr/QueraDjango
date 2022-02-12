from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def signup_view(request, name):
    return HttpResponse(f'Signup Completed! {name}')

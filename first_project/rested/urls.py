from rest_framework.authtoken.views import obtain_auth_token
from django.urls import path
from .views import *

urlpatterns = [
    path('', IndexAPI.as_view(), name='rest-home'),
    path('book/<int:book_pk>/', BookAPI.as_view(), name='book-api'),
    path('login/', view=obtain_auth_token),
]
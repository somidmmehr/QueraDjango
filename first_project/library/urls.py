from django.urls import path
from .views import *

urlpatterns = [
    path('', index),
    path('books/<int:book_id>/', book_detail, name='book_detail'),
    path('books/', book_list, name='book_list'),
    path('signup/', signup, name='signup')
]
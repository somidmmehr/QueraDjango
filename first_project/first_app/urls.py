from django.urls import path
from .views import *

urlpatterns = [
    path('signup/<str:name>/', signup_view),
    path('lasto/', last_online),
    path('book/<int:pk>', ShowBook.as_view(), name="book-detail"),
    path('users/', Users.as_view()),
    path('books/', Books.as_view(), name="book-list"),
    path('new-book/', NewBook.as_view(), name="new-book"),
    path('book-delete/<int:pk>/', DeleteBook.as_view(), name="book-delete"),
    path('book-edit/<int:pk>/', EditBook.as_view(), name="book-edit"),
]
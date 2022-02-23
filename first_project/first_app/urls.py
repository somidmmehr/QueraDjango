from django.urls import path
from .views import *

urlpatterns = [
    path('signup/<str:name>/', signup_view),
    path('lasto/', last_online),
    path('book/', show_book),
]
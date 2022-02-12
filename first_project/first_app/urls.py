from django.urls import path
from .views import *

urlpatterns = [
    path('signup/<str:name>/', signup_view),
]
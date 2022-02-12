from django.urls import  path
from first_app.views import signup_view

urlpatterns = [
    path('signup/<str:name>/', signup_view),
]
from django.urls import path
from . import views  # Import your views

urlpatterns = [
    path('', views.home, name='home'),  # URL for the home view
]

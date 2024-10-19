# formapp/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('submit/', views.submit_user_data, name='submit_user_data'),
    path('show-data/', views.show_user_data, name='show_data'),
    path('show-name-email/', views.show_name_email, name='show_name_email'),
    path('show-experience-picture/', views.show_experience_picture, name='show_experience_picture'),
]

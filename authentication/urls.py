
from django.urls import path
from . import views
# from django.contrib.auth.decorators import login_required



# from .views import due_tasks,task_graph  # Import your views


urlpatterns = [     
    path('', views.LoginPage, name='login'),  # URL for LoginPage
    path('signup/', views.SignUpPage, name='signup'),  # URL for SignUpPage
    path('logout/', views.LogoutPage, name='logout'),  # URL for LogoutPage
]
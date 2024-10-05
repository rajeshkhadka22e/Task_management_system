from django.urls import path
from . import views
# from .views import due_tasks,task_graph  # Import your views

urlpatterns = [
    path('', views.home, name='home'),  # URL for the home view
    # path('due-tasks/',due_tasks, name='due_tasks'), #URL for the due_tasks
    # path('task-graph/', task_graph, name='task_graph'), #URL for the task_graph
    path('profile/', views.profile, name='profile'), 
    path('profile_card/', views.profile_card, name='profile_card'), 
]

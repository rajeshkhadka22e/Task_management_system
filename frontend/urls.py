from django.urls import path
from . import views 
from django.contrib.auth.decorators import login_required



# from .views import due_tasks,task_graph  # Import your views

urlpatterns = [
    path('',views.home, name='home'),# URL for the home view
    # path('due-tasks/',views.due_tasks, name='due_tasks'), #URL for the due_tasks
    path('task-graph/', views.task_graph, name='task_graph'), #URL for the task_graph
    path('profile/', views.profile, name='profile'), 
    path('profile_success/', views.profile_success, name='profile_success'), 
    path('calender/', views.calender, name='calender'), 
    path('developer_personal_profile/<int:id>/', views.developer_personal_profile, name='developer_personal_profile'),
    path('due_task/', views.due_task, name='due_task'), 
    path('new_task_list/', views.new_task_list, name='new_task_list'), 

    path('add-task/', views.due_task, name='add_task'),  # URL for the task form submission
    # path('add-member/', views.add_member, name='add_member'), 
    
    path('project_member_detail/', views.project_member_detail, name='project_member_detail'), 
    path('task_graph/', views.task_graph, name='task_graph'), 
    path('task_time/', views.task_time, name='task_time'), 
    path('profile_card/', views.profile_card, name='profile_card'), 
    path('edit_task/<int:task_id>/', views.edit_task, name='edit_task'),

    path('api/events/', views.get_events, name='get_events'),

]

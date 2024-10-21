from django.shortcuts import render,redirect,get_object_or_404
# from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseBadRequest,HttpResponse,JsonResponse
from django.utils import timezone
from .models import Task, TaskList,UserProfile,TeamMember,Project,User,Event
from .forms import UserProfileForm
from django.contrib import messages
from .forms import EditTaskForm
from .forms import TaskForm,ProjectForm
from datetime import datetime
# Create your views here.
# def home(request):
#     return render(request,'index.html')


# class LogoutView():
#     def get(self, request):
#         logout(request)
#         return redirect('login') 


def home(request):
    task_lists = TaskList.objects.all()
    UserProfiles = User.objects.all()
    current_time = datetime.now()

    # Get the current hour using 24-hour format
    current_hour = current_time.hour
    
    # Determine greeting based on the time of day
    if current_hour < 12:
        greeting = "Good Morning"
    elif 12 <= current_hour < 17:
        greeting = "Good Afternoon"
    else:
        greeting = "Good Evening"
    
    # Format the current time to 12-hour clock with AM/PM
    formatted_time = current_time.strftime("%I:%M:%S %p")  # Example: 02:40:04 PM



    # return render(request, 'index.html', context)

# def home(request):
#     task_lists = TaskList.objects.all()
#     UserProfiles = User.objects.all()
#     current_time = datetime.now()

#     # Determine the greeting based on the current hour
#     if current_time.hour < 12:
#         greeting = "Good Morning"
#     elif 12 <= current_time.hour < 18:
#         greeting = "Good Afternoon"
#     else:
#         greeting = "Good Evening"

#     context = {
#         "profiles": UserProfiles,
#         "current_date": current_time,
#         "greeting": greeting  # Pass the greeting to the template
#     }

#     return render(request, 'index.html', context)

# Pranu ..........................
    total_tasks = Task.objects.count()
    ongoing_tasks = Task.objects.filter(status='ongoing').count()
    completed_tasks = Task.objects.filter(status='completed').count()
    overdue_tasks = Task.objects.filter(status='overdue').count()

    # Calculate percentage of completed tasks
    if total_tasks > 0:
        progress_percentage = (completed_tasks / total_tasks) * 100
    else:
        progress_percentage = 0

    # Get tasks that are upcoming (today or in the future)
    upcoming_tasks = Task.objects.filter(due_date__gte=timezone.now().date()).order_by('due_date')

    context = {
        "profiles": UserProfiles,
        "current_date": current_time,
        "greeting": greeting,
        "formatted_time": formatted_time, 
        "profiles":UserProfiles,
        'task_lists': task_lists,
        'total_tasks': total_tasks,
        'ongoing_tasks': ongoing_tasks,
        'completed_tasks': completed_tasks,
        'overdue_tasks': overdue_tasks,
        'progress_percentage': progress_percentage,
        'upcoming_tasks': upcoming_tasks,

     }

    # context = {
    #     "profiles":UserProfiles
    #     "current_date":current_date
    # }
    
    return render(request, 'index.html', context)


def due_tasks(request):
    # Query the database to get tasks that are due
    tasks = Task.objects.filter(due_date__lt='2024-10-10')  # Adjust the date as needed
    context = {
        'tasks': tasks
    }
    return render(request, 'due_task.html', context)

    # def task_graph(request):
    #     return render(request, 'task_graph.html')

def profile(request):
    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully!')
            return redirect('profile')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        # For a GET request, populate the form with the user's profile data
        form = UserProfileForm(instance=request.user)  # Prepopulate form with existing profile data

    return render(request, 'profile.html', {
        'form': form
    })



def profile_card(request):
    return render(request, 'profile_card.html')


def profile_success(request):
    return render(request, 'profile_success.html')



def calender(request):
    months = [...]  # Your months list
    month_calendars = [...]  # Your month_calendars list
    
    # Zip the two lists together
    zipped_months_calendars = zip(months, month_calendars)
    
    # Pass the zipped list to the template context
    return render(request, 'calender.html', {
        'zipped_months_calendars': zipped_months_calendars,
        'year': 2024,  # Example year
    })


def developer_personal_profile(request, id):
    UserProfiles = User.objects.all()
    context = {
        "profiles": UserProfiles
        }
    return render(request, 'developer_personal_profile.html',context)


def due_task(request):
    return render(request, 'due_task.html')




def new_task_list(request):
    Projects = Project.objects.all()
  
    context = {
        "Projects":Projects
    }
    return render(request, 'new_task_list.html',context)


def project_member_detail(request):
    # team_members = TeamMember.objects.all()
# {'team_members': team_members}
#  SAm
 team_members = TeamMember.objects.all()
 return render(request, 'project_member_detail.html', {'team_members': team_members})
#  SAm
# UserProfiles = User.objects.all()
#     print(UserProfiles)
#     context = {
#         "profiles":UserProfiles
#     }
#     return render(request, 'project_member_detail.html', context)

def task_graph(request):
    return render(request, 'task_graph.html')


def task_time(request):
    return render(request, 'task_time.html')


# #########################################
##############code from chatjpt ##########
##########################################


def edit_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('home')  # Redirect after successful edit
        else:
            return HttpResponse("Form is not valid")  # For debugging invalid forms
    else:
        form = TaskForm(instance=task)  # Pre-fill the form with task data

    return render(request, 'edit_task.html', {'form': form, 'task': task})



############for  making calender dynamic ##############
from django.http import JsonResponse
from .models import Event  # Assuming you have an Event model

def get_events(request):
    # Fetch events from the database
    events = Event.objects.all()
    
    # Format the events into a list of dictionaries
    event_list = []
    for event in events:
        event_list.append({
            'title': event.title,
            'start': event.start_date.strftime('%Y-%m-%d'),
            'end': event.end_date.strftime('%Y-%m-%d') if event.end_date else None,
        })

    return JsonResponse(event_list, safe=False)


# def add_task(request):
#     # Add your logic here
#     return render(request, 'due_task.html')

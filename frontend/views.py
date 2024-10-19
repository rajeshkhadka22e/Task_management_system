from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponseBadRequest,HttpResponse,JsonResponse
from django.utils import timezone
from .models import Task, TaskList,UserProfile,TeamMember,Project,User,Event
from .forms import UserProfileForm
from django.contrib import messages
from .forms import EditTaskForm
from .forms import TaskForm,ProjectForm

# Create your views here.
# def home(request):
#     return render(request,'index.html')



# class LogoutView():
#     def get(self, request):
#         logout(request)
#         return redirect('login') 



def home(request):
    task_lists = TaskList.objects.all()
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
        'task_lists': task_lists,
        'total_tasks': total_tasks,
        'ongoing_tasks': ongoing_tasks,
        'completed_tasks': completed_tasks,
        'overdue_tasks': overdue_tasks,
        'progress_percentage': progress_percentage,
        'upcoming_tasks': upcoming_tasks,
    }

    return render(request, 'index.html', context)

# def due_tasks(request):
#     # Query the database to get tasks that are due
#     tasks = Task.objects.filter(due_date__lt='2024-10-10')  # Adjust the date as needed
#     context = {
#         'tasks': tasks
#     }
#     return render(request, 'due_task.html', context)

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
    # profile = get_object_or_404(UserProfile, id=id)
    # rest of your view logic

    # Fetch the user profile or return 404 if not found
    # profile = get_object_or_404(UserProfile, id=id)
    
    # Render the profile page
    return render(request, 'developer_personal_profile.html')


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
    UserProfiles = User.objects.all()
    print(UserProfiles)
    context = {
        "profiles":UserProfiles
    }
    return render(request, 'project_member_detail.html', context)

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

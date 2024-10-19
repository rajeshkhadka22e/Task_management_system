# formapp/views.py
from django.shortcuts import render, redirect
from .forms import UserProfileForm
from .models import UserProfile

# View to handle form submission
def submit_user_data(request):
    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()  # Save the form data to the database
            return redirect('show_data')
    else:
        form = UserProfileForm()
    
    return render(request, 'submit_form.html', {'form': form})

# View to show all user data
def show_user_data(request):
    user_data = UserProfile.objects.all()
    return render(request, 'show_data.html', {'user_data': user_data})

# View to show specific data (name and email)
def show_name_email(request):
    user_data = UserProfile.objects.all()
    return render(request, 'show_name_email.html', {'user_data': user_data})

# View to show specific data (experience and profile picture)
def show_experience_picture(request):
    user_data = UserProfile.objects.all()
    return render(request, 'show_experience_picture.html', {'user_data': user_data})

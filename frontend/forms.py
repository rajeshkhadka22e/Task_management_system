from django import forms
from .models import User,Task,Project


# forms.py in your frontend app

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['duration', 'budget', 'description']

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name','last_name', 'email', 'role', 'profile_images']
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'mt-1 block w-full border-gray-300 rounded-md shadow-sm'}),
            'last_name': forms.TextInput(attrs={'class': 'mt-1 block w-full border-gray-300 rounded-md shadow-sm'}),
            'experienced': forms.TextInput(attrs={'class': 'mt-1 block w-full border-gray-300 rounded-md shadow-sm'}),
            'email': forms.EmailInput(attrs={'class': 'mt-1 block w-full border-gray-300 rounded-md shadow-sm'})

        }




class EditTaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'status', 'due_date']


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'status', 'due_date']  # Include any fields you want to edit
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseBadRequest, JsonResponse
from django.contrib import messages
from django.contrib.auth import get_user_model  # Correctly imported custom user model
from django.contrib.auth.decorators import login_required
from .forms import SignUpForm

# Get the correct User model
User = get_user_model()

# Logout view to log out users and redirect to the login page
@login_required  # Require login for this view
def LogoutPage(request):
    logout(request)  # Logs out the user
    return redirect('login')  # Redirects to login page after logout

# Sign up view, no login required here
def SignUpPage(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)  # Don't save the user just yet
            user.first_name = form.cleaned_data['first_name']
            user.last_name = form.cleaned_data['last_name']
            user.email = form.cleaned_data['email']
            user.save()  # Now save the user
            messages.success(request, "Registration successful. You can now log in.")
            return redirect('login')  # Redirect to login page after successful registration
        else:
            messages.error(request, "There was an error with your registration. Please correct the issues below.")
    else:
        form = SignUpForm()

    return render(request, 'signup.html', {'form': form})

def LoginPage(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            messages.error(request, 'Email is incorrect!')
            return redirect('login')

        # Authenticate using the username (not email, as authenticate expects a username)
        user = authenticate(request, username=user.username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Invalid credentials!')
            return redirect('login')

    return render(request, 'login.html')

# Optionally, you can apply login_required to any other view as needed

from django.shortcuts import render
# Create your views here.
from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth import authenticate, login, logout
# from django.contrib.auth.decorators import login_required
from django.http import HttpResponseBadRequest,HttpResponse,JsonResponse
from django.contrib import messages
from django.contrib.auth.models import User
 
# Create your views here.
# def home(request):
#     return render(request,'index.html')


# class LogoutView():
#     def get(self, request):
#         logout(request)
#         return redirect('login') 

#Sam
# def Homepage(request):
#     return render(request, 'Home.html')

def SignUpPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('pass1')
        password_confirm = request.POST.get('pass2')

        if password == password_confirm:
            # return render(request,'Login.html')
            if not User.objects.filter(username=username).exists():
                if not User.objects.filter(email=email).exists():
                    user = User.objects.create_user(username=username, email=email, password=password)
                    user.save()
                    messages.warning(request, 'Account created successfully!')
                    return redirect('login')
                else:
                    messages.error(request, 'Email already exists!')
            else:
                messages.error(request, 'Username already exists!')
        else:
            messages.error(request, 'Passwords do not match!')

    return render(request, 'signup.html')

def LoginPage(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            messages.error(request, 'Email is incorrect!')
            return redirect('login')  # Redirect back to login page if email is incorrect

        # Authenticate using the username (not email, as authenticate expects a username)
        user = authenticate(request, username=user.username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')  # Redirect to homepage after login
        else:
            messages.error(request, 'Invalid credentials!')  # Invalid password
            return redirect('login')

    return render(request, 'login.html')


# Logout view to log out users and redirect to the login page
def LogoutPage(request):
    logout(request)  # Logs out the user
    return redirect('login')  # Redirects to login page after logout

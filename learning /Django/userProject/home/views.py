from django.shortcuts import redirect, render
from django.contrib.auth.models import User, auth
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.http import HttpResponse

# Home Page View
def index(request):
    if request.user.is_anonymous:
        return redirect('login')  # Redirect to the login view
    return render(request, 'index.html')  # Render the index page for logged-in users

# Login View
def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)
        if user is not None:
            print(f"Authenticated user: {user}")  # Debugging statement
            auth_login(request, user)
            return redirect('/')  # Redirect to home page after successful login
        else:
            print("Authentication failed")  # Debugging statement
            return render(request, 'login.html', {'error': 'Invalid username or password'})
    return render(request, 'login.html')  # Render login form for GET requests

# Signup View
def signup(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        email = request.POST.get('email')

        # Check if the username already exists
        if User.objects.filter(username=username).exists():
            return render(request, 'signup.html', {'error': 'Username already taken'})

        # Create new user
        user = User.objects.create_user(username=username, password=password, email=email)
        user.save()
        return redirect('login')  # Redirect to login page after successful signup

    return render(request, 'signup.html')  # Render signup form for GET requests

# Logout View
def logout(request):
    auth_logout(request)
    return redirect('login')  # Redirect to login page after logout

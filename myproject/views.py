# myproject/views.py

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from vaccination.forms import SignupForm, LoginForm, AppointmentForm

def home(request):
    return render(request, 'home.html')

def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = SignupForm()
    return render(request, 'signup.html', {'form': form})

def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            user = form.get_user()
            auth_login(request, user)
            return redirect('home')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})

def logout(request):
    auth_logout(request)
    return redirect('home')

def search(request):
    if request.method == 'POST':
        location = request.POST['location']
        centers = Center.objects.filter(location__icontains=location)
        return render(request, 'search.html', {'centers': centers})
    return render(request, 'search.html')

def apply(request):
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            center_id = request.POST['center']
            center = Center.objects.get(id=center_id)
            if center.is_full():
                message = 'Sorry, the center is full for today. Please try again tomorrow.'
            else:
                form.save()
                message = 'Your appointment has been made successfully!'
            return render(request, 'apply.html', {'form': form, 'message': message})
    else:
        form = AppointmentForm()
    return render(request, 'apply.html', {'form': form})



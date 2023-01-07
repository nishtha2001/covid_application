from django.shortcuts import render,redirect
from .models import User, VaccinationCenter, Vaccination
from .forms import SignupForm, LoginForm
from django.contrib.auth import authenticate


def base(request):
    return render(request, 'base.html')

def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = authenticate(request, email=email, password=password)
            if user is not None:
                login(request, user)
                return redirect('base')
            else:
                return render(request, 'login.html', {'form': form, 'message': 'Invalid login credentials'})
        else:
            return render(request, 'login.html', {'form': form, 'message': 'Form is invalid'})
    else:
        form = LoginForm()
        return render(request, 'login.html', {'form': form})


def signup(request):
    if request.method == 'POST':
        # create new user
        email = request.POST['email']
        password = request.POST['password']
        password_confirm = request.POST['password_confirm']
        if password == password_confirm:
            user = User(email=email, password=password, role='user')
            user.save()
            return render(request, 'signup.html', {'message': 'Signup successful'})
        else:
            return render(request, 'signup.html', {'form': form, 'message': 'Passwords do not match'})
    else:
        # render signup form
        form = SignupForm()
        return render(request, 'signup.html', {'form': form})


def search(request):
    centers = VaccinationCenter.objects.all()
    return render(request, 'search.html', {'centers': centers})

def apply(request):
    if request.method == 'POST':
        # apply for vaccination
        user_id = request.session['user_id']
        user = User.objects.get(id=user_id)
        center_id = request.POST['center']
        center = VaccinationCenter.objects.get(id=center_id)
        # check if there are less than 10 candidates per day
        if Vaccination.objects.filter(date=date.today(), vaccination_center=center).count() < 10:
            vaccination = Vaccination(user=user, vaccination_center=center, date=date.today())
            vaccination.save()
            return render(request, 'apply.html', {'message': 'Your application has been received. You will be notified if you are selected for vaccination.'})
        else:
            return render(request, 'apply.html', {'message': 'Sorry, there are already 10 candidates for today. Please try again tomorrow.'})
    else:
        # render apply form
        return render(request, 'apply.html')


def logout(request):
    # clear session
    request.session.flush()
    return render(request, 'logout.html', {'message': 'You have been logged out.'})

def add_center(request):
    if request.method == 'POST':
        # create new center
        name = request.POST['name']
        location = request.POST['location']
        capacity = request.POST['capacity']
        center = VaccinationCenter(name=name, location=location, capacity=capacity)
        center.save()
        return render(request, 'add_center.html', {'message': 'Vaccination center added successfully.'})
    else:
        # render add center form
        return render(request, 'add_center.html')

def dosage(request):
    centers = VaccinationCenter.objects.all()
    return render(request, 'dosage.html', {'centers': centers})

def remove_center(request):
    if request.method == 'POST':
        # delete center
        center_id = request.POST['center']
        center = VaccinationCenter.objects.get(id=center_id)
        center.delete()
        return render(request, 'remove_center.html', {'message': 'Vaccination center removed successfully.'})
    else:
        # render remove center form
        centers = VaccinationCenter.objects.all()
        return render(request, 'remove_center.html', {'centers': centers})


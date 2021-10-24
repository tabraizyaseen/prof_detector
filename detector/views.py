from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from .forms import *
from . import detector_model
from .models import Upload

# Create your views here.
@login_required(login_url='login')
def home(request):

    if request.method == 'POST':
        form = UploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            # Get the current instance object to display in the template
            img_obj = form.instance

            results = detector_model.detection(img_obj)
            print(results)

            context = {
                'form': form,
                'img_obj': img_obj,
                'results': results,
            }
    else:
        form = UploadForm()
        context = {
            'form': form,
        }
    
    return render(request, 'detector/home.html', context)

def Signup(request):
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')

            # group = Group.objects.get(name='customer')
            # user.groups.add(group)
            # Customer.objects.create(user=user)

            messages.success(request, 'Account was created for ' + username)
            return redirect('login')
    context = {
        'form': form
    }
    return render(request, 'detector/signup.html', context)

def Login(request):

    if request.method == 'POST':
        name = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=name, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.success(request, 'Invalid Username or Password')
    context = {

    }
    return render(request, 'detector/login.html', context)

def Logout(request):
    logout(request)
    return redirect('login')
from django.shortcuts import render
from .forms import User_form, UserProfileForm
from .models import UserProfile, User
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.contrib.auth.decorators import login_required

from . import forms

# Create your views here.
def home(request):
    return render(request, 'loginApp/home.html')

# def users_list(request):
#     users = User.objects.all()
#     return render(request, 'loginApp/user_list.html', {'users': users})

def sign_up(request):
    registered = False
    if request.method == 'POST':
        user_form = User_form(data=request.POST)
        profile_form = UserProfileForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user

            if 'profile_image' in request.FILES:
                profile.profile_image = request.FILES['profile_image']

            profile.save()

            registered = True
        else:
            print(user_form.errors, profile_form.errors)

    else:
        user_form = User_form()
        profile_form = UserProfileForm()

    return render(request, 'loginApp/sign_up.html',{'registered':registered, "user_form":user_form, "user_profile":profile_form })


def user_login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username = username, password = password)

        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('home'))

            else:
                return HttpResponse("Your account is not active")
        else:
            print("someone tried to login and failed")
            return HttpResponse("Invalid User")

    return render(request, 'loginApp/login.html', {})

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('sign_up'))

def view_users(request):
    users = User.objects.all()
    return render(request, 'loginApp/users_list.html', {"users": users})

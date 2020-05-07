from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from .models import UserProfilePic
from .forms import User, ProfilePicForm, User_form
from django.contrib.auth import authenticate, logout, login
from django.contrib.auth.decorators import login_required
# Create your views here.


def sign_up(request):
    registered = False
    if request.method == "POST":
        user_form = User_form(request.POST)
        profile_pic_form = ProfilePicForm(request.POST)

        if user_form.is_valid() and profile_pic_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            profile = profile_pic_form.save(commit=False)
            profile.user = user

            if 'profile_pic'in request.FILES:
                profile.profile_pic =request.FILES['profile_pic']
            profile.save()
            registered = True
            return HttpResponseRedirect(reverse('index'))
        else:
            print(user_form.errors, profile_pic_form.errors)
    else:
        user_form = User_form()
        profile_pic_form = ProfilePicForm()

    return render(request, 'users/sign_up.html', {'registered':registered, 'user_form':user_form, "profile_pic": profile_pic_form})

def user_login(request):
    if request.method == "POST":

        username = request.POST.get('username')
        password =  request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('topics'))
            else:
                return HttpResponse("Your account is not active.")
        else:
            print('Someone tried to login and failed to login in')
            return HttpResponse("Invalid Username or password")
    else:
        return render(request, 'users/login.html')

@login_required()
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))
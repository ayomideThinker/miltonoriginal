# from django.shortcuts import render, get_object_or_404, redirect
import uuid 
import json
import requests
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from home.models import *
from . forms import *
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from userprofile.forms import *
from userprofile.models import *
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.conf import settings
from django.db.models import Q
from django.contrib.admin.views.decorators import staff_member_required


from django.core.paginator import Paginator
# Create your views here.


def milton(request):
    # return HttpResponse("Hello this is ayo from milton academy!")
    return render(request, 'milton.html')

@login_required(login_url='signin')
def sections(request):
    return render(request, 'sections.html')

def english(request):
    return render(request, 'english.html')

def mathematics(request):
    return render(request, 'mathematics.html')

def physics(request):
    return render(request, 'physics.html')

def economics(request):
    return render(request, 'economics.html')






def signin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('milton')
        else:
            return redirect('signin')
    return render(request, 'signin.html')

def logout_view(request):
    logout(request)
    return redirect('milton')


def signup(request):
    form = SignupForm()
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            newprofile = Profile(user=user)
            newprofile.username = user.username
            newprofile.first_name = user.first_name
            newprofile.last_name = user.last_name
            newprofile.email = user.email
            newprofile.save()
            login(request, user)
            messages.success(request, "Your account was created")
            # send_mail(
            #     "Thank You",
            #     "We got your message... and it will be attended to in due time",
            #     settings.EMAIL_HOST_USER,
            #     {user.email},
            #     fail_silently=False,
            # )
            return redirect('milton')
        else:
            messages.error(request, form.errors)
            return redirect('signup')
    return render(request, 'signup.html')

@login_required(login_url='signin')
def profile(request):
    profile = Profile.objects.get(user__username=request.user.username)
    context = {
        'profile': profile
    }

    return render(request, 'profile.html', context)

@login_required(login_url='signin')
def profile_update(request):
    profile = Profile.objects.get(user__username=request.user.username)
    update = ProfileUpdate(instance=request.user.profile)
    if request.method == 'POST':
        update = ProfileUpdate(request.POST, request.FILES, instance=request.user.profile)
        if update.is_valid():
            update.save()
            messages.success(request, 'User profile updated successfully')
            return redirect('profile')
        else:
            messages.error(request, update.errors)
            return redirect('profileupdate')
    context = {
        'profile': profile,
        'update': update,
    }
    return render(request, 'profile_update.html', context)

@login_required(login_url='signin')
def password(request):
    profile = Profile.objects.get(user__username= request.user.username)
    form = PasswordChangeForm(request.user)
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.success(request, 'Password change successfully!')
            return redirect('profile')
        else:
            messages.error(request, forms.errors)
            return redirect('password')
    context = {
        'profile': profile,
        'form': form,
    }
    return render(request, 'password.html', context)





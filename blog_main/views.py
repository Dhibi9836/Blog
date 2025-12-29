from django.shortcuts import render, redirect
from blogs.models import Category, Blog
from references.models import About
from .forms import RegistrationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import auth

def home(request) :
    featured_posts = Blog.objects.filter(is_featured = True, status = "Published").order_by('-updated_at')
    posts = Blog.objects.filter(is_featured = False, status = "Published").order_by('-updated_at')
    try :
        about = About.objects.get()
    except :
        about = None
    context = {
        "featured" : featured_posts,
        "posts" : posts,
        "about" : about
    }
    return render(request, 'home.html', context)

def register(request) :
    if request.method == 'POST' :
        form = RegistrationForm(request.POST)
        if form.is_valid() :
            form.save() 
            return redirect('register')
    else :
        form = RegistrationForm()
    return render(request, 'register.html', {'form' : form})

def login(request) :
    if request.method == 'POST' :
        form = AuthenticationForm(request, request.POST)
        if form.is_valid() :
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = auth.authenticate(username = username, password = password)
            if user is not None :
                auth.login(request, user)
            return redirect('dashboard')
    else :
        form = AuthenticationForm()
    return render(request, 'login.html', {"form" : form})

def logout(request) :
    auth.logout(request)
    return redirect('home')
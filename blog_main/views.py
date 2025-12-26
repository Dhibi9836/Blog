from django.shortcuts import render
from blogs.models import Category, Blog
from references.models import About

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
from django.shortcuts import render, get_object_or_404, redirect
# from django.http import HttpResponse
from .models import Blog, Category

def groupby_category(request, category_id) :
    posts = Blog.objects.filter(category = category_id, status = "Published")
    category_name = get_object_or_404(Category, pk = category_id)
    # try :
    #     category_name = Category.objects.get(pk = category_id)
    # except :
    #     return redirect("home")
    context = {'posts' : posts, 'category' : category_name}
    return render(request, "grouped_posts.html", context)
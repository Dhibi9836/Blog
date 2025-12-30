from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect
from .models import Blog, Category, Comment
from django.db.models import Q

def groupby_category(request, category_id) :
    posts = Blog.objects.filter(category = category_id, status = "Published").order_by("-created_at")
    category_name = get_object_or_404(Category, pk = category_id)
    # try :
    #     category_name = Category.objects.get(pk = category_id)
    # except :
    #     return redirect("home")
    context = {'posts' : posts, 'category' : category_name}
    return render(request, "grouped_posts.html", context)

def blogs(request, slug) :
    blog = get_object_or_404(Blog, slug = slug, status = "Published")
    if request.method == "POST" :
        comment = Comment()
        comment.user = request.user
        comment.blog = blog
        comment.comment = request.POST['comment']
        comment.save()
        return HttpResponseRedirect(request.path_info)
    comments = Comment.objects.filter(blog = blog).order_by("-created_at")
    counts = comments.count()
    context = {
        "blog" : blog,
        "comments" : comments,
        "counts" : counts
    }
    return render(request, 'blogs.html', context)

def search(request) :
    keyword = request.GET.get('keyword')
    blogs = Blog.objects.filter(Q(title__icontains = keyword) | Q(short_desc__icontains = keyword) | Q(blog_body__icontains = keyword), status = "Published")
    context = {"search_result" : blogs, "keyword" : keyword}
    return render(request, 'search.html', context)
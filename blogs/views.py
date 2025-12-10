from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from .models import Blog, Category

def posts_by_category(request, category_id):
    posts = Blog.objects.filter(status='Published', category=category_id)
    # for custom page we use try and except for that we need to false debug in settings and put * value 
    # try:
    #     category = Category.objects.get(pk=category_id)
    # except:
    #     return redirect('home')
    # for simple 404 error page 
    category = get_object_or_404(Category, pk=category_id)

    context = {
        'posts':posts,
        'category':category,
    }
    return render(request, 'posts_by_category.html', context)
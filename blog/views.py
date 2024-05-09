from django.shortcuts import render, get_object_or_404, redirect
from .models import Post,Category
from django.core.paginator import PageNotAnInteger, EmptyPage, Paginator

# Create your views here.

def home(req, category_name = None):
    
    categories = None
    post = None
    if category_name is not None:
        categories = get_object_or_404(Category, category_name = category_name)
        post = Post.objects.filter(category=categories).order_by('-created')
        paginator = Paginator(post, 10)
        page = req.GET.get('page')
        post_paginator = paginator.get_page(page)

    else:
        post = Post.objects.all().order_by('-created')
        paginator = Paginator(post, 10)
        page = req.GET.get('page')
        post_paginator = paginator.get_page(page)

        

    context = {'post':post_paginator}
    return render(req, 'blog/home.html', context)


def single_post(req, pk):
    post = Post.objects.get(id = pk)
    context = {'post':post}
    return render(req, 'blog/single-post.html', context)



def search(req):
    try:
        if 'keyword' in req.GET:
            keyword = req.GET['keyword']
            if keyword:
                post = Post.objects.filter(title__icontains = keyword)
    except:
        pass

    paginator = Paginator(post, 10)
    page = req.GET.get('page')
    post_paginator = paginator.get_page(page)
    context = {'post':post_paginator, 'keyword':keyword}

    return render(req, 'blog/search.html', context)

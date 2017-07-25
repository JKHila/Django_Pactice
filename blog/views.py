from django.shortcuts import render, get_object_or_404, redirect
from .models import Post
from django.utils import timezone
from .forms import PostForm

from .w2v import *


def var_test(request):
    place = []
    place.append(request.GET["name"])
    if(request.GET["cate"]):
        place.append(request.GET["cate"])
    places = getWords(place)
    return render(request, 'blog/var_test.html',{'places': places})

def post_list(request):
    posts = Post.objects.order_by('-published_date')
    return render(request, 'blog/post_list.html', {'posts':posts})

def post_detail(request,pk):
     post = get_object_or_404(Post, pk=pk)
     return render(request,'blog/post_detail.html', {'post':post})

def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail',pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html',{'form':form})

def post_edit(request,pk):
    post = get_object_or_404(Post,pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail',pk=post.pk)
    else:
        form = PostForm(instance = post)
    return render(request, 'blog/post_edit.html',{'form':form})
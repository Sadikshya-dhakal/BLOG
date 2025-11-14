from django.shortcuts import render, redirect
from blog_app.models import Post
from blog_app.forms import PostForm
from django.contrib.auth.decorators import login_required
from django.utils import timezone

# function based views
# Create your views here.
def post_list(request):
    posts = Post.objects.filter(published_at__isnull=False).order_by("-published_at")
    return render(
        request,
        "post_list.html",
        {"posts": posts},
    )



def post_detail(request, pk):
    post = Post.objects.get(pk=pk)
    return render(
        request,
        "post_detail.html",
        {"post": post},
    )

@login_required
def post_create(request):
    if request.method == "GET":
        form = PostForm()
        return render(
            request,
            "post_create.html",
            {"form": form},
        )
    else:
        form = PostForm(request.POST)  # form => data validate garxa 

        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect("post_list")
        else:
            return render(
                request,
                "post_create.html",
                {"form": form},
            )
        

@login_required
def draft_list(request):
    posts =Post.objects.filter(published_at__isnull=True)
    return render(
        request,
        "draft_list.html",
        {"posts": posts},
    )

@login_required
def draft_detail(request, pk):
    post = Post.objects.get(pk=pk, published_at__isnull=True)
    return render(
        request,
        "draft_detail.html",
        {"post": post},
    )

@login_required
def post_update(request,pk):
    if request.method == "GET":
        post= Post.objects.get(pk=pk)
        form = PostForm(instance=post)
        return render(
            request,
            "post_create.html",
            {"form": form},
        )
    else:
        post= Post.objects.get(pk=pk)
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save()
            if post.published_at:
                return redirect("post_detail", pk=post.pk)
            else:
                return redirect("draft_detail", pk=post.pk)
        else:
            return render(
                request,
                "post_create.html",
                {"form": form},
            )
       
@login_required
def post_delete(request,pk):
    post = Post.objects.get(pk=pk)
    post.delete()
    if post.published_at:
        return redirect("post_list")
    else:
        return redirect("draft_list")
    
@login_required
def draft_publish(request, pk):
    post = Post.objects.get(pk=pk, published_at__isnull=True)
    post.published_at = timezone.now()
    post.save()
    return redirect("post_list")

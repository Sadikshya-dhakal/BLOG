from django.shortcuts import render, redirect
from blog_app.models import Post
from blog_app.forms import PostForm
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.views.generic import ListView, DetailView, CreateView, UpdateView, View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse


# class based views
# Create your views here.

class PostListView(ListView):
    model = Post
    template_name = "post_list.html"
    context_object_name = "posts"

    def get_queryset(self): # filter gareko queryset return garxa
        posts = Post.objects.filter(published_at__isnull=False).order_by(
            "-published_at"
        )
        return posts


class PostDetailView(DetailView):
    model = Post
    template_name = "post_detail.html"
    context_object_name = "post"
    
    def get_queryset(self):
       queryset = Post.objects.filter(pk=self.kwargs['pk'], published_at__isnull=False)
       return queryset
    

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    template_name = "post_create.html"
    form_class = PostForm

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
    def get_success_url(self):
        return reverse("draft_detail", kwargs={"pk": self.object.pk})


  

class DraftListView(LoginRequiredMixin, ListView):
    model = Post
    template_name = "draft_list.html"
    context_object_name = "posts"

    def get_queryset(self):
        queryset = Post.objects.filter(published_at__isnull=True)
        return queryset
    

class DraftDetailView(LoginRequiredMixin, DetailView):
    model = Post
    template_name = "draft_detail.html"
    context_object_name = "post"

    def get_queryset(self):
        queryset = Post.objects.filter(pk=self.kwargs["pk"], published_at__isnull=True)
        return queryset


class PostUpdateView(LoginRequiredMixin, UpdateView):
    model=Post
    template_name="post_create.html"
    form_class=PostForm

    def get_success_url(self):
        post = self.object()
        if post.published_at:
            return reverse("post_detail", kwargs={"pk": post.pk})
        else:
            return reverse("draft_detail", kwargs={"pk": post.pk})
        


class PostDeleteView(LoginRequiredMixin, View):
    def get(self, request, pk):
        post = Post.objects.get(pk=pk)
        post.delete()
        if post.published_at:
           return redirect("post_list")
        else:
           return redirect("draft_list")

class DraftPublishView(LoginRequiredMixin, View):
    def get(self, request, pk):
        post = Post.objects.get(pk=pk, published_at__isnull=True)
        post.published_at = timezone.now()
        post.save()
        return redirect("post_list")
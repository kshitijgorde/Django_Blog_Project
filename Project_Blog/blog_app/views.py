from django.shortcuts import render
from django.views.generic import (ListView, TemplateView, CreateView, UpdateView, DeleteView)
from blog_app.models import Post, Comment
from django.utils import timezone
from django.contrib.auth.mixins import LoginRequiredMixin
from blog_app.forms import PostForm, CommentForm
from django.urls import reverse_lazy
# Create your views here.


class AboutView(TemplateView):
    template_name = 'about.html'

class PostListView(ListView):
    model = Post

    # Now, to list all the blog post, just filter them by published date in descending order
    def get_queryset(self):
        return Post.objects.filter(published_date__lte = timezone.now()).order_by('-published_date')

class PostDetailView(DetailView):
    model = Post

#We will required a mixin for creating a new blog post
class CreatePostView(LoginRequiredMixin, CreateView):
    login_url = '/login/'
    redirect_field_name = 'blog_app/post_details.html'

    form_class = PostForm
    model = Post

#Updating Blogs

class PostUpdateView(LoginRequiredMixin, UpdateView):
    login_url = '/login/'
    redirect_field_name = 'blog_app/post_details.html'

    form_class = PostForm
    model = Post

class PostDeleteView(LoginRequiredMixin, DeleteView):
    model = Post
    success_url = reverse.lazy('post_list')

class DraftListView(LoginRequiredMixin, ListView):
    login_url = '/login'
    redirect_field_name = '/blog_app/post_list.html'
    model = Post

    def get_queryset(self):
        return Post.objects.filter(published_date__isnull = True).order_by('created_date')

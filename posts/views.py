from django.shortcuts import render
from django.views.generic import ListView
from .models import Post, PostForm

# Create your views here.
class HomePageView(ListView):
    model = Post
    template_name = "home.html"

class AboutPageView(ListView):
    model = PostForm
    template_name = "about.html"
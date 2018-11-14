from django.shortcuts import render
from .models import Blog


def allblogs(request):
    posts = Blog.objects
    return render(request, 'allblogs.html', {'posts':posts})
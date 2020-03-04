from django.shortcuts import render
from blog.models import Blog,Blog_Type

def home(request):
    context = {}
    context['blogs'] = Blog.objects.all()
    return render(request, 'home.html', context)
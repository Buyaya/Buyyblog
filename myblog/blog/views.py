from django.shortcuts import render,get_object_or_404
from .models import Blog,Blog_Type

# Create your views here.

def blog_detail(request, blog_pk):
    context = {}
    context['blog'] = get_object_or_404(Blog, pk=blog_pk)
    return render(request, 'blog/blog_detail.html', context)

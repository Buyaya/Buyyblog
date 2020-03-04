from django.contrib import admin
from .models import Blog_Type,Blog

# Register your models here.

@admin.register(Blog_Type)
class BlogTypeAdmin(admin.ModelAdmin):
    list_display = ('id','type_name')
    ordering = ('id',)

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('title','author','blog_type','created_time','last_update_time')
    ordering = ('-created_time',)

from django.contrib import admin
from .models import Profile, Post

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "avatar_path")

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("id", "username", "likes_count", "created_at")
    search_fields = ("username", "caption")

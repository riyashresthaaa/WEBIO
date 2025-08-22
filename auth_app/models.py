# auth_app/models.py
from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    avatar_path = models.CharField(max_length=255, default="img/user.png")

    def __str__(self):
        return f"{self.user.username} profile"


class Post(models.Model):
    username = models.CharField(max_length=150)         
    image_path = models.CharField(max_length=255)        
    caption = models.CharField(max_length=300, blank=True)
    likes_count = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.username} - {self.caption[:20]}"

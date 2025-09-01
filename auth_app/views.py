from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404

from .models import Profile, Post 

def signup_view(request):
    if request.method == "POST":
        username = request.POST.get("username", "").strip()
        email = request.POST.get("email", "").strip()
        password1 = request.POST.get("password1", "")
        password2 = request.POST.get("password2", "")

        if not username or not email or not password1 or not password2:
            messages.error(request, "All fields are required.")
            return render(request, "auth_app/signup.html")

        if password1 != password2:
            messages.error(request, "Passwords do not match.")
            return render(request, "auth_app/signup.html")

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already taken.")
            return render(request, "auth_app/signup.html")

        if User.objects.filter(email=email).exists():
            messages.error(request, "Email already registered.")
            return render(request, "auth_app/signup.html")

        user = User.objects.create_user(username=username, email=email, password=password1)

        
        Profile.objects.create(user=user) 

        login(request, user)
        return redirect("index")

    return render(request, "auth_app/signup.html")


def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username", "").strip()
        password = request.POST.get("password", "")
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect("index")
        messages.error(request, "Invalid username or password.")
    return render(request, "auth_app/login.html")


def logout_view(request):
    logout(request)
    return redirect("login")


@login_required
def index_view(request):
    profile, _ = Profile.objects.get_or_create(user=request.user)

    posts = Post.objects.all()
    suggestions = User.objects.exclude(id=request.user.id)[:10]

    return render(request, "index.html", {
        "profile": profile,
        "posts": posts,
        "suggestions": suggestions,
    })


@login_required
def profile_view(request):
    profile, _ = Profile.objects.get_or_create(user=request.user)
    return render(request, "pages/profile.html", {"profile_user": request.user, "profile": profile})

@login_required
def messages_view(request):
    return render(request, "pages/messages.html")

@login_required
def new_post_view(request):
    return render(request, "pages/new_post.html")

@login_required
def likes_view(request):
    return render(request, "pages/likes.html")

def public_profile_view(request, username):
    user = get_object_or_404(User, username=username)
    profile, _ = Profile.objects.get_or_create(user=user)
    return render(request, "pages/profile.html", {"profile_user": user, "profile": profile, "is_public": True})




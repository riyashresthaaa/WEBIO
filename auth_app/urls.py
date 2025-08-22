from django.urls import path
from . import views

urlpatterns = [
    path("signup/", views.signup_view, name="signup"),
    path("login/", views.login_view, name="login"),
    path("logout/", views.logout_view, name="logout"),

    # Menu pages
    path("", views.index_view, name="index"),            # Home
    path("messages/", views.messages_view, name="messages"),
    path("new/", views.new_post_view, name="new_post"),
    path("likes/", views.likes_view, name="likes"),
    path("profile/", views.profile_view, name="profile"),   # current user's profile

    # (Optional) public profile by username, e.g. /u/jennie/
    path("u/<str:username>/", views.public_profile_view, name="public_profile"),
]

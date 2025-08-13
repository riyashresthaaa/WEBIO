from django.urls import path
from post import views

urlpatterns = [
    path('index', views.index, name='index')
]




from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.home,name="home"),
    path('about', views.about, name="about"),
    path('skills', views.skills, name="skills"),
    path('contact', views.contact, name="contact"),
    path('project', views.project, name="project"),
]
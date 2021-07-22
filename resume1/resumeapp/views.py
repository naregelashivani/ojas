from django.shortcuts import render
from .models import Data
# Create your views here.
def home(request):
    return render(request,'home.html')
def about(request):
    return render(request,'about.html')
def skills(request):
    return render(request,'skills.html')
def contact(request):
    if request.method=="POST":
        Name=request.POST.get("usrname")
        Email=request.POST.get("email id")
        Contact=request.POST.get("number")
        Messages=request.POST.get("comment")
        store=Data(Name=Name,Email=Email,Contact=Contact,Messages=Messages)
        store.save()
    return render(request,'contact.html')
def project(request):
    return render(request,'project.html')

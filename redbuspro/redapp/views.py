from django.shortcuts import render, HttpResponseRedirect
from .forms import RedbusRegistration
from .forms import SignupForm
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from .models import Ticket_User
# Create your views here.

def signup(request):
    if request.method == 'POST':
        fm = SignupForm(request.POST)
        if fm.is_valid():
            messages.success(request,'Account Created Succesfully')
            fm.save()
    else:
        fm = SignupForm()
    return render(request, 'signup.html', {'form': fm})


def user_login(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            fm = AuthenticationForm(request=request,data=request.POST)
            if fm.is_valid():
                uname = fm.cleaned_data['username']
                upass = fm.cleaned_data['password']
                user = authenticate(username=uname,password=upass)
                if user is not None:
                    login(request,user)
                    messages.success(request,'Logged in Succesfully !!!')
                    return HttpResponseRedirect('/add')
        else:
            fm = AuthenticationForm()
        return render(request, 'signup.html', {'form': fm})
    else:
        return HttpResponseRedirect('/add')


def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/login')


def add_show(request):
    if request.method == 'POST':
        fm = RedbusRegistration(request.POST)
        if fm.is_valid():
            nm = fm.cleaned_data['name']
            em = fm.cleaned_data['email']
            pw = fm.cleaned_data['password']
            cn = fm.cleaned_data['contact']
            sp = fm.cleaned_data['startingpoint']
            ep = fm.cleaned_data['endingpoint']
            d = fm.cleaned_data['date']
            reg = Ticket_User(name=nm, email=em, password=pw,contact=cn,startingpoint=sp,endingpoint=ep,date=d)
            reg.save()
            fm = RedbusRegistration()
    else:
        fm = RedbusRegistration()
    stud = Ticket_User.objects.all()
    return render(request, 'add.html', {'form':fm, 'stu':stud})


#edit and update function
def update_data(request,id):
    if request.method == 'POST':
        pi = Ticket_User.objects.get(pk=id)
        fm = RedbusRegistration(request.POST, instance=pi)
        if fm.is_valid():
            fm.save()
    else:
        pi = Ticket_User.objects.get(pk=id)
        fm = RedbusRegistration(instance=pi)
    return render(request,'update.html', {'form':fm})
#delete function
def delete_data(request,id):
    if request.method == 'POST':
        pi = Ticket_User.objects.get(pk=id)
        pi.delete()
        return HttpResponseRedirect('/')


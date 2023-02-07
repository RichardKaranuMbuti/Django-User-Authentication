from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login
from .forms import LoginForm,SignUpForm


def login_view(request):
    if request.method=='POST':
        form=LoginForm(data=request.POST)
        if form.is_valid():
            username=form.cleaned_data.get('username')
            password=form.cleaned_data.get('password')
            user=authenticate(username=username,password=password)
            if user is not None:
                login(request,user)
                return redirect('home')
    else:
        form=LoginForm()
    return render(request, 'users/login.html',{'form':form})

def signup_view(request):
    if request.method=='POST':
        form=SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username=form.cleaned_data.get('username')
            raw_password=form.cleaned_data.get('password1')
            user=authenticate(username=username,password=raw_password)
            login(request,user)
            return redirect('login')
    else:
        form=SignUpForm()
    return render(request, 'users/signup.html',{'form':form})

def home_view(request):
    return render(request, 'users/home.html')


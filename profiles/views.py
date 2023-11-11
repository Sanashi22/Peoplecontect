from django.shortcuts import render, redirect
from .forms import LoginForm,Signupform, UserUpdateForm
from django.contrib.auth import authenticate, login, logout
from .models import Profile
from django.contrib.auth.decorators import login_required
from post.models import Post
from django.views.generic import DetailView
# Create your views here.

def user_login(request):
    forms=LoginForm()
    if request.method=="POST":
        form=LoginForm(request.POST)
        if form.is_valid():
            username=form.cleaned_data["username"]  
            password=form.cleaned_data["password"]
            user=authenticate(request, username=username, password=password)
            if user: 
                login(request, user)
                return redirect("/")

    context= {"form": forms }
    return render(request,"login.html", context)

def signup(request):
    forms=Signupform()
    if request.method=="POST":
        form=Signupform(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/profiles/login")

    context= {"form": forms }
    return render(request,"signup.html",context)

@login_required(login_url='/profiles/login')

def update_profile(request):
    profile= Profile.objects.get(user= request.user) 
    forms=UserUpdateForm(instance=profile) 
    if request.method=="POST":
        form=UserUpdateForm(request.POST, request.FILES, instance=profile)
        # print(form.is_valid())
        if form.is_valid():
            instance=form.save(commit=False) #commit=False means don't save form now 
            instance.user=request.user
            instance.save()
            return redirect ("/")
    context= {"form": forms}
    return render(request,"updateprofile.html", context)

@login_required(login_url='/profiles/login')
def get_profile(request):
    profile= Profile.objects.get(user=request.user)
    posts= Post.objects.filter(author=request.user)
    post_count= posts.count()
    context={"profile": profile, "posts": posts,"post_count":post_count}
    return render(request,"profile.html", context)
    
@login_required(login_url='/profiles/login')
def user_logout(request):
    logout(request)
    return redirect("/profiles/login")


class ProfileDetailView(DetailView):
    model= Profile
    pk_url_kwarg = 'pk'
    template_name= 'profile.html'
    

def get_all_user(request):
    profiles= Profile.objects.exclude(user=request.user)
    context= {'profiles': profiles}
    return render(request, 'people-list.html', context)


from django.shortcuts import render, redirect
from .forms import PostForm
from .models import Post

# Create your views here.

def homepage(request):
    form= PostForm()
    if request.method=="POST":
        form= PostForm(request.POST, request.FILES)
        if form.is_valid():
            instance= form.save(commit=False)
            instance.author=request.user
            instance.save()
            return redirect('/')
    post= Post.objects.all()
    context={'form': form, 'posts': post}
    return render(request,'homepage.html', context)


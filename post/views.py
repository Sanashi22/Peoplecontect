from django.shortcuts import render, redirect
from .forms import PostForm, CommentForm
from .models import Post
from django.contrib.auth.decorators import login_required
# Create your views here.

def homepage(request):
    form= PostForm()
    c_form= CommentForm()
    print(request.POST)

    if "post_button" in request.POST:
        form= PostForm(request.POST, request.FILES)
        if form.is_valid():
            instance= form.save(commit=False)
            instance.author=request.user
            instance.save()
            return redirect('/')
    if "comment_button" in request.POST:
        form=CommentForm(request.POST)
        post=Post.objects.get(id=request.POST.get('post_id'))
        if form.is_valid():
            instance=form.save(commit=False)
            instance.user=request.user
            instance.post=post
            instance.save()
            return redirect('/')
        


    post= Post.objects.all()
    context={'form': form, 'posts': post, 'c_form': c_form}
    return render(request,'homepage.html', context)

@login_required(login_url='/profile/login')
def delete_post(request, post_id):
    post= Post.objects.get(id=post_id)
    post.delete()
    return redirect('/')

@login_required(login_url='/profile/login')
def update_post(request, post_id):
    
    post=Post.objects.get(id=post_id)
    form=PostForm(instance=post)
    if request.method=="POST":
        form=PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            instance=form.save(commit=False)
            instance.author=request.user
            instance.save()
            return redirect("/")
    context={
        "form": form
    }
    return render(request, 'update-post.html', context)



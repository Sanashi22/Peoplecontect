from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Post (models.Model):
    content=models.CharField(max_length=400)
    image=models.ImageField(upload_to="posts", blank=True, null=True)
    author=models.ForeignKey(User,on_delete= models.CASCADE)  #one to many and if user delete will delete profile post will delete
    created=models.DateTimeField(auto_now_add=True) # date is fixed
    updated=models.DateTimeField(auto_now=True) # date will be updated


    def __str__(self):
        return f"{self.author.username} created post at {self.updated}"
    
    def get_all_comments(self):
        return self.comment_set.all()
    
    class Meta: 
        ordering=["-updated"] # current updated post will be on top

class Comment(models.Model):
    comment= models.CharField(max_length=200)
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    post=models.ForeignKey(Post, on_delete=models.CASCADE)
    created=models.DateTimeField(auto_now_add=True) # date is fixed ex: created 
    updated=models.DateTimeField(auto_now=True) # for date updated

    def __str__(self):
        return f"{self.user.username} commented post at {self.updated}"
    
    class Meta: 
        ordering=["-updated"]

    

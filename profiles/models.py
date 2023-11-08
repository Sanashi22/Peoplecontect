from django.db import models
from django.contrib.auth.models import User
from django.core.validators import FileExtensionValidator
# Create your models here.

STATUS_CHOICE= (
    ('send','send'), # 1st send will be database, 2nd sent will be on user
    ('accepted','accepted')

)

class Profile(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE)  # one user has one profile
    address=models.CharField(max_length=200)
    bio=models.TextField(blank=True) # blank means bio is not manadatory
    profile_pic=models.ImageField(upload_to="profile", validators=[FileExtensionValidator(['png','jpg','jpeg'])])
    friends=models.ManyToManyField(User, blank=True, related_name="friends")
    
    def __str__(self):
        return f"{self.user.username} profile has been created"
    
class Relationship(models.Model):
    sender=models.ForeignKey(Profile, on_delete=models.CASCADE, related_name="sender") 
    receiver=models.ForeignKey(Profile, on_delete=models.CASCADE, related_name="receiver")
    status=models.CharField(max_length=8, choices=STATUS_CHOICE)
    
    
    def __str__(self):
        return f"{self.sender.user.username} has sent request to {self.receiver.user.username}"
    
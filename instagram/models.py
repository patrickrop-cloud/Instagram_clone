from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    profile_pic = models.ImageField(default='default.jpg',upload_to='profile')
    bio = models.TextField(max_length=300)
    user = models.OneToOneField(User,null=True,on_delete=models.CASCADE)
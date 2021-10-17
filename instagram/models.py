from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    profile_pic = models.ImageField(default='default.jpg',upload_to='profile')
    bio = models.TextField(max_length=300)
    user = models.OneToOneField(User,null=True,on_delete=models.CASCADE)

    def __str__(self):
        return self.bio

    def save_profile(self):
        self.save()

    def delete_profile(self):
        self.delete()

    @classmethod
    def update_profile(self):
        profile=Profile.objects.get_or_create()
        return profile

class Image(models.Model):
    image = models.ImageField(blank=True,null=False)
    name = models.CharField(max_length=60)
    caption = models.TextField(max_length=255)
    liked = models.ManyToManyField(User, default=0,blank=True,related_name='liked')
    comments = models.TextField(max_length=80)
    profile = models.ForeignKey(Profile,on_delete=models.CASCADE,null=True)
    author = models.ForeignKey(User,on_delete=models.CASCADE,related_name='author',null=True)
    

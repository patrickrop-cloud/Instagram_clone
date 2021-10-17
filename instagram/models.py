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


    def __str__(self):
        return self.name

    def save_image(self):
        self.save()

    def delete_image(self):
        self.delete()

    @classmethod
    def update_caption(self):
        caption = Image.objects.get_or_create()
        return caption
    @property
    def num_likes(self):
        return self.likes.all().count()

    LIKE_CHOICES = (
        ('Like','Like'),
        ('Unlike','Unlike')
    )

class Like(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    Image = models.ForeignKey(Image, on_delete=models.CASCADE)
    value = models.CharField(choices=LIKE_CHOICES,default='Like',max_length=10)

    def __str__(self):
        return self.image


class Following(models.Model):
    user=models.OneToOneField(User,null=True,on_delete=models.CASCADE)
    followed=models.OneToOneField(User,null=True,related_name='followed',on_delete=models.CASCADE)

    @classmethod
    def follow(cls,user,another_account):
        obj=Following.objects.all()
        obj.create=cls.objects.get_or_create(user=user)
        obj.followed.add(another_account)
        print('follow')

    @classmethod
    def unfollowed(cls,user,another_account):
        obj=Following.objects.all()
        obj.create=cls.objects.get_or_create(user=user)
        obj.followed.remove(another_account)
        print('unfollowed')

class Comment(models.Model):
    post = models.ForeignKey(Image,on_delete=models.CASCADE,related_name='comment')
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=False)

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return 'Comment {} by {}'.format(self.body, self.name)










from django.db import models
from django.contrib.auth.models import User
from userwork.models import Profile
from django.urls import reverse


# Create your models here.
class Post(models.Model):
    post_id = models.AutoField(primary_key=True,default=None)
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete= models.CASCADE,related_name='blog_posts')
    updated_on = models.DateTimeField(auto_now= True)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    thumbnail = models.ImageField(upload_to = 'profile_picture/')

    profile = models.ForeignKey(Profile, on_delete=models.CASCADE,default=None,null=True)

    
    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title 

    
    def get_absolute_url(self):
        return reverse("blog" )
    
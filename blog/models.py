from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from taggit.managers import TaggableManager

    
# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=200)
    
    def __str__(self) :
        return self.name
    
class Post(models.Model):
    image = models.ImageField(upload_to ='blog/',default='blog/default.jpg')
    author = models.ForeignKey(User, on_delete= models.SET_NULL, null= True)
    title = models.CharField(max_length=215)
    category = models.ManyToManyField(Category)
    content = models.TextField()
    counted_view = models.IntegerField(default=0)
    status = models.BooleanField(default=False)
    published_date = models.TimeField(blank=True,null= True)
    created_date = models.DateTimeField(auto_now_add= True)
    updated_date = models.DateTimeField(auto_now= True)
    tags = TaggableManager()
    class Meta:
        ordering = ["-created_date"]
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse("blog:single", kwargs={"pid": self.id})
    
class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE,related_name='comments')
    name = models.CharField(max_length=80)
    email = models.EmailField()
    subject = models.CharField(max_length=250)
    body = models.TextField()
    approach = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=True)
    published_date = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.name
    
# python manage.py schemamigration common drop_Comment --auto
#  - Deleted model 'common.cat'
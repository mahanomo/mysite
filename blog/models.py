from django.db import models
from django.contrib.auth.models import User
    
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
    published_date = models.TimeField(null= True)
    created_date = models.TimeField(auto_now_add= True)
    updated_date = models.TimeField(auto_now= True)
    class Meta:
        ordering = ["-created_date"]
    def __str__(self):
        return self.title
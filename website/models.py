from django.contrib.sites.models import Site
from django.contrib.sites.managers import CurrentSiteManager
from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=250,blank=True)
    message = models.TextField()
    created_date = models.TimeField(auto_now_add=True)
    updated_date = models.TimeField(auto_now=True)
    
    class Meta:
        ordering = ["-created_date"]
    def __str__(self):
        return self.name
    

class Newsletter(models.Model):
    email= models.EmailField()

    def __str__(self):
        return self.email
from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=250)
    message = models.TextField()
    created_date = models.TimeField(auto_now_add=True)
    updated_date = models.TimeField(auto_now=True)
    class Meta:
        ordering = ["-created_date"]
    def __str__(self):
        return self.name
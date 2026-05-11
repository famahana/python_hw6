from django.db import models

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=200,blank=False)
    created_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return f'{self.title}'
    

class Contacts(models.Model):
    firstName = models.CharField(max_length=50)
    lastName = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    phoneNumber = models.CharField(max_length=20)
    text = models.TextField(max_length=500)

    



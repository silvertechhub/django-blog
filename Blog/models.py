from django.conf import settings
from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

# User =  get_user_model()   
# class Author(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     profile_picture = models.ImageField

#     def __str__(self):
#         return self.user.username

class Category(models.Model):
    name = models.CharField(max_length=50)
    date_added = models.DateTimeField(auto_now_add=True)
   
    
    def __str__(self): 
        return f"${self.name}"
    class Meta: 
      verbose_name_plural = 'Categories'
   

class Blog(models.Model):
     topic = models.ManyToManyField(Category)
     title = models.CharField(max_length=200)
     article = models.TextField(max_length=2000)
     author = models.ForeignKey(User, related_name='writer_name', on_delete=models.CASCADE)
     image = models.ImageField(upload_to='images/')
     date_added = models.DateTimeField(auto_now_add=True)
     def get_absolute_url(self):
        return reverse("single_blog", kwargs={"pk": self.pk})
     
     def __str__(self):
         return self.title[:50] + "..."
    

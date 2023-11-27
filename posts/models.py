from django.db import models

# Create your models here.

#database name
class Post(models.Model):
    text = models.TextField()
    def __str__(self):
        return self.text[:50]
    #databse field
class PostForm(models.Model):
    text = models.TextField()
    email = models.EmailField()
    def __str__(self):
        return self.text[:50]

from django.db import models

# Create your models here.
class Post(models.Model):
    title=models.CharField(max_length=64)
    title=models.DateField(auto_now_add=True)

    content=models.TextField()


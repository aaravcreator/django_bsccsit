from django.db import models
from django.contrib.auth import get_user_model
from django.utils import timezone
User = get_user_model()
# Create your models here.
class BlogPost(models.Model):
    title = models.CharField(max_length=255)
    slug = models.CharField(max_length=255,unique=True)
    body  = models.TextField()
    date = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)




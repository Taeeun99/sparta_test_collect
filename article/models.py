from tabnanny import verbose
from django.db import models
from django.contrib.auth import get_user_model
# Create your models here.
class Article(models.Model):
    author = models.ForeignKey(get_user_model())
    title = models.CharField(max_length=30)
    content = models.CharField(max_length=30)
from django.db import models
from datetime import datetime
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User
# from froala_editor.fields import FroalaField

# Create your models here.

class BlogModel(models.Model):
    title = models.TextField(max_length=255)
    content = models.TextField(max_length=2000)
    image = models.ImageField(upload_to='media/slider/%Y/%m', blank=True)
    created_date = models.DateTimeField(default = datetime.now, blank=True)
    # user = User.username

class NightFood(models.Model):
    image = models.ImageField(upload_to='media/slider/%Y/%m', blank=True)
    title = models.TextField(max_length=255)
    price = models.TextField(max_length=255)

class Grocery(models.Model):
    image = models.ImageField(upload_to='media/slider/%Y/%m', blank=True)
    title = models.TextField(max_length=255)
    price = models.TextField(max_length=255)

class Donate(models.Model):
    food_type = models.TextField(max_length=255)
    address = models.TextField(max_length=255)

class RewardPoints(models.Model):
    points = models.IntegerField(blank=True)

from django.db import models

# Create your models here.
class Movie(models.Model):
    objects = models.Manager()
    title = models.CharField(max_length=100)
    overview = models.TextField()
    poster_path = models.CharField(max_length=500)
from django.db import models
from django.contrib.auth.models import AbstractUser


def __str__(self):
    return f"{self.first_name} {self.last_name}"


class Artist(models.Model):
    name = models.CharField(max_length=100)
    bio = models.TextField()

    def __str__(self):
        return self.name


class tag(models.Model):
    caption = models.CharField(max_length=15)

    def __str__(self):
        return self.caption


class Vinyl(models.Model):
    title = models.CharField(max_length=100)
    genre = models.CharField(max_length=100)
    year = models.IntegerField()
    price = models.DecimalField(max_digits=5, decimal_places=2)
    stock = models.IntegerField()
    slug = models.SlugField(unique=True, db_index=True)
    artist = models.ForeignKey(Artist, on_delete=models.SET_NULL, null=True, related_name='vinyls')
    tags = models.ManyToManyField(tag)
    image = models.ImageField(upload_to="images", null=True)
    dominantcolor = models.CharField(max_length=7, null=True)

    def __str__(self):
        return self.title

from django.db import models

# Create your models here.


class Artist(models.Model):
    name = models.CharField(max_length=100)
    bio = models.TextField()
    #image = models.ImageField(upload_to='images/', default='images/default.jpg')

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
    slug= models.SlugField(unique=True,db_index=True)
    artist = models.ForeignKey(Artist, on_delete=models.SET_NULL,null=True, related_name='vinyls') #the null=True is used for the author field to be optional, null is not true by default
    tags= models.ManyToManyField(tag)
    image = models.ImageField(upload_to="images", null=True)

    def __str__(self):
        return self.title
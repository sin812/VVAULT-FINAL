from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator

def __str__(self):
    return f"{self.first_name} {self.last_name}"

class Customer(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField()


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
    title = models.CharField(max_length=50, help_text='Enter the title of the vinyl')
    genre = models.CharField(max_length=50, help_text='Enter the genre of the vinyl')
    year = models.IntegerField(
        validators=[
            MinValueValidator(1900),
            MaxValueValidator(2100)
        ],
        help_text='Enter the release year of the vinyl'
    )
    price = models.DecimalField(
        max_digits=6,
        decimal_places=2,
        validators=[
            MinValueValidator(0.01)
        ],
        help_text='Enter the price of the vinyl'
    )
    stock = models.PositiveIntegerField(help_text='Enter the stock quantity of the vinyl')
    slug = models.SlugField(unique=True, db_index=True, help_text='Unique slug for the vinyl URL')
    artist = models.ForeignKey(
        Artist,
        on_delete=models.SET_NULL,
        null=True,
        related_name='vinyls',
        help_text='Select the artist of the vinyl'
    )
    tags = models.ManyToManyField(tag, help_text='Select tags for the vinyl')
    image = models.ImageField(upload_to="images", null=True, help_text='Upload image of the vinyl')
    dominantcolor = models.CharField(max_length=7, null=True, help_text='Dominant color of the vinyl')

    def __str__(self):
        return self.title
    
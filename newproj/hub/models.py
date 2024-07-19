from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator

class Artist(models.Model):
    name = models.CharField(max_length=50, help_text='Enter the artist name')
    bio = models.TextField(help_text='Enter the biography of the artist')

    def __str__(self):
        return self.name

class tag(models.Model):
    caption = models.CharField(max_length=20, help_text='Enter tag caption')

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
    rating = models.FloatField(default=0)  # New field for rating

    def __str__(self):
        return self.title

class Cart(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"Cart for {self.user.username}"

class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    vinyl = models.ForeignKey(Vinyl, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.quantity} x {self.vinyl.title}"

class Rating(models.Model):
    vinyl = models.ForeignKey(Vinyl, on_delete=models.CASCADE, related_name='ratings')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    score = models.IntegerField(
        validators=[
            MinValueValidator(1),
            MaxValueValidator(10)
        ],
        help_text='Rate the vinyl from 1 to 10'
    )

    def __str__(self):
        return f"Rating of {self.score} for {self.vinyl.title} by {self.user.username}"

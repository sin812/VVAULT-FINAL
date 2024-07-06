from django.db import models
from django.contrib.auth.models import AbstractUser, Group as AuthGroup, Permission as AuthPermission
from django.core.validators import RegexValidator

class CustomUser(AbstractUser):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phonenumber = models.CharField(max_length=10, validators=[RegexValidator(r'^[0-9]{10}$', message='Phone number must be 10 digits.')])
    groups = models.ManyToManyField(
        AuthGroup,
        related_name='auth_users',  # Unique related_name for auth.User groups
        blank=True,
        verbose_name='groups',
        help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.',
    )
    user_permissions = models.ManyToManyField(
        AuthPermission,
        related_name='auth_users',  # Unique related_name for auth.User user_permissions
        blank=True,
        verbose_name='user permissions',
        help_text='Specific permissions for this user.',
    )

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

from django import forms
from .models import Vinyl, Artist
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import Group
from .models import CustomUser




class VinylForm(forms.ModelForm):
    class Meta:
        model = Vinyl
        fields = ['title', 'genre', 'year', 'price', 'stock', 'slug', 'artist', 'tags', 'image', 'dominantcolor']
        widgets = {'dominantcolor': forms.TextInput(attrs={'type': 'color'}),}


class ArtistForm(forms.ModelForm):
    class Meta:
        model = Artist
        fields = ['name', 'bio']  
        

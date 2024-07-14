from django import forms
from .models import Vinyl, Artist, tag
from django.contrib.auth.models import User

class ContactForm(forms.Form):
    name = forms.CharField(max_length=100, label='Name')
    email = forms.EmailField(label='Email')
    message = forms.CharField(widget=forms.Textarea, label='Message')

class VinylForm(forms.ModelForm):
    class Meta:
        model = Vinyl
        fields = ['title', 'genre', 'year', 'price', 'stock', 'slug', 'artist', 'tags', 'image', 'dominantcolor']
        widgets = {
            'dominantcolor': forms.TextInput(attrs={'type': 'color'}),
        }

class ArtistForm(forms.ModelForm):
    class Meta:
        model = Artist
        fields = ['name', 'bio']

class TagForm(forms.ModelForm):
    class Meta:
        model = tag
        fields = ['caption']

class UpdateUsernameForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username']
        labels = {
            'username': 'New Username'
        }

class EditVinylForm(VinylForm):
    class Meta(VinylForm.Meta):
        # Suppose you don't want to allow editing the 'slug' field
        fields = ['title', 'genre', 'year', 'price', 'stock', 'artist', 'tags', 'image', 'dominantcolor']

class EditUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']
        labels = {
            'username': 'Username',
            'first_name': 'First Name',
            'last_name': 'Last Name',
            'email': 'Email'
        }




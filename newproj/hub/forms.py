from django import forms
from .models import Vinyl, Artist, tag
from django.contrib.auth.models import User

# Form for contact page
class ContactForm(forms.Form):
    name = forms.CharField(max_length=100, label='Name')  # Field for the user's name
    email = forms.EmailField(label='Email')  # Field for the user's email
    message = forms.CharField(widget=forms.Textarea, label='Message')  # Field for the user's message

# Model form for adding/editing Vinyl
class VinylForm(forms.ModelForm):
    class Meta:
        model = Vinyl
        fields = ['title', 'genre', 'year', 'price', 'stock', 'slug', 'artist', 'tags', 'image', 'dominantcolor']  # Fields to be included in the form
        widgets = {
            'dominantcolor': forms.TextInput(attrs={'type': 'color'}),  # Widget for color input
        }

# Model form for adding/editing Artist
class ArtistForm(forms.ModelForm):
    class Meta:
        model = Artist
        fields = ['name', 'bio']  # Fields to be included in the form

# Model form for adding/editing Tag
class TagForm(forms.ModelForm):
    class Meta:
        model = tag
        fields = ['caption']  # Fields to be included in the form

# Form for updating the username
class UpdateUsernameForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username']  # Field to be included in the form
        labels = {
            'username': 'New Username'  # Custom label for the username field
        }

# Form for editing Vinyl excluding the 'slug' field
class EditVinylForm(VinylForm):
    class Meta(VinylForm.Meta):
        fields = ['title', 'genre', 'year', 'price', 'stock', 'artist', 'tags', 'image', 'dominantcolor']  # Fields to be included in the form

# Form for editing User details
class EditUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']  # Fields to be included in the form
        labels = {
            'username': 'Username',  # Custom label for the username field
            'first_name': 'First Name',  # Custom label for the first name field
            'last_name': 'Last Name',  # Custom label for the last name field
            'email': 'Email'  # Custom label for the email field
        }

# Form for rating a Vinyl
class RateVinylForm(forms.ModelForm):
    rating = forms.IntegerField(min_value=1, max_value=10)  # Field for rating with a range from 1 to 10

    class Meta:
        model = Vinyl
        fields = ['rating']  # Field to be included in the form

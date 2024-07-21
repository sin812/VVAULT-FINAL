import re
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.core.validators import EmailValidator

# Custom validators
def validate_no_special_characters(value):
    """Validator to ensure no special characters are in the input."""
    if re.search(r'[^a-zA-Z0-9]', value):
        raise ValidationError('Special characters are not allowed.')

def validate_no_numbers(value):
    """Validator to ensure no numbers are in the input."""
    if re.search(r'\d', value):
        raise ValidationError('Numbers are not allowed.')

class RegisterForm(UserCreationForm):
    username = forms.CharField(
        required=True,
        label="Username",
        help_text="Username",
        validators=[validate_no_special_characters],  # Validate no special characters
    )
    first_name = forms.CharField(
        required=True,
        label="First name",
        help_text="First name",
        validators=[validate_no_special_characters, validate_no_numbers],  # Validate no special characters and no numbers
    )
    last_name = forms.CharField(
        required=True,
        label="Last name",
        help_text="Last name",
        validators=[validate_no_special_characters, validate_no_numbers],  # Validate no special characters and no numbers
    )
    email = forms.EmailField(
        required=True,
        label="Email",
        help_text="Email address",
        validators=[EmailValidator()],  # Validate email format
    )
    password1 = forms.CharField(
        label="Password",
        widget=forms.PasswordInput,
        help_text=(
            "Your password must contain at least 8 characters, can't be entirely numeric, "
            "and can't be too similar to your other personal information."
        ),  # Help text for password requirements
    )
    password2 = forms.CharField(
        label="Password confirmation",
        widget=forms.PasswordInput,
        help_text="Enter the same password as before, for verification.",  # Help text for password confirmation
    )

    class Meta:
        model = User
        fields = ["username", "first_name", "last_name", "email", "password1", "password2"]  # Fields to include in the form

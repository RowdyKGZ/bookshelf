from django.contrib.auth.forms import UserCreationForm

from account.models import MyUser


class UserRegistrationForm(UserCreationForm):
    """Form for register user"""
    class Meta:
        model = MyUser
        fields = ('email', 'password1', 'password2')

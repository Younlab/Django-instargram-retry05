from django.contrib.auth import get_user_model, authenticate, login
from django import forms

User = get_user_model()

class SignInForm(forms.ModelForm):
    username = forms.CharField(
        max_length=50,
        widget=forms.TextInput(
            attrs={
                'class':'uk-input',
                'placehorder':'Username'
            }
        )
    )
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                'class':'uk-input'
            }
        )
    )
    class Meta:
        model = User
        fields = ['username', 'password']

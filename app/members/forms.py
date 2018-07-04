from django.contrib.auth import get_user_model, authenticate, login
from django import forms

User = get_user_model()

class SignInForm(forms.ModelForm):
    username = forms.CharField(max_length=50)
    password = forms.CharField(
        widget=forms.PasswordInput()
    )
    class Meta:
        model = User
        fields = ['username', 'password']

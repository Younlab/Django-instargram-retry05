from django.contrib.auth import get_user_model, authenticate, login
from django import forms
from django.core.exceptions import ValidationError

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

class SignUpForm(forms.ModelForm):
    password2 = forms.CharField(
        widget=forms.PasswordInput(),
    )

    class Meta:
        model = User
        fields = ['username', 'password', 'password2', 'email', 'site', 'gender', 'profile_image']
        widgets = {
            'password': forms.PasswordInput(),
        }

    def clean(self):
        super().clean()
        password = self.cleaned_data['password']
        password2 = self.cleaned_data['password2']

        if password != password2:
            self.add_error('password2','패스워드가 일치하지 않습니다.')
        else:
            return self.cleaned_data

    def clean_username(self):
        username = self.cleaned_data['username']
        if User.objects.filter(username=username).exists():
            raise ValidationError('중복된 ID 입니다.')
        else:
            return username


    def created_user(self):
        username = self.cleaned_data['username']
        password = self.cleaned_data['password']
        email = self.cleaned_data['email']
        site = self.cleaned_data['site']
        gender = self.cleaned_data['gender']
        profile_image = self.cleaned_data['profile_image']

        user = User.objects.create_user(
            username = username,
            password = password,
            email = email,
            site = site,
            gender = gender,
            profile_image = profile_image,
        )
        return user
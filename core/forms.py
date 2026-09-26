from django import forms
from django.contrib.auth import get_user_model
from django.core.validators import RegexValidator


class LoginForm(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={'class': 'form-control', 'placeholder': 'Enter your full name'}
        )
    )
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={'class': 'form-control', 'placeholder': 'Enter your password'}
        )
    )


User=get_user_model()

class RegisterForm(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={'class': 'form-control', 'placeholder': 'Enter your user name'}
        )
    )
    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={'class': 'form-control', 'placeholder': 'Enter your Email address'}
        )
    )
    password = forms.CharField(
        validators=[RegexValidator(regex=r'^(?=.*[A-Z])(?=.*[a-z])(?=.*[!@#$%^&*]).{8,}$',
                                   message='Your password must be at least 8 characters long and contain at least one uppercase letter, one lowercase letter, and one special character.')],
        widget=forms.PasswordInput(
            attrs={'class': 'form-control', 'placeholder': 'Enter your password'}
        )

    )
    password2 = forms.CharField(
        label='confirm Password',
        widget=forms.PasswordInput(
            attrs={'class': 'form-control', 'placeholder': 'confirm your password'}
        )
    )

    def clean_username(self):
        username = self.cleaned_data.get('username')
        query_user = User.objects.filter(username=username)
        if query_user.exists():
            raise forms.ValidationError("this Username has used")
        return username

    def clean_email(self):
        email = self.cleaned_data['email']
        if not "gmail.com" in email:
            raise forms.ValidationError("Email has not gmail")

        return email

    def clean_password2(self):
        password = self.cleaned_data.get('password')
        password2 = self.cleaned_data.get('password2')
        if password != password2:
            raise forms.ValidationError("Passwords don't match")
        return self.cleaned_data

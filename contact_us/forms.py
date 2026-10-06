from django import forms


class ContactForm(forms.Form):
    fullname = forms.CharField(
        label='نام کامل شما',
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'لطفا نام کامل خود را وارد کنید', 'maxlength': '20'}),
    )
    email = forms.EmailField(
        label='ایمیل شما',
        widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'لطفا ایمیل خود را وارد کنید'}),
    )
    message = forms.CharField(
        label='پیام شما',
        widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'لطفا پیام خود را وارد کنید'}),
    )

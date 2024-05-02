from django import forms
from django.contrib.auth.password_validation import validate_password
from .models import User

class LoginForm(forms.Form):
    username = forms.CharField(max_length=30)
    password = forms.CharField(widget=forms.PasswordInput)

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if len(username) < 4:
            raise forms.ValidationError('طول نام کاربری بالای ۴ کاراکتر باشد')
        elif len(username) > 30:
            raise forms.ValidationError('طول نام کاربری کمتر از ۳۰ کاراکتر باشد')

        return username


class SignUpForm(forms.Form):
    username = forms.CharField(max_length=30)
    password = forms.CharField(widget=forms.PasswordInput)

    def clean_username(self):
        username = self.cleaned_data.get('username')
        user = User.objects.filter(username=username).exists()
        if user:
            raise forms.ValidationError('نام کاربری با این اسم ثبت شده است.')
        if len(username) < 4:
            raise forms.ValidationError('طول نام کاربری بالای ۴ کاراکتر باشد')
        elif len(username) > 30:
            raise forms.ValidationError('طول نام کاربری کمتر از ۳۰ کاراکتر باشد')
        return username

    def clean_password(self):
        password = self.cleaned_data.get('password')
        try:
            validate_password(password)
        except forms.ValidationError as e:
            raise forms.ValidationError(e)
        return password
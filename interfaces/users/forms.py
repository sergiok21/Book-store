import requests
from django import forms
from rest_framework import status


class UserLoginForm(forms.Form):
    username = forms.CharField(required=True, widget=forms.TextInput(attrs={
        'class': 'form-control py-4',
        'placeholder': 'Username',
    }))
    password = forms.CharField(required=True, widget=forms.PasswordInput(attrs={
        'class': 'form-control py-4',
        'placeholder': 'Password',
    }))

    def clean(self):
        cleaned_data = super().clean()
        data = {
            'username': cleaned_data.get('username'),
            'password': cleaned_data.get('password')
        }
        req = requests.post('http://127.0.0.1:8000/api/users/login/', data=data)
        if req.status_code == status.HTTP_400_BAD_REQUEST:
            raise forms.ValidationError(req.json().get('error'))

    def add_error(self, field, error):
        errors = self.errors.setdefault(forms.forms.NON_FIELD_ERRORS, forms.utils.ErrorList())
        errors.append(error)


class UserRegistrationForm(forms.Form):
    first_name = forms.CharField(required=True, widget=forms.TextInput(attrs={
        'class': 'form-control py-4',
        'placeholder': 'First name',
    }))
    last_name = forms.CharField(required=True, widget=forms.TextInput(attrs={
        'class': 'form-control py-4',
        'placeholder': 'Last name',
    }))
    username = forms.CharField(required=True, widget=forms.TextInput(attrs={
        'class': 'form-control py-4',
        'placeholder': 'Username',
    }))
    email = forms.CharField(required=True, widget=forms.EmailInput(attrs={
        'class': 'form-control py-4',
        'placeholder': 'E-mail',
    }))
    password = forms.CharField(required=True, widget=forms.PasswordInput(attrs={
        'class': 'form-control py-4',
        'placeholder': 'Password',
    }))
    password2 = forms.CharField(required=True, widget=forms.PasswordInput(attrs={
        'class': 'form-control py-4',
        'placeholder': 'Confirm password',
    }))

    def clean(self):
        cleaned_data = super().clean()
        data = {
            'first_name': cleaned_data.get('first_name'),
            'last_name': cleaned_data.get('last_name'),
            'email': cleaned_data.get('email'),
            'username': cleaned_data.get('username'),
            'password': cleaned_data.get('password'),
        }
        if data['password'] != cleaned_data.get('password2'):
            raise forms.ValidationError('Password mismatch.')
        req = requests.post('http://127.0.0.1:8000/api/users/registration/', data=data)
        if req.status_code == status.HTTP_400_BAD_REQUEST:
            for error in req.json().get('errors').values():
                raise forms.ValidationError(error)

    def add_error(self, field, error):
        errors = self.errors.setdefault(forms.forms.NON_FIELD_ERRORS, forms.utils.ErrorList())
        errors.append(error)

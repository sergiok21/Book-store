from django import forms


class MessageForm(forms.Form):
    name = forms.CharField(required=True, widget=forms.TextInput(attrs={
                'class': 'u-full-width',
                'name': 'name',
                'placeholder': 'Name',
                'minlength': '2',
                'type': 'text',
    }))
    email = forms.EmailField(required=True, widget=forms.TextInput(attrs={
        'class': 'u-full-width',
        'name': 'email',
        'placeholder': 'E-mail',
        'type': 'email',
    }))
    message = forms.CharField(required=True, widget=forms.Textarea(attrs={
        'class': 'u-full-width',
        'name': 'message',
        'placeholder': 'Message',
        'style': 'height: 150px',
    }))


class ProfileForm(forms.Form):
    first_name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'u-full-width',
        'name': 'name',
        'placeholder': 'First Name',
        'minlength': '2',
        'type': 'text',
    }))
    last_name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'u-full-width',
        'name': 'last_name',
        'placeholder': 'Last Name',
        'type': 'text',
    }))
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'u-full-width',
        'name': 'username',
        'placeholder': 'Username',
        'minlength': '2',
        'type': 'text',
        'readonly': True,
        'style': 'background-color: #a4a4a4',
    }))
    email = forms.EmailField(widget=forms.TextInput(attrs={
        'class': 'u-full-width',
        'name': 'email',
        'placeholder': 'E-mail',
        'type': 'email',
    }))

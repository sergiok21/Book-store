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

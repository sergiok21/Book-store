from django import forms

from books.models import Message


class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ['name', 'email', 'message']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'u-full-width',
                'name': 'name',
                'placeholder': 'Name',
                'minlength': '2',
                'type': 'text',
            }),
            'email': forms.TextInput(attrs={
                'class': 'u-full-width',
                'name': 'email',
                'placeholder': 'E-mail',
                'type': 'email',
            }),
            'message': forms.Textarea(attrs={
                'class': 'u-full-width',
                'name': 'message',
                'placeholder': 'Message',
                'style': 'height: 150px',
                # 'type': 'email',
            }),
        }

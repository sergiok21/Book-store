from django import forms


class CheckoutForm(forms.Form):
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
    email = forms.EmailField(widget=forms.TextInput(attrs={
        'class': 'u-full-width',
        'name': 'email',
        'placeholder': 'E-mail',
        'type': 'email',
    }))
    phone = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'u-full-width',
        'name': 'username',
        'placeholder': 'Phone number',
        'minlength': '2',
        'type': 'text',
    }))
    address = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'u-full-width',
        'name': 'username',
        'placeholder': 'Address',
        'minlength': '2',
        'type': 'text',
    }))
    message = forms.CharField(widget=forms.Textarea(attrs={
        'class': 'u-full-width',
        'name': 'message',
        'placeholder': 'Message',
        'style': 'height: 150px',
    }))

from django import forms


class MessageForm(forms.Form):
    message = forms.CharField(max_length=500, label='Your message')


class UserInfoForm(forms.Form):
    """Collect basic user details before starting the chat."""

    name = forms.CharField(max_length=100, label='Name')
    contact = forms.CharField(max_length=20, label='Contact Number')
    email = forms.EmailField(label='Email')
    location = forms.CharField(max_length=100, label='Location')

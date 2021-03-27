from django import forms
from django.core.exceptions import ValidationError

from budapp.helpers import (
    url as url_helper,
    user as user_helper,
)
from budapp.apps.authentication import services as auth_service


class LoginForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        super(LoginForm, self).__init__(*args, **kwargs)

    def clean(self):
        cleaned_data = self.cleaned_data
        auth_service.authenticate_user(
            cleaned_data['email'],
            cleaned_data['password'],
            self.request,
        )
        if not user_helper.is_authenticated(self.request):
            raise forms.ValidationError('Login failed.')

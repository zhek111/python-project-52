from django.contrib.auth.forms import UserCreationForm, UserChangeForm, \
    PasswordChangeForm, SetPasswordForm
from users.models import User


class UserCreateForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username']

from django import forms

from django import forms
from django.contrib.auth.forms import UserChangeForm

class UserUpdateForm(UserChangeForm):
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Подтверждение пароля', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'password']

    def clean_password2(self):
        password = self.cleaned_data.get("password")
        password2 = self.cleaned_data.get("password2")
        if password and password2 and password != password2:
            raise forms.ValidationError("Пароли не совпадают")
        return password2
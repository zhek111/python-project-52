from django.contrib.auth.forms import UserCreationForm, UserChangeForm, \
    PasswordChangeForm, SetPasswordForm
from users.models import User


class UserCreateChangeForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username']


from django import forms
from .models import User
from django.contrib.auth.forms import UserCreationForm


# class UserForm(forms.Form):
#     username = forms.CharField(
#         label="用户名", max_length=16)
#     password = forms.CharField(
#         label="密码", max_length=256, widget=forms.PasswordInput)


class RegisterForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('username', 'email')

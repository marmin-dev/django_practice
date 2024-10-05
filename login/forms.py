from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm

from django.db import models

from login.models import CustomUser


class LoginForm(AuthenticationForm):
    username = forms.CharField(label='ID')

    def clean(self):
        cleaned_data = super().clean()
        username = cleaned_data.get('username')
        password = cleaned_data.get('password')
        user_model = get_user_model()

        try:
            # user = user_model.objects.get(models.Q(nickname=username) | models.Q(email=username))
            user = user_model.objects.get(models.Q(username=username))
            if not user.check_password(password):
                raise forms.ValidationError("Invalid password")

            cleaned_data['user'] = user
        except user_model.DoesNotExist:
            raise forms.ValidationError("User does not exist")

        return cleaned_data


class CustomUserCreationForm(UserCreationForm):
    nickname = forms.CharField(max_length=30, required=True, help_text='Required. 30 characters or fewer.')
    class Meta:
        model = CustomUser
        fields = ('username', 'nickname', 'password1', 'password2')  # 원하는 필드 추가


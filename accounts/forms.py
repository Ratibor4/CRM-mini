from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.forms import AuthenticationForm
from .models import CustomUser

class RegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password1', 'password2']


class LoginForm(AuthenticationForm):
    remember_me = forms.BooleanField(required=False)




class AdminLoginForm(AuthenticationForm):
    def confirm_login_allowed(self, user):
        if not user.is_admin_account:
            raise forms.ValidationError(
                "Доступ разрешен только администратору",
                code='admin_only',
            )
        return super().confirm_login_allowed(user)
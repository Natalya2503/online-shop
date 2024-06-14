from typing import Any
from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm
from django.contrib.auth import get_user_model

class UserLoginForm(AuthenticationForm):

    username = forms.CharField(
        label = 'Имя',
        widget=forms.TextInput(attrs={"autofocus": True,
                                      'class': 'form-control',
                                      'placeholder': 'Введите ваше имя пользователя'})
    )
    password = forms.CharField(
        label = 'Пароль',
        widget=forms.PasswordInput(attrs={"autocomplete": "current-password",
                                          'class': 'form-control',
                                          'placeholder': 'Введите ваш пароль'})
    )

    class Meta:
        model = get_user_model()
        fields = ['username', 'password']

# ------------------------------------------

class UserRegistrationForm(UserCreationForm):

    first_name = forms.CharField(
        label = 'Имя*',
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "Введите ваше имя",
            }
        )
    )
    last_name = forms.CharField(
        label = 'Фамилия*',
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "Введите вашу фамилию",
            }
        )
    )
    username = forms.CharField(
        label = 'Имя пользователя*', 
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "Введите ваше имя пользователя",
            }
        )
    )
    email = forms.CharField(
        label = 'E-mail',
        widget=forms.EmailInput(
            attrs={
                "class": "form-control",
                "placeholder": "Введите ваш email *youremail@example.com",
            }
        )
    )
    password1 = forms.CharField(
        label = 'Пароль*',
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control",
                "placeholder": "Введите ваш пароль",
            }
        )
    )
    password2 = forms.CharField(
        label = 'Подтверждение пароля*',
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control",
                "placeholder": "Поддтвердите ваш пароль",
            }
        )
    )

    class Meta:
        model = get_user_model()
        fields = [
            "first_name",
            "last_name",
            "username",
            "email",
            "password1",
            "password2",
        ]
    
    def clean_password2(self):
        sd = self.cleaned_data
        if sd['password1'] != sd['password2']:
            raise forms.ValidationError('Пароли не совпадают')
        return sd['password2']
        

   
    
# ------------------------------------------
    
class UserProfileForm(forms.ModelForm):

    image = forms.ImageField(
        widget=forms.FileInput(attrs={"class": "form-control mt-3"}), required=False
    )
    first_name = forms.CharField(
        label = 'Имя*',
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "Введите ваше имя",
            }
        )
    )
    last_name = forms.CharField(
        label = 'Фамилия*',
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "Введите вашу фамилию",
            }
        )
    )
    username = forms.CharField(
        disabled=True,
        label = 'Имя пользователя*',
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "Введите ваше имя пользователя",
            }
        )
    )
    email = forms.CharField(
        disabled=True,
        label = 'E-mail',
        widget=forms.EmailInput(
            attrs={
                "class": "form-control",
                "placeholder": "Введите ваш email *youremail@example.com",
                
            }
        ),
    )

    class Meta:
        model = get_user_model()
        fields = [
            "image",
            "first_name",
            "last_name",
            "username",
            "email"]
from django import forms

from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

# from .models import Testimonial
from django.forms import ModelForm

from .models import Testimonial


class NameForm(forms.ModelForm):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    subject = forms.CharField(max_length=100)
    message = forms.TextInput()
    


# class PaymentForm(ModelForm):
#     card_number = forms.IntegerField()
#     month_year = forms.IntegerField()
#     cvv = forms.IntegerField()
#     name = forms.CharField(max_length=25)
#     zip = forms.IntegerField()
#     state = forms.CharField()
#     class Meta:
#         model = PaymentDetails
#         fields = '__all__'




    
class RegisterUserForm(UserCreationForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class': 'form-input'}))
    email = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={'class': 'form-input'}))
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-input'}))
    password2 = forms.CharField(label='Повтор пароля', widget=forms.PasswordInput(attrs={'class': 'form-input'}))

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    def clean_email(self):
        return self.cleaned_data['email'].lower()


class ImageForm(forms.ModelForm):
    """Form for the image model"""
    class Meta:
        model = Testimonial
        fields = ('name', 'text', 'image')

class LoginUserForm(AuthenticationForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class': 'form-input'}))
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-input'}))







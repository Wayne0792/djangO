
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django import forms
from django.forms.widgets import PasswordInput, TextInput
from .models import Record

#Create Form View
class CreateUserForm(UserCreationForm):
    class Meta:

        model = User
        fields = ['username', 'password1', 'password2']

#Login View
class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=TextInput())
    password = forms.CharField(widget=PasswordInput())


#Create Record View
class CreateRecordForm(forms.ModelForm):
    class Meta:

        model = Record
        fields = ['first_name', 'last_name', 'email','phone', 'address', 'city', 'province', 'country']


#Update Record View
class UpdateRecordForm(forms.ModelForm):
    class Meta:

        model = Record
        fields = ['first_name', 'last_name', 'email','phone', 'address', 'city', 'province', 'country']

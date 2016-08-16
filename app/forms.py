from django import forms 
from models import Category, Item, CustomUser 

# crispy import:

from crispy_forms.helper import FormHelper 
from crispy_forms.layout import Submit 
from crispy_forms.layout import Layout, Submit, HTML, Div, Field 
from crispy_forms.bootstrap import FormActions
from django import forms 
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

class UserSignUp(forms.Form):
  email = forms.EmailField(required=True)
  password = forms.CharField(widget=forms.PasswordInput(), required=True)

class UserLogin(forms.Form):  
  username = forms.CharField(required=True)
  password = forms.CharField(required=True, widget=forms.PasswordInput())

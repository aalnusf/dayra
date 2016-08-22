from django import forms 
from django.contrib.auth.forms import UserCreationForm, UserChangeForm 
from app.models import Category, Item, CustomeUserManager, CustomUser
from django import forms


# crispy import:

from crispy_forms.helper import FormHelper 
from crispy_forms.layout import Layout, Submit, HTML, Div, Field 
from crispy_forms.bootstrap import FormActions

# from django.contrib.auth.forms import UserCreationForm, UserChangeForm

# class UserSignUp(forms.Form):
#   email = forms.EmailField(required=True)
#   password = forms.CharField(widget=forms.PasswordInput(), required=True)

# class UserLogin(forms.Form):  
#   email = forms.EmailField(required=True)
#   password = forms.CharField(required=True, widget=forms.PasswordInput())

class CustomUserCreationForm(forms.ModelForm):
    # def __init__(self, *args, **kargs):
    #     super(CustomUserCreationForm, self).__init__(*args, **kargs)
    # email = forms.CharField(max_length=255, required=True)
    # password = forms.CharField(widget=forms.PasswordInput(), required=True)


    class Meta:
        model = CustomUser
        fields = ('email', 'password')

    def __init__(self, *args, **kwargs):
        super(CustomUserCreationForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.form_action ='/signup/'
        #self.helper.add_input(Submit('submit', 'Search'))
        self.helper.layout = Layout(
                        
                        Div('email', css_class='col-sm-5', style= 'margin-top: 200px'),
                        Div('password', css_class='col-sm-5', style= 'margin-top: 200px'),
                        Div(FormActions(Submit('submit','signup'),
                            css_class= 'col-sm-2',
                            style= 'margin-top: 200px'))
                
                    )

class CustomUserChangeForm(UserChangeForm):
    def __init__(self, *args, **kargs):
        super(CustomUserChangeForm, self).__init__(*args, **kargs)
        

    class Meta:
        model = CustomUser 
        fields = '__all__'



class CustomUserLoginForm(forms.Form):
    email = forms.CharField(required=True)
    password = forms.CharField(required=True, widget=forms.PasswordInput())

    
    def __init__(self, *args, **kwargs):
        super(CustomUserLoginForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.form_action = '/login_view/'
        #self.helper.add_input(Submit('submit', 'Search'))
        self.helper.layout = Layout(
                        
                        Div('email', css_class='col-sm-5', style= 'margin-top: 200px'),
                        Div('password', css_class='col-sm-5', style= 'margin-top: 200px'),
                        Div(FormActions(Submit('submit','Log in'),
                            css_class= 'col-sm-2',
                            style= 'margin-top: 200px')) 
                    )

class ContactForm(forms.Form):
   Name = forms.CharField(required=True)
   Email = forms.EmailField(required=True)
   Message = forms.CharField(required=True, widget=forms.Textarea)

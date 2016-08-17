from django import forms 
from django.contrib.auth.forms import UserCreationForm, UserChangeForm 
from app.models import CustomUser 


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

class CustomUserCreationForm(UserCreationForm):
    def __init__(self, *args, **kargs):
        super(CustomUserCreationForm, self).__init__(*args, **kargs)
        

    class Meta:
        model = CustomUser 
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(CustomUserCreationForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.form_action ='signup'
        #self.helper.add_input(Submit('submit', 'Search'))
        self.helper.layout = Layout(
                        
                        Div('Email', css_class='col-sm-6'),
                        Div('Password', css_class='col-sm-6'),
                        Div(FormActions(Submit('submit','signup')))
                
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
        self.helper.form_action = 'login'
        #self.helper.add_input(Submit('submit', 'Search'))
        self.helper.layout = Layout(
                    Div('email', css_class='col-sm-6 col-md-6'), 
                    Div('password', css_class='col-sm-6 col-md-6'),
                    Div(
                        FormActions(
                            Submit('submit', 'Sign Up')
                        ),
                    css_class='col-sm-12 col-md-12',
                    style='margin-top:25px;'
                    )
            )    

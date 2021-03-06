from django import forms
from django.contrib.auth.models import User
from .models import Profile

#User Profile Form
class UserEditForm(forms.ModelForm):
    class Meta:
        model = User
        
        fields =('first_name','last_name','email')

class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = Profile
        labels = {
            'dob':'Date of Birth',
        }
        fields = ('dob','photo')

#Login Form
class LoginForm(forms.Form):
    username        = forms.CharField()
    password        = forms.CharField(widget=forms.PasswordInput)


#Registration Form
class UserRegistrationForm(forms.ModelForm):
    password    = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2   = forms.CharField(label='Confrim Password', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields =('username','first_name','last_name','email')

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Passowrd don\'t match')
        return cd['password2']

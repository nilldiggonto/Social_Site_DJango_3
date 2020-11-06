from django import forms

#Login Form
class LoginForm(forms.Form):
    username        = forms.CharField()
    password        = forms.CharField(widget=forms.PasswordInput)
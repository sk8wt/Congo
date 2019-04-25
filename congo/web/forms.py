from django import forms

class login_form(forms.Form):
    Username = forms.CharField(label = 'Username')
    password = forms.CharField(label = 'Password')

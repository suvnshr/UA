from django import forms

class RegisterForm(forms.Form):

    name = forms.CharField()
    email = forms.EmailField()
    password = forms.CharField()

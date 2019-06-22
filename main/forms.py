from django import forms

class RegisterForm(forms.Form):

    email = forms.CharField(widget=forms.TextInput(
        attrs={
            'type': 'text'
        }
    ))
    name = forms.CharField()
    password = forms.CharField()


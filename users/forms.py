from django import forms

class LoginForms(forms.Form):
    name_login = forms.CharField(
        label="Login Name",
        max_length=100,
        required=True,
        )
    password_login = forms.CharField(
        label="Password",
        required=True,
        max_length=70,
        widget=forms.PasswordInput()
    )
   
    
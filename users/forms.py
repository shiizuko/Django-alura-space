from django import forms

class LoginForms(forms.Form):
    name_login = forms.CharField(
        label="Login Name",
        max_length=100,
        required=True,
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "Ex:. Maria Antonia",
            }
        ),
        )
    password_login = forms.CharField(
        label="Password",
        required=True,
        max_length=70,
        widget=forms.PasswordInput(
            attrs={
                "class":"form-control",
                "placeholder": "Digite sua senha",
            },
        )
    )
   
    
from django import forms

class LoginForms(forms.Form):
    name_login = forms.CharField(
        label="Nome",
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
        label="Senha",
        required=True,
        max_length=70,
        widget=forms.PasswordInput(
            attrs={
                "class":"form-control",
                "placeholder": "Digite sua senha",
            },
        )
    )
class RegisterForm (forms.Form):
    name_register = forms.CharField(
        label="Nome",
        max_length=100,
        required=True,
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "Ex:. Maria Antonia",
            }
        ),
        )
    email_register = forms.EmailField(
        max_length=100,
        required=True,
        label="Email",
        widget=forms.EmailInput(
            attrs={
                "class":"form-control",
                "placeholder":"Ex:. email@email.com",
                
            }
        )
    )
    password_1 = forms.CharField(
        label="Senha",
        required=True,
        max_length=70,
        widget=forms.PasswordInput(
            attrs={
                "class":"form-control",
                "placeholder": "Digite sua senha",
            },
        )
    )
    password_2 = forms.CharField(
        label="Confirmação de senha",
        required=True,
        max_length=70,
        widget=forms.PasswordInput(
            attrs={
                "class":"form-control",
                "placeholder": "Digite sua senha novamente",
            },
        )
    )

    def clean_name_register(self):
        name = self.cleaned_data.get('name_register')
        if name:
            name = name.strip() # tira os espaços do ínicio e do final da string
            if ' ' in name:
                raise forms.ValidationError("não é possível inserir espaços dentro do campo nome de usuário")
            else:
                return name

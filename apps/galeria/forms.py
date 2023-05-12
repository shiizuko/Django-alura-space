from django import forms

from apps.galeria.models import Photography

class PhotographyForms(forms.ModelForm):
    class Meta:
        model = Photography
        exclude = ['published',]
        labels = {
            'description': 'Description',
            'date_picture': 'Registration Date',
            'user': 'Owner',
            'name': 'Title',
        }
        
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'legend': forms.TextInput(attrs={'class': 'form-control'}),
            'category': forms.Select(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'picture': forms.FileInput(attrs={'class': 'form-control'}),
            'date_picture': forms.DateInput(
                format = '%d/%m/%Y',
                attrs={
                    'type': 'date',
                    'class': 'form-control'
                    }
                ),
            'user': forms.Select(attrs={'class': 'form-control'}),
        }
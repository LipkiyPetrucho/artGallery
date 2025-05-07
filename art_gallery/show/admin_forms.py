from django import forms
from .models import Exhibition


class ExhibitionAdminForm(forms.ModelForm):
    class Meta:
        model = Exhibition
        fields = '__all__'
        widgets = {
            'date': forms.DateInput(attrs={
                'type': 'month',
                'class': 'vDateField'
            })
        }

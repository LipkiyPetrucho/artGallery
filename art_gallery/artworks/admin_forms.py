from django import forms
from .models import Painting
import datetime

class PaintingAdminForm(forms.ModelForm):
    creation_year = forms.IntegerField(label="Год создания", required=False, min_value=1900, max_value=2100)

    class Meta:
        model = Painting
        fields = ["title",
        "material",
        "dimensions",
        "image",
        "description",
        "status",]  # Или перечислите нужные поля

    def save(self, commit=True):
        painting = super().save(commit=False)

        year = self.cleaned_data.get('creation_year')  # используем get() для избежания KeyError
        if year:  # Если год введен
            if painting.created_at:  # Если уже есть дата
                painting.created_at = painting.created_at.replace(year=year)
            else:  # Если дата отсутствует, создаем новую
                painting.created_at = datetime.date(year, 1, 1)  # Устанавливаем на 1 января

        if commit:
            painting.save()
        return painting

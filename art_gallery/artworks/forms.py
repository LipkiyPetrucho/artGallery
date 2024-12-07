from django import forms


class ContactForm(forms.Form):
    name = forms.CharField(
        max_length=100,
        required=True,
        widget=forms.TextInput(attrs={"placeholder": "Имя"}),
    )
    email = forms.EmailField(
        required=True,
        widget=forms.EmailInput(attrs={"placeholder": "E-mail"}),
        error_messages={
            "invalid": "Пожалуйста, введите корректный адрес электронной почты."
        },
    )
    message = forms.CharField(
        widget=forms.Textarea(attrs={"placeholder": "Ваше сообщение", "rows": 2}),
        required=True,
    )
    attachment = forms.FileField(
        required=False, widget=forms.ClearableFileInput(attrs={"class": "file-input"})
    )

    def clean_attachment(self):
        attachment = self.cleaned_data.get("attachment", False)
        if attachment:
            if attachment.size > 4 * 1024 * 1024:
                raise forms.ValidationError("Размер файла не должен превышать 20MB.")
            if not attachment.content_type in [
                "image/jpeg",
                "image/png",
                "application/pdf",
            ]:
                raise forms.ValidationError("Разрешены только файлы JPEG, PNG и PDF.")
        return attachment

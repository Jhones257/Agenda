from django import forms
from django.core.exceptions import ValidationError
from . import models


class ContactForm(forms.ModelForm):
    first_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'classe-a classe-b',
                'placeholder': 'Nome',
            }
        ),
        label='Primeiro Nome',
        help_text='Insira o primeiro nome',
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


    class Meta:
        model = models.Contact
        fields = (
            'first_name', 'last_name', 'phone',
            'email', 'description', 'category',

        )


    def clean(self):
        cleanned_data = super().clean()
        first_name = cleanned_data.get('first_name')
        last_name = cleanned_data.get('last_name')

        if first_name == last_name:
            msg = self.add_error(
                'first_name',
                ValidationError(
                    'O primeiro nome não pode ser igual ao último nome',
                    code='invalid'
                )
            )
            self.add_error('first_name', msg)
            self.add_error('last_name', msg)
        return super().clean()

    def clean_first_name(self):
        first_name = self.cleaned_data.get('first_name')
        if len(first_name) < 3:
            raise ValidationError('O primeiro nome deve ter mais de 3 caracteres')
        return first_name
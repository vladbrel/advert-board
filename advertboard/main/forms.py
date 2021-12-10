from .models import Ad
from django.forms import ModelForm, TextInput, Textarea


class AdForm(ModelForm):
    class Meta:
        model = Ad
        fields = ['name', 'price', 'description', 'category']
        widgets = {
            'name': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите название'
            }),

            'price': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите цену'
            }),
            'description': Textarea(attrs={
                'class': 'form-control',
                'placeholder' : 'Введите описание'
            }),
            'category': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите категорию'
            })
        }
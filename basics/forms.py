from django import forms
from core.models import Item


class ProductForm(forms.ModelForm):
    name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "Your full name"
            }
        )
    )
    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={
                "class": "form-control",
                "placeholder": "Your email"
            }
        )
    )
    message = forms.CharField(
        widget=forms.Textarea(
            attrs={
                'class': 'form-control',
                "placeholder": "Your message"
            }
        )
    )

    class Meta:
        model = Item
        fields = [
            'custom_design',
            'print_text',
            'size',
            'color',
            'instruction'
        ]

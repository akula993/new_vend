from django import forms
from django.forms import Textarea

from vend.models import Address


# class AddressForm(forms.Form):
#     name = forms.CharField(max_length=255, label="Заголовок",widget=forms.widgets.Textarea)
#     # slug = forms.SlugField(max_length=255, label="URL")
#     # to_rent = forms.DecimalField(max_digits=10, decimal_places=2, label='Аренда')

class AddressForm(forms.ModelForm):


    class Meta:
        model = Address
        fields = ['name', 'slug', 'to_rent']  # list of fields you want from model

        widgets = {
            'name': Textarea(attrs={'cols': 80, 'rows': 20}),
        }
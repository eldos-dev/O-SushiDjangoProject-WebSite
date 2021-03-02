from django import forms
from django.forms import modelformset_factory

from apps.product.models import Product


class CreateProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'



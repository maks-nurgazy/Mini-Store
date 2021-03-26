from django import forms

from store.models import Product


class ProductForm(forms.ModelForm):
    description = forms.CharField(max_length=1000, widget=forms.Textarea())

    class Meta:
        model = Product
        fields = '__all__'

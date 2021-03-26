from django import forms

from store.models import Category


def get_category_choices():
    return [(int(obj.id), obj.name) for obj in Category.objects.all()]


class CategoryForm(forms.Form):
    category = forms.ChoiceField(required=False, widget=forms.Select(attrs={'class': 'form-control'}),
                                 choices=get_category_choices,
                                 label="Some content")

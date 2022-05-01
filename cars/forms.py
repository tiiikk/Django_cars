from django import forms

from .models import Category, Car

CHOICE_LIST = [
    (y, y) for y in range(1900, 2022)
]
CHOICE_LIST.insert(0, ('', '----'))


class CarSearchForm(forms.Form):
    category = forms.ModelChoiceField(Category.objects.order_by('name'), required=False)
    name = forms.CharField(required=False)
    vin = forms.CharField(required=False)
    year = forms.ChoiceField(choices=CHOICE_LIST, required=False)

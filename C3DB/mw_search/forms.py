from django import forms
from index.models import Category, fpCategory

CATEGORY_CHOICES = [(i.id, i) for i in Category.objects.all()]

class MassSearchForm(forms.Form):
    Category = forms.TypedChoiceField(choices=CATEGORY_CHOICES, widget=forms.Select(attrs={'class': 'chzn-select selectpicker',
                                                                                           'data-style': 'btn-primary'}))

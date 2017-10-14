from django import forms
from index.models import Category


CATEGORY_CHOICES = [(i.id, i) for i in Category.objects.all()]


class ExactSearchForm(forms.Form):
    """ Form class for exact molecule search. """
    Category = forms.TypedChoiceField(choices=CATEGORY_CHOICES, widget=forms.Select(attrs={'class': 'chzn-select selectpicker',
                                                                                           'data-style': 'btn-primary'}))
    Exact_Search = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Input CID, InChI, Smiles and Formular'}))

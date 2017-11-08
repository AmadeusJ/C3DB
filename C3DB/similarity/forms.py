from django import forms
from index.models import Category, fpCategory


CATEGORY_CHOICES = [ (i.id , i) for i in Category.objects.all() ]
FP_CATEGORY_CHOICES = [(j.id, j) for j in fpCategory.objects.all()]


class SimilaritySearchForm(forms.Form):
    Category = forms.TypedChoiceField(choices=CATEGORY_CHOICES, widget=forms.Select(attrs={'class': 'chzn-select selectpicker',
                                                                                           'data-style': 'btn-primary'}))
    Similar_Search = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Input InChI and Smiles'}))
    fp_category = forms.TypedChoiceField(choices=FP_CATEGORY_CHOICES, widget=forms.Select())
    tanimoto_min = forms.FloatField(widget=forms.NumberInput(attrs={'class': 'filter'}), required=True)
    tanimoto_max = forms.FloatField(widget=forms.NumberInput(attrs={'class': 'filter'}), required=False)


    LogP_min2 = forms.CharField(max_length=5, widget=forms.NumberInput(attrs={'class': 'filter'}), required=False)
    LogP_max2 = forms.CharField(widget=forms.NumberInput(attrs={'class': 'filter'}), required=False)

    ringnum_min2 = forms.CharField(widget=forms.NumberInput(attrs={'class': 'filter'}), required=False)
    ringnum_max2 = forms.CharField(widget=forms.NumberInput(attrs={'class': 'filter'}), required=False)

    molweight_min2 = forms.CharField(widget=forms.NumberInput(attrs={'class': 'filter',
                                                                     'size': 5,
                                                                     'maxlength': 5}), required=False)
    molweight_max2 = forms.CharField(widget=forms.NumberInput(attrs={'class': 'filter',
                                                                     'size': 5,
                                                                     'maxlength': 5}), required=False)

    AtomNum_min2 = forms.CharField(widget=forms.NumberInput(attrs={'class': 'filter'}), required=False)
    AtomNum_max2 = forms.CharField(widget=forms.NumberInput(attrs={'class': 'filter'}), required=False)

    BondNum_min2 = forms.CharField(widget=forms.NumberInput(attrs={'class': 'filter'}), required=False)
    BondNum_max2 = forms.CharField(widget=forms.NumberInput(attrs={'class': 'filter'}), required=False)

    Rotate_min2 = forms.CharField(widget=forms.NumberInput(attrs={'class': 'filter'}), required=False)
    Rotate_max2 = forms.CharField(widget=forms.NumberInput(attrs={'class': 'filter'}), required=False)

    Formal_min2 = forms.CharField(widget=forms.NumberInput(attrs={'class': 'filter'}), required=False)
    Formal_max2 = forms.CharField(widget=forms.NumberInput(attrs={'class': 'filter'}), required=False)

    HBA_min2 = forms.CharField(widget=forms.NumberInput(attrs={'class': 'filter'}), required=False)
    HBA_max2 = forms.CharField(widget=forms.NumberInput(attrs={'class': 'filter'}), required=False)

    HBD_min2 = forms.CharField(widget=forms.NumberInput(attrs={'class': 'filter'}), required=False)
    HBD_max2 = forms.CharField(widget=forms.NumberInput(attrs={'class': 'filter'}), required=False)


from django import forms
from index.models import Category, fpCategory


CATEGORY_CHOICES = [(i.id, i) for i in Category.objects.all()]



class FunctionalSearchForm(forms.Form):
    Category = forms.TypedChoiceField(choices=CATEGORY_CHOICES, widget=forms.Select(attrs={'class': 'chzn-select selectpicker',
                                                                                           'data-style': 'btn-primary'}))
    Sub_Search = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Input InChI and Smiles'}))

    FC_Num = forms.CharField(widget=forms.NumberInput(attrs={'class': 'filter',
                                                             'size': 2,
                                                             'maxlength': 2}),
                             required=True,
                             initial=1)

    methyl_amide = forms.CharField(max_length=2, widget=forms.NumberInput(attrs={'class': 'filter'}), required=False)


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
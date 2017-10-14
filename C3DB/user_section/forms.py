from django import forms
from index.models import Category, fpCategory
from .models import UserDataBase


CATEGORY_CHOICES = [ (i.id , i) for i in Category.objects.all() ]


class UserdbHandlerForm(forms.Form):
    Category = forms.TypedChoiceField(choices=CATEGORY_CHOICES,
                                      widget=forms.Select(attrs={'class': 'chzn-select selectpicker',
                                                                 'data-style': 'btn-primary',}))


class MakingUserDB(forms.Form):
    user_db_name = forms.CharField(max_length=30, help_text="Required. Inform a your database name.", )

    class Meta:
        model = UserDataBase
        fields = ('user_db_name',)

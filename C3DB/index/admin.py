# -*- coding: utf-8 -*-
from django.contrib import admin
from .models import Category, MoleculeData, fpCategory
from user_section.models import UserMolecule


# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['category']

admin.site.register(Category, CategoryAdmin)


class MoleculeDataAdmin(admin.ModelAdmin):
    list_display = ['SSU_CID', 'Py_MW', 'AtomNumber', 'BondNumber', 'RingNumber', 'LogP',
                    'PUB_CID', 'Formula', 'InChI', 'SMILES', 'FormalCharge', 'HBA',
                    'HBD', 'RotateBond', 'category', 'RDKit_MW']

    list_filter = ['Py_MW', 'AtomNumber', 'BondNumber', 'RingNumber', 'LogP',
                   'FormalCharge', 'HBA', 'HBD', 'RotateBond', 'category', 'RDKit_MW']

admin.site.register(MoleculeData, MoleculeDataAdmin)

#class UserMoleculeAdmin(admin.ModelAdmin):
#    list_display = ['user_id', 'user_mol']

#admin.site.register(UserMolecule, UserMoleculeAdmin)


class fpCategoryAdmin(admin.ModelAdmin):
    list_display = ['category']

admin.site.register(fpCategory, fpCategoryAdmin)

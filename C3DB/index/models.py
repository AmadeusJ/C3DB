# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


# ============================== DB Category Table ========================================
class Category(models.Model):
    """
    DataBase category model
    """
    category = models.CharField(max_length=20)

    class Meta:
        db_table = 'DB_Category'
        verbose_name = 'category'
        verbose_name_plural = 'categories'
        ordering = ('id',)

    def __unicode__(self):
        return unicode(self.category)


# ============================== FingerPrint Category Table ========================================
class fpCategory(models.Model):
    """ Molecule Finger-Print categories """
    category = models.CharField(max_length=20)

    class Meta:
        db_table = 'DB_fpCategory'
        verbose_name = 'fpcategory'
        verbose_name_plural = 'fpcategories'

    def __unicode__(self):
        return unicode(self.category)


# ============================== Molecule Data Table ========================================
# Created Date: 2017-10-13
# Updated Date: -
class MoleculeData(models.Model):
    """
    Molecule data model
    """
    SSU_CID = models.IntegerField()
    Py_MW = models.FloatField(null=True)
    AtomNumber = models.IntegerField(null=True)
    BondNumber = models.IntegerField(null=True)
    RingNumber = models.IntegerField(null=True)
    LogP = models.FloatField(null=True)
    PUB_CID = models.TextField(null=True)
    Formula = models.TextField(null=True)
    InChI = models.TextField(null=True)
    SMILES = models.TextField(null=True)
    SMARTS = models.TextField(null=True)
    FormalCharge = models.IntegerField(null=True)
    HBA = models.IntegerField(null=True)
    HBD = models.IntegerField(null=True)
    RotateBond = models.IntegerField(null=True)
    category = models.ForeignKey(Category, related_name='molecules')
    RDKit_MW = models.FloatField(null=True)
    yaChI = models.TextField(null=True)
    TPSA = models.FloatField(null=True)
    InChIKey = models.TextField(null=True)

    class Meta:
        db_table = 'DB_Data'
        ordering = ('SSU_CID',)

    def __str__(self):
        return '{0} {1} {2} {3} {4} {5} {6} {7} {8} {9} {10} {11} {12} {13} {14}'.format(self.SSU_CID, self.Py_MW, self.AtomNumber, self.BondNumber,
                                                                                         self.RingNumber, self.LogP, self.PUB_CID, self.Formula,
                                                                                         self.InChI,self.SMILES, self.FormalCharge, self.HBA,
                                                                                         self.HBD, self.RotateBond, self.category, self.RDKit_MW)


# ============================== Molecule Data Table ========================================
# Created Date: 2017-10-13
# Updated Date: -
class MopacData(models.Model):
    """
    Molecule descriptors from mopac
    """
    SSU_CID = models.IntegerField()
    Heat = models.FloatField(null=True)
    Total_Energy = models.FloatField(null=True)
    Elec_Energy = models.FloatField(null=True)
    Point_Group = models.FloatField(null=True)
    COSMO_Area = models.FloatField(null=True)
    COSMO_Volume = models.FloatField(null=True)
    Ion_Potential = models.FloatField(null=True)
    HOMO = models.FloatField(null=True)
    LUMO = models.FloatField(null=True)
    Dimensions = models.TextField(null=True)
    Charge = models.TextField(null=True)

    class Meta:
        db_table = 'DB_Mopac_1'
        ordering = ('SSU_CID',)


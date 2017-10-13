# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from index.models import Category


# Create your models here.

class UserDataBase(models.Model):
    """
    User custom Database.
    """
    user = models.ForeignKey(User, related_name='myDB', db_index=True)
    user_db_name = models.CharField(max_length=30, db_index=True)
    created = models.DateTimeField(auto_now_add=True, db_index=True)

    class Meta:
        db_table = 'DB_UserDB'


class UserMolecule(models.Model):
    """
    Storage model for user own db.
    """
    user_db = models.ForeignKey(UserDataBase, related_name='myMols', db_index=True)
    user_mol = models.IntegerField(db_index=True, unique=False)
    added = models.DateTimeField(auto_now_add=True, db_index=True)


    class Meta:
        db_table = 'DB_UserMol'
        ordering = ('user_db',)


    def __str__(self):
        return '{}'.format(self.user_db)


class UserCategory(models.Model):
    """
    User Database Select Category.
    """
    user_db = models.ForeignKey(UserDataBase, related_name='myCategory', db_index=True)
    category = models.CharField(max_length=20)

    class Meta:
        db_table = 'DB_User_Category'
        verbose_name = 'category'
        verbose_name_plural = 'categories'
        ordering = ('id',)

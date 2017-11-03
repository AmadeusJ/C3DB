# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class MgfPath(models.Model):
    """
    Check mgf folder
    """
    SSU_CID = models.IntegerField()
    mgf = models.TextField(null=True)

    class Meta:
        db_table = 'DB_mgf'
        ordering = ('SSU_CID',)

    def __str__(self):
        return

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.decorators import login_required
from django.db import IntegrityError
from user_section.models import UserDataBase, UserMolecule


class UserDataBaseHandler(object):
    def __init__(self, request):
        """
        Handler user database.
        :param request: 
        """
        # Get the request
        self.request = request

        # Get the current user
        self.current_user = request.user

        # Get the current user's db
        self.user_db = UserDataBase.objects.filter(user_id=self.current_user.id)

    def mol_add(self):
        """ Add selected molecules to user db. """
        mol_set = self.request.POST.getlist('user_mol')
        if len(mol_set) != 0:
            current_user = self.current_user.id
#            for SSU_CID in mol_set:

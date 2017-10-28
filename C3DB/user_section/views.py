# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.db import IntegrityError
from django.core import serializers
from django.core.serializers.json import DjangoJSONEncoder
from .forms import MakingUserDB
from .models import UserDataBase, UserMolecule
from index.models import MoleculeData
from common.decorators import ajax_required

# Create your views here.

@login_required
def user_db(request):
    """ User Workbench main UI. """
    current_user = request.user
    user_db = UserDataBase.objects.filter(user_id=current_user.id)

    # Redirect if user has db nothing.
    if len(user_db) == 0:
        return redirect('C3DB:user_db_create')

    else:

        context = {
            'user_db': user_db
        }
        return render(request, 'user/user_db.html', context)


@login_required
def user_db_create_ui(request):
    """ Render user_db_Creation form """
    current_user = request.user
    user_db = UserDataBase.objects.filter(user_id=current_user.id)

    if request.method == 'POST':
        form = MakingUserDB(request.POST)
        if form.is_valid():
            user_db_name = form.cleaned_data['user_db_name']
            UserDataBase.objects.create(user_db_name=str(user_db_name), user_id=int(current_user.id))

            return redirect('C3DB:user_db')

    else:
        form = MakingUserDB()
        context = {
            'form': form,
            'user_db': user_db
        }

    return render(request, 'user/user_db_create.html', context)


@ajax_required
@login_required
def user_db_delete(request):
    """ Delete user_db """
    current_user = request.user
    user_db_id = int(request.POST.get('user_db_id'))
    try:
        user_db_mol = UserMolecule.objects.filter(user_db_id=user_db_id)
        user_db_mol.delete()
        user_db = UserDataBase.objects.filter(id=user_db_id)
        user_db.delete()

        return JsonResponse({'status': 'ok'})

    except Exception as err:
        print err
        pass

    return JsonResponse({'status': 'None'})


@ajax_required
@login_required
def mol_show(request):
    """ Show user' molecules from user's db. """
    user_db_id = request.POST.get('user_db_id')
    current_user = request.user.id
    user_mol_set = UserMolecule.objects.filter(user_db_id=int(user_db_id))
    mol_set = []
    for mol in user_mol_set:
        mol_set.append(MoleculeData.objects.get(SSU_CID=int(mol.user_mol)))

    data = serializers.serialize('json', mol_set, cls=DjangoJSONEncoder)

    return JsonResponse({'status': 'ok', 'mol_set': data})


@ajax_required
@login_required
def mol_add(request):
    """ Add selected molecules to user db. """
    mol_set = request.POST.getlist('mol_ids[]')  # Do like this 'mol_ids[]', if ajax sending signal has 'array' type data !!
    user_db_id = request.POST.get('user_db_id')

    print mol_set
    if len(mol_set) != 0:
        current_user = request.user.id
        user_selected_db = [db.id for db in UserDataBase.objects.filter(user_id=current_user) if db.id == int(user_db_id)]
        user_selected_db = user_selected_db[0]

        duplicate_list = []
        for SSU_CID in mol_set:
            try:
                # Don't make the new mol if same mol already in same user db selected
                duplicate_mol = UserMolecule.objects.filter(user_mol=int(SSU_CID), user_db_id=user_selected_db)
                if duplicate_mol:
                    duplicate_list.append(SSU_CID)
                else:
                    UserMolecule.objects.create(user_db_id=user_selected_db, user_mol=int(SSU_CID))

            # Chek if user already has molecule.
            except IntegrityError as err:
                print err
                pass

        if len(duplicate_list) != 0:
            return JsonResponse({'status': 'duplicate', 'duplicate': duplicate_list})
        else:
            return JsonResponse({'status': 'ok'})

    else:
        return JsonResponse({'status': 'None'})


@ajax_required
@login_required
def mol_delete(request):
    """ Remove selected molecuoles from user db. """
    mol_set = request.POST.getlist('user_mols[]')
    print mol_set
    user_db_id = int(request.POST.get('user_db_id'))
    print user_db_id
    for SSU_CID in mol_set:
        UserMolecule.objects.get(user_mol=int(SSU_CID), user_db_id=user_db_id).delete()

    return JsonResponse({'status': 'ok'})

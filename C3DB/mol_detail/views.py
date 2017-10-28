# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404
from index.models import MoleculeData
from django.http import HttpResponse, JsonResponse
from common.decorators import ajax_required
from user_section.models import UserDataBase


def addZero(ssu_cid):
    final_num = ""
    num = str(ssu_cid)
    num_len = len(num)
    if num_len == 1:
        while len(final_num) < 8:
            final_num += "0"
        final_num += num

    elif num_len == 2:
        while len(final_num) < 7:
            final_num += "0"
        final_num += num

    elif num_len == 3:
        while len(final_num) < 6:
            final_num += "0"
        final_num += num

    elif num_len == 4:
        while len(final_num) < 5:
            final_num += "0"
        final_num += num

    elif num_len == 5:
        while len(final_num) < 4:
            final_num += "0"
        final_num += num

    elif num_len == 6:
        while len(final_num) < 3:
            final_num += "0"
        final_num += num

    elif num_len == 7:
        while len(final_num) < 2:
            final_num += "0"
        final_num += num

    elif num_len == 8:
        while len(final_num) < 1:
            final_num += "0"
        final_num += num

    return final_num


def getMolFilePath(ssu_cid):
    ssu_cid = int(ssu_cid)
    ssu_cid_string = addZero(ssu_cid)
    dir = ssu_cid_string[:4]

    final_path = "/C3DB/mol/{}/{}.mol".format(dir, ssu_cid_string)

    return final_path


def result_detail(request, SSU_CID):
    """ Result Detail Page """
    user_db = None
    molecule = get_object_or_404(MoleculeData, SSU_CID=SSU_CID)

    if request.user.is_active:
        user_db = UserDataBase.objects.filter(user_id=request.user.id)

    mol_content = ""
    try:
        mol_file_path = getMolFilePath(SSU_CID)
        print mol_file_path
        for line in open(mol_file_path):
            mol_content += line

    except Exception as err:
        pass
        print mol_content
    return render(request, 'result/result_detail.html', {'mol': molecule, 'mol_file': mol_content, 'user_db': user_db})


@ajax_required
def getMolFileContent(request):
    """ Get the .mol file content from server """

    molFilePath = str(request.POST.get('molFilePath'))
    try:
        mol_content = """"""
        molFileContent = open(molFilePath)
        for line in molFileContent:
            mol_content += line

        return JsonResponse({'status': 'ok', 'molFileContent': mol_content})

    except Exception as err:

        return JsonResponse({'status': 'fail', 'err_msg': "Sorry, Can't get the mol file..."})


def JMol3DViewer(request, SSU_CID):
    """ Show the 3D moleule with JMol """
    user_db = None
    molecule = get_object_or_404(MoleculeData, SSU_CID=SSU_CID)

    if request.user.is_active:
        user_db = UserDataBase.objects.filter(user_id=request.user.id)

    mol_content = ""
    try:
        mol_file_path = getMolFilePath(SSU_CID)
        print mol_file_path
        for line in open(mol_file_path):
            mol_content += line

    except Exception as err:
        pass
        print mol_content

    return render(request, 'result/result_jsmol.html', {'mol': molecule, 'mol_file': mol_content, 'user_db': user_db})

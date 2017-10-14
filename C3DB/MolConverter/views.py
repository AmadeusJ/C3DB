# -*- coding: utf-8 -*-

import json
from rdkit import Chem
from rdkit.Chem import AllChem
from django.http import HttpResponse


# Create your views here.

def MolConversion(request):
    """ Convert molecule format wit RDKit. """
    if request.is_ajax():
        if 'MolForSmarts' in request.POST.keys() and request.POST['MolForSmarts']:
            mol = request.POST['MolForSmarts']
            mol = mol.encode('ascii', 'ignore')
            try:
                rdmol = Chem.MolFromMolBlock(mol)
                smarts = Chem.MolToSmarts(rdmol)
                data = {
                    'smarts': smarts
                }
                json_data = json.dumps(data)

                return HttpResponse(json_data, content_type='application/json')

            except Exception as err:
                data = {
                    'err_msg': err
                }
                json_data = json.dumps(data)

                return HttpResponse(json_data, content_type='application/json')

        else:
            data = "No mol..."
            json_data = json.dumps(data)

            return HttpResponse(json_data, content_type='application/json')

    else:
        data = "This is not an ajax request! or Something wrong!"
        json_data = json.dumps(data)

        return HttpResponse(json_data, content_type='application/json')


def InChIFromMarvinJS(request):
    """ Convert molecule from marvin to inchi """
    if request.is_ajax():
        if 'MarvinForInchi' in request.POST.keys() and request.POST['MarvinForInchi']:
            mol = request.POST['MarvinForInchi']
            mol = mol.encode('ascii', 'ignore')
            try:
                rdmol = Chem.MolFromMolBlock(mol)
                inchi = Chem.MolToInchi(rdmol)
                data = {
                    'inchi': inchi
                }
                json_data = json.dumps(data)

                return HttpResponse(json_data, content_type='application/json')

            except Exception as err:
                data = {
                    'err_msg': err
                }
                json_data = json.dumps(data)

                return HttpResponse(json_data, content_type='application/json')
        else:
            data = "No mol..."
            json_data = json.dumps(data)

            return HttpResponse(json_data, content_type='application/json')
    else:
        data = "This is not an ajax request! or Something wrong!"
        json_data = json.dumps(data)

        return HttpResponse(json_data, content_type='application/json')


def YaChIFromMarvinJS(request):
    """ Convert molecule from marvin to inchi """
    if request.is_ajax():
        if 'MarvinForYachi' in request.POST.keys() and request.POST['MarvinForYachi']:
            mol = request.POST['MarvinForYachi']
            mol = mol.encode('ascii', 'ignore')
            rdmol = Chem.MolFromMolBlock(mol)
            rdmol = Chem.AddHs(rdmol)
            AllChem.EmbedMolecule(rdmol)
            AllChem.UFFOptimizeMolecule(rdmol)
            new_mol = Chem.MolToMolBlock(rdmol)
            import sys
            iChem = "/share/iChem"
            sys.path.append(iChem + '/LIB/')
            sys.path.append(iChem + '/YACHI/')
            from Core import *
            mol2 = Core()
            mol2.sdf2core(new_mol)
            yachi = mol2.yaChI2()
            print yachi
            try:

                data = {
                    'yachi': yachi
                }
                json_data = json.dumps(data)

                return HttpResponse(json_data, content_type='application/json')

            except Exception as err:
                data = {
                    'err_msg': err
                }
                json_data = json.dumps(data)

                return HttpResponse(json_data, content_type='application/json')
        else:
            data = "No mol..."
            json_data = json.dumps(data)

            return HttpResponse(json_data, content_type='application/json')
    else:
        data = "This is not an ajax request! or Something wrong!"
        json_data = json.dumps(data)

        return HttpResponse(json_data, content_type='application/json')


def SmilesFromMarvinJS(request):
    """ Convert molecule from marvin to smiles """
    if request.is_ajax():
        if 'MarvinForSmiles' in request.POST.keys() and request.POST['MarvinForSmiles']:
            mol = request.POST['MarvinForSmiles']
            mol = mol.encode('ascii', 'ignore')
            try:
                rdmol = Chem.MolFromMolBlock(mol)
                smiles = Chem.MolToSmiles(rdmol)
                data = {
                    'smiles': smiles
                }
                json_data = json.dumps(data)

                return HttpResponse(json_data, content_type='application/json')
            except Exception as err:
                data = {
                    'err_msg': err
                }
                json_data = json.dumps(data)

                return HttpResponse(json_data, content_type='application/json')
        else:
            data = "No mol..."
            json_data = json.dumps(data)

            return HttpResponse(json_data, content_type='application/json')
    else:
        data = "This is not an ajax request! or Something wrong!"
        json_data = json.dumps(data)

        return HttpResponse(json_data, content_type='application/json')

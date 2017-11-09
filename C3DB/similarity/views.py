# -*- coding: utf-8 -*-
from celery.result import AsyncResult
from C3DB.celery2 import *
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from .forms import SimilaritySearchForm
from index.models import Category, fpCategory
from .task import similar_search
from user_section.models import UserDataBase
from SearchSession.search import SearchSession


# Create your views here.


def similar_search_form(request):
    """ A view for similarity search """
    user_db = None
    flt_mw_min = None
    flt_mw_max = None
    flt_atom_num_min = None
    flt_atom_num_max = None
    flt_bond_num_min = None
    flt_bond_num_max = None
    flt_ring_num_min = None
    flt_ring_num_max = None
    flt_rotate_min = None
    flt_rotate_max = None
    flt_formal_min = None
    flt_formal_max = None
    flt_hba_min = None
    flt_hba_max = None
    flt_hbd_min = None
    flt_hbd_max = None
    flt_logP_min = None
    flt_logP_max = None
    cosmo_area_min = None
    cosmo_area_max = None
    cosmo_volume_min = None
    cosmo_volume_max = None
    dimensions_min = None
    dimensions_max = None
    elec_energy_min = None
    elec_energy_max = None
    homo_min = None
    homo_max = None
    lumo_min = None
    lumo_max = None
    total_energy_min = None
    total_energy_max = None

    if 'job' in request.GET:
        job_id = request.GET['job']
        job = AsyncResult(job_id)
        data = job.result
        query_session = SearchSession(request)
        query_stored = query_session.show()

        # Run when user is log-in
        if request.user.is_active:
            user_db = UserDataBase.objects.filter(user_id=request.user.id)

        context = {
            'data': data,
            'task_id': job_id,
            'query_similarity': query_stored['similarity_query'],
            'query_tanimoto': query_stored['tanimoto'],
            'user_db': user_db,
        }
        return render(request, 'result/similar_result_list.html', context)

    elif 'Similar_Search' in request.GET:
        query = request.GET['Similar_Search']
        category = request.GET['Category']
        fp_category = request.GET['fp_category']
        tanimoto = request.GET['tanimoto_min']
        max_result = request.GET['max_result']
        exclude_atoms = request.GET['exclude_atoms']

        try:
            if request.GET['molweight_min2']:
                flt_mw_min = request.GET['molweight_min2']
        except KeyError:
            pass

        try:
            if request.GET['molweight_max2']:
                flt_mw_max = request.GET['molweight_max2']
        except KeyError:
            pass

        try:
            if request.GET['AtomNum_min2']:
                flt_atom_num_min = request.GET['AtomNum_min2']
        except KeyError:
            pass

        try:
            if request.GET['AtomNum_max2']:
                flt_atom_num_max = request.GET['AtomNum_max2']
        except KeyError:
            pass

        try:
            if request.GET['BondNum_min2']:
                flt_bond_num_min = request.GET['BondNum_min2']
        except KeyError:
            pass

        try:
            if request.GET['BondNum_max2']:
                flt_bond_num_max = request.GET['BondNum_max2']
        except KeyError:
            pass

        try:
            if request.GET['ringnum_min2']:
                flt_ring_num_min = request.GET['ringnum_min2']
        except KeyError:
            pass

        try:
            if request.GET['ringnum_max2']:
                flt_ring_num_max = request.GET['ringnum_max2']
        except KeyError:
            pass

        try:
            if request.GET['Rotate_min2']:
                flt_rotate_min = request.GET['Rotate_min2']
        except KeyError:
            pass

        try:
            if request.GET['Rotate_max2']:
                flt_rotate_max = request.GET['Rotate_max2']
        except KeyError:
            pass

        try:
            if request.GET['Formal_min2']:
                flt_formal_min = request.GET['Formal_min2']
        except KeyError:
            pass

        try:
            if request.GET['Formal_max2']:
                flt_formal_max = request.GET['Formal_max2']
        except KeyError:
            pass

        try:
            if request.GET['HBA_min2']:
                flt_hba_min = request.GET['HBA_min2']
        except KeyError:
            pass

        try:
            if request.GET['HBA_max2']:
                flt_hba_max = request.GET['HBA_max2']
        except KeyError:
            pass

        try:
            if request.GET['HBD_min2']:
                flt_hbd_min = request.GET['HBD_min2']

        except KeyError:
            pass

        try:
            if request.GET['HBD_max2']:
                flt_hbd_max = request.GET['HBD_max2']
        except KeyError:
            pass

        try:
            if request.GET['LogP_min2']:
                flt_logP_min = request.GET['LogP_min2']
        except KeyError:
            pass

        try:
            if request.GET['LogP_max2']:
                flt_logP_max = request.GET['LogP_max2']
        except KeyError:
            pass

        try:
            if request.GET['cosmo_area_min']:
                cosmo_area_min = request.GET['cosmo_area_min']
        except KeyError:
            pass

        try:
            if request.GET['cosmo_area_max']:
                cosmo_area_max = request.GET['cosmo_area_max']
        except KeyError:
            pass

        try:
            if request.GET['cosmo_volume_min']:
                cosmo_volume_min = request.GET['cosmo_volume_min']
        except KeyError:
            pass

        try:
            if request.GET['cosmo_volume_max']:
                cosmo_volume_max = request.GET['cosmo_volume_max']
        except KeyError:
            pass

        try:
            if request.GET['dimensions_min']:
                dimensions_min = request.GET['dimensions_min']
        except KeyError:
            pass

        try:
            if request.GET['dimensions_max']:
                dimensions_max = request.GET['dimensions_max']
        except KeyError:
            pass

        try:
            if request.GET['elec_energy_min']:
                elec_energy_min = request.GET['elec_energy_min']
        except KeyError:
            pass

        try:
            if request.GET['elec_energy_max']:
                elec_energy_max = request.GET['elec_energy_max']
        except KeyError:
            pass

        try:
            if request.GET['homo_min']:
                homo_min = request.GET['homo_min']
        except KeyError:
            pass

        try:
            if request.GET['homo_max']:
                homo_max = request.GET['homo_max']
        except KeyError:
            pass

        try:
            if request.GET['lumo_min']:
                lumo_min = request.GET['lumo_min']
        except KeyError:
            pass

        try:
            if request.GET['lumo_max']:
                lumo_max = request.GET['lumo_max']
        except KeyError:
            pass

        try:
            if request.GET['total_energy_min']:
                total_energy_min = request.GET['total_energy_min']
        except KeyError:
            pass

        try:
            if request.GET['total_energy_max']:
                total_energy_max = request.GET['total_energy_max']
        except KeyError:
            pass

        job = similar_search.delay(category, fp_category, tanimoto, max_result, query, exclude_atoms,
                                   mw_min=flt_mw_min, mw_max=flt_mw_max,
                                   atom_min=flt_atom_num_min, atom_max=flt_atom_num_max,
                                   bond_min=flt_bond_num_min, bond_max=flt_bond_num_max,
                                   ring_min=flt_ring_num_min, ring_max=flt_ring_num_max,
                                   rotate_min=flt_rotate_min, rotate_max=flt_rotate_max,
                                   formal_min=flt_formal_min, formal_max=flt_formal_max,
                                   hba_min=flt_hba_min, hba_max=flt_hba_max,
                                   hbd_min=flt_hbd_min, hbd_max=flt_hbd_max,
                                   logP_min=flt_logP_min, logP_max=flt_logP_max,
                                   cosmo_area_min=cosmo_area_min, cosmo_area_max=cosmo_area_max,
                                   cosmo_volume_min=cosmo_volume_min, cosmo_volume_max=cosmo_volume_max,
                                   dimensions_min=dimensions_min, dimensions_max=dimensions_max,
                                   elec_energy_min=elec_energy_min, elec_energy_max=elec_energy_max,
                                   homo_min=homo_min, homo_max=homo_max,
                                   lumo_min=lumo_min, lumo_max=lumo_max,
                                   total_energy_min=total_energy_min, total_energy_max=total_energy_max)

        # Store query to session
        query_session = SearchSession(request)
        query_session.get_similarity_search_query(job.id, query, tanimoto)

        return HttpResponseRedirect(reverse('C3DB:similar') + '?job=' + job.id)

    else:
        # Reset the Session
        query_session = SearchSession(request)
        query_stored = query_session.show()

        # If user get back to search ui during the job searchin, terminate the job.
        try:
            if query_stored['task_id']:
                app.control.revoke(str(query_stored['task_id']), terminate=True) # => This line only works on UINX type OS !!!
                query_session.clear()
                return HttpResponseRedirect(reverse('C3DB:similar'))

        except KeyError as err:
            print err
            pass

        query_session.clear()

        form = SimilaritySearchForm()
        categories = Category.objects.all()
        fp_categories = fpCategory.objects.all()
        context = {
            'form': form,
            'categories': categories,
            'fp_categories': fp_categories
        }
        return render(request, 'search/similar_search.html', context)

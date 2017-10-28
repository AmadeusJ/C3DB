from celery.result import AsyncResult
from C3DB.celery2 import *
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from .forms import SubstructSearchForm
from index.models import Category
from .task import substructure_search
from user_section.models import UserDataBase
from SearchSession.search import SearchSession


# Create your views here.


def substruct_search_form(request):
    """ A view for substructure search """
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

    if 'job' in request.GET:
        job_id = request.GET['job']
        job = AsyncResult(job_id)
        data = job.result
        query_session = SearchSession(request)
        query_stored = query_session.show()
        form = SubstructSearchForm()

        # Run when user is log-in
        if request.user.is_active:
            user_db = UserDataBase.objects.filter(user_id=request.user.id)

        context = {
            'data': data,
            'task_id': job_id,
            'form': form,
            'substruct_query' : query_stored['substruct_query'],
            'user_db': user_db,
        }
        return render(request, 'result/substruct_result_list.html', context)

    elif 'Sub_Search' in request.GET:
        query = request.GET['Sub_Search']
        super_sub = request.POST.get('Supersub', False)
        category = request.GET['Category']
        max_result = request.GET['max_result']
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

        # Run search
        job = substructure_search.delay(category, super_sub, max_result, query,
                                        mw_min=flt_mw_min, mw_max=flt_mw_max,
                                        atom_min=flt_atom_num_min, atom_max=flt_atom_num_max,
                                        bond_min=flt_bond_num_min, bond_max=flt_bond_num_max,
                                        ring_min=flt_ring_num_min, ring_max=flt_ring_num_max,
                                        rotate_min=flt_rotate_min, rotate_max=flt_rotate_max,
                                        formal_min=flt_formal_min, formal_max=flt_formal_max,
                                        hba_min=flt_hba_min, hba_max=flt_hba_max,
                                        hbd_min=flt_hbd_min, hbd_max=flt_hbd_max,
                                        logP_min=flt_logP_min, logP_max=flt_logP_max)

        # Store query to session
        query_session = SearchSession(request)
        query_session.get_substruct_search_query(job.id, query)

        return HttpResponseRedirect(reverse('C3DB:substruct') + '?job=' + job.id)

    else:
        # Reset the Session
        query_session = SearchSession(request)
        query_stored = query_session.show()

        # If user get back to search ui during the job searchin, terminate the job.
        try:
            if query_stored['task_id']:
                app.control.revoke(str(query_stored['task_id']), terminate=True) # => This line only works on UINX type OS !!!
                query_session.clear()
                return HttpResponseRedirect(reverse('C3DB:substruct'))

        except KeyError as err:
            print err
            pass

        query_session.clear()

        form = SubstructSearchForm()
        categories = Category.objects.all()
        context = {
            'form': form,
            'categories': categories,
        }
        return render(request, 'search/substruct_search.html', context)

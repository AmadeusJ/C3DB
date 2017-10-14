# -*- coding: utf-8 -*-

from celery.result import AsyncResult
from C3DB.celery2 import *
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from .forms import FunctionalSearchForm
from index.models import Category
from .task import functional_search
from user_section.models import UserDataBase
from SearchSession.search import SearchSession


def functional_search_form(request):
    """ A view for functional search """
    user_db =None

    if 'job' in request.GET:
        job_id = request.GET['job']
#        print "This is the job_id [1]", job_id
#        print "This is the job_id [2]", job_id.id
        job = AsyncResult(job_id)
        data = job.result
        query_session = SearchSession(request)
        query_stored = query_session.show()
        form = FunctionalSearchForm()

        # Run when user is log-in
        if request.user.is_active:
            user_db = UserDataBase.objects.filter(user_id=request.user.id)

        context = {
            'data': data,
            'task_id': job_id,
            'query_smarts': query_stored['SmartsQuery'],
            'query_mf': query_stored['Formulaquery'],
            'query_mw': query_stored['MoleculeWeight'],
            'form': form,
            'user_db': user_db,
        }
        return render(request, 'result/functional_result_list.html', context)

    elif 'SmartsQuery' in request.GET:
        Smartsquery = request.GET['SmartsQuery']
        category = request.GET['Category']
        mw = request.GET['MW']
#        mw_max = request.GET['FMW_MAX']
        mw_max = u""
#        mw_min = request.GET['FMW_MIN']
        mw_min = u""
        Formularquery = request.GET['FMF']

        # Run task using query
        job = functional_search.delay(category, Smartsquery, mw, Formularquery)

        # Store query to session
        query_session = SearchSession(request)
        query_session.get_functioinal_search_query(job.id, Smartsquery, mw, Formularquery)

#        print "This is the job_id [3]", job.id
        return HttpResponseRedirect(reverse('chemdb:functional') + '?job=' + job.id)

    else:
        # Reset the Session
        query_session = SearchSession(request)
        query_stored = query_session.show()

        # If user get back to search ui during the job searchin, terminate the job.
        try:
            if query_stored['task_id']:
                app.control.revoke(str(query_stored['task_id']), terminate=True) # => This line only works on UINX type OS !!!
                query_session.clear()
                return HttpResponseRedirect(reverse('chemdb:functional'))

        except KeyError as err:
            print err
            pass

        query_session.clear()

        # Render input form
        form = FunctionalSearchForm()
        categories = Category.objects.all()

        context = {
            'form': form,
            'categories': categories,
        }
        return render(request, 'search/functional_search.html', context)


def kill_job(request):
    # Reset the Session
    try:
        query_session = SearchSession(request)
        query_stored = query_session.show()

        # If user get back to search ui during the job searchin, terminate the job.
        if query_stored['task_id']:
            app.control.revoke(str(query_stored['task_id']),
                                   terminate=True)  # => This line only works on UINX type OS !!!
            query_session.clear()

        query_session.clear()

    except KeyError as err:
        pass

    return HttpResponseRedirect(reverse('chemdb:functional'))

# -*- coding: utf-8 -*-

from django.shortcuts import render, redirect
from C3DB.celery2 import *
from celery.result import AsyncResult
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from .task import MassSearch
from .forms import MassSearchForm
from index.models import Category
from user_section.models import UserDataBase
from SearchSession.search import SearchSession


def MassSearch_form(request):
    """ A view for mass search """
    user_db = None

    if 'job' in request.GET:
        job_id = request.GET['job']
        job = AsyncResult(job_id)
        data = job.result
        query_session = SearchSession(request)
        query_stored = query_session.show()
        form = MassSearchForm()

        # Run when user is log-in
        if request.user.is_active:
            user_db = UserDataBase.objects.filter(user_id=request.user.id)

        context = {
            'data': data,
            'task_id': job_id,
            'query_mass': query_stored['mass'],
            'form': form,
            'user_db': user_db,
        }

        return render(request, 'result/mass_result_list.html', context)

    elif 'Mass' in request.GET:
        mass = request.GET['Mass']
        category = request.GET['Category']

        # Run task using query
        job = MassSearch.delay(category, mass)

        # Store query to session
        query_session = SearchSession(request)
        query_session.get_mass_search_query(job.id, mass)

        return HttpResponseRedirect(reverse('C3DB:mass') + '?job=' + job.id)

    else:
        query_session = SearchSession(request)
        query_stored = query_session.show()

        # If user get back to search ui during the job searchin, terminate the job.
        try:
            if query_stored['task_id']:
                app.control.revoke(str(query_stored['task_id']), terminate=True) # => This line only works on UINX type OS !!!
                query_session.clear()
                return HttpResponseRedirect(reverse('C3DB:mass'))

        except KeyError as err:
            print err
            pass

        query_session.clear()

        # Render input form
        form = MassSearchForm()
        categories = Category.objects.all()

        context = {
            'form': form,
            'categories': categories,
        }
        return render(request, 'search/mass_search.html', context)

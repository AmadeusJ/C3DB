# -*- coding: utf-8 -*-
from celery.result import AsyncResult
from C3DB.celery2 import *
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from .forms import ExactSearchForm
from index.models import Category
from .task import exact_search
from user_section.models import UserDataBase
from SearchSession.search import SearchSession

# Create your views here.


def exact_search_form(request):
    """ A view for exact search """

    if 'job' in request.GET:
        job_id = request.GET['job']
        job = AsyncResult(job_id)
        data = job.result
        query_session = SearchSession(request)
        query_stored = query_session.show()
        form = ExactSearchForm()
        # Run when user is log-in
        user_db = None
        if request.user.is_active:
            user_db = UserDataBase.objects.filter(user_id=request.user.id)

        context = {
            'data': data,
            'task_id': job_id,
            'form': form,
            'exact_query': query_stored['exact_query'],
            'user_db': user_db,
        }
        return render(request, 'result/exact_result_list.html', context)

    elif 'Exact_Search' in request.GET:
        query = request.GET['Exact_Search']
        category = request.GET['Category']
        job = exact_search.delay(category, query)

        # Store query to session
        query_session = SearchSession(request)
        query_session.get_exact_search_query(job.id, query)

        return HttpResponseRedirect(reverse('chemdb:exact') + '?job=' + job.id)

    else:
        # Reset the Session
        query_session = SearchSession(request)
        query_stored = query_session.show()

        # If user get back to search ui during the job searchin, terminate the job.
        try:
            if query_stored['task_id']:
                app.control.revoke(str(query_stored['task_id']), terminate=True) # => This line only works on UINX type OS !!!
                query_session.clear()
                return HttpResponseRedirect(reverse('chemdb:exact'))

        except KeyError as err:
            print err
            pass

        query_session.clear()

        # Render input form
        form = ExactSearchForm()
        categories = Category.objects.all()
        context = {
            'form': form,
            'categories': categories,
        }
        return render(request, 'search/exact_search.html', context)

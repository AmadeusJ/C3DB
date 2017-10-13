# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from C3DB.celery2 import *
from SearchSession.search import SearchSession
from django.http import HttpResponseRedirect


def index(request):
    """ Main index page. """
    a = None

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


    return render(request, 'index.html', {'a': a})

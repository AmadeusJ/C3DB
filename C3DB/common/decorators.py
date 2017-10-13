from django.http import HttpResponseBadRequest


def ajax_required(f):

    """ This is custorm 'ajax_required' decorator.

     It defines a wrap function that returns an 'HttpResponseBadRequest' object 

     (HTTP 400 code) if the request is not AJAX. """

    def wrap(request, *args, **kwargs):

        if not request.is_ajax():

            return HttpResponseBadRequest()

        return f(request, *args, **kwargs)

    wrap.__doc__ = f.__doc__

    wrap.__name__ = f.__name__

    return wrap

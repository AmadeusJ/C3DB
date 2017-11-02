# -*- coding: utf-8 -*-
from celery.result import AsyncResult
import json
from django.core.serializers.json import DjangoJSONEncoder
from django.http import HttpResponse
import platform


os = platform.system()
if os == 'Windows':
    conf_path = "C:\Users\JDW\Documents\GitHub\C3DB\C3DB\progress\C3DB_Result.conf"

elif os == 'Linux':
    conf_path = "/C3DB/GitHub/C3DB/C3DB/progress/C3DB_Result.conf"


def calling_result_configure():
    """  """
    result_conf = {}
    file = open(conf_path, 'r')
    for line in file:
        lines = line.strip().split()
        column = lines[1]
        value = int(lines[2])
        result_conf[column] = value

    file.close()
    return result_conf


def poll_state(request):
    """ A view to report the progress to the user. """
    data = None

    if request.is_ajax():
        if 'task_id' in request.POST.keys() and request.POST['task_id']:
            task_id = request.POST['task_id']
            task = AsyncResult(task_id)
            data = task.result or task.state

            if task.failed():
                print task.state

                json_data = json.dumps({'state': "ERROR"})
                return HttpResponse(json_data, content_type='application/json')

            elif task.successful():
                print task.state
                json_data = json.dumps({'data': data, 'state': "SUCCESS", 'configure': calling_result_configure()},
                                       cls=DjangoJSONEncoder)

                return HttpResponse(json_data, content_type='application/json')

        else:
            data = 'No task_id in the request'
            json_data = json.dumps(data, cls=DjangoJSONEncoder)

            return HttpResponse(json_data, content_type='application/json')

    else:
        data = 'This is not an ajax request'
        json_data = json.dumps(data, cls=DjangoJSONEncoder)

        return HttpResponse(json_data, content_type='application/json')

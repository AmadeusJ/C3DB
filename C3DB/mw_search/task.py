from celery import shared_task, current_task
from django.conf import settings
import time, re
import psycopg2


@shared_task
def MassSearch(category, mass):
    conn_string = settings.DB_CONNECTION_INFO
    conn = psycopg2.connect(conn_string)
    curs = conn.cursor()

    start_time = time.time()

    LIMIT = 100

    if mass is not u"":
        mass = float(mass)
        sql = """ SELECT * FROM mass ORDER BY abs(%.04f - "Py_MW") limit %d; """ % (mass, LIMIT)
        print sql
        curs.execute(sql)

    else:
        pass


    try:
        results = list(curs.fetchall())
#        print mol

    except Exception as err:
        print err
        results = []

    # Append results to be enable parsed by JS.
    process_percent = int(100 * len(results) / len(results))
    current_task.update_state(state='PROGRESS',
                                  meta={'process_percent': process_percent})

#    results.append(m)

    # Search time chenk.
    end_time = time.time() - start_time
    end_time = '%.02f' % end_time

    # Render variables to ajax calling(html page).
    context = {
        'result_mw_search': results,
        'time': end_time,
    }

    return context

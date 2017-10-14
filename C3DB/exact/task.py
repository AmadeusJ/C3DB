from celery import shared_task, current_task
from django.conf import settings
import re, time
import psycopg2


@shared_task
def exact_search(category, query):
    conn_string = settings.DB_CONNECTION_INFO
    conn = psycopg2.connect(conn_string)

    curs = conn.cursor()
    start_time = time.time()    # Check search time.

    cid = re.match(r'^[0-9]', query)
    inchi = re.match(r'InChI=', query)

    if cid:
        curs.execute('select * from "DB_Data" where "SSU_CID"=%s' % query)

    elif inchi:
        curs.execute("""select * from "DB_Data" where "MolInchi"='%s'""" % query)
        mol = list(curs.fetchall())

    else:
        curs.execute("""select * from "DB_Data" where "MolFormular"='%s' OR "MolSmiles"='%s' """ % (query, query))


    # Get the result as list to make as JSON format.
    try:
        mol = list(curs.fetchall())

    except Exception as err:
        print err
        mol = []


    # Append results to be enable parsed by JS.
    results = []

    # When there are result or results...
    if len(mol) >= 1:
        try:
            # When results are more than one...
            if len(mol) != 1:
                # When results return by 'LIMIT n' within SQL query...Result would be all same has the number of 'n'!
                # => This case actually result is only one... So distinguish!
                if mol[0] != mol[1]:
                    for m in mol:
                        process_percent = int(100 * len(results) / len(mol))
                        current_task.update_state(state='PROGRESS',
                                                  meta={'process_percent': process_percent})

                        results.append(m)
                else:
                    results.append(mol[0])

            # When result is only one...
            else:
                results.append(mol[0])

        except IndexError:
            pass

    # When there are no result...
    else:
        pass

    # Search time chenk.
    end_time = time.time() - start_time
    end_time = '%.02f' % end_time

    # Count results
    total_count = len(mol)

    if total_count >= 100:
        total_count = '100+'

    else:
        pass

    context = {
        'result_exact': results,
        'time': end_time,
        'Total_result': total_count
    }
    return context

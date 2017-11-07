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
    yachi = re.match(r'yaChI=', query)

    if cid:
        curs.execute("""SELECT db.*, mp.* FROM "DB_Data" AS db, "DB_Mopac_1" AS mp 
        WHERE "SSU_CID"=%s AND db."SSU_CID"=mp."SSU_CID";""" % query)

    elif inchi:
        curs.execute("""SELECT db.*, mp.*FROM "DB_Data" AS db, "DB_Mopac_1" AS mp 
        WHERE db."InChI"='%s' AND db."SSU_CID"=mp."SSU_CID"; """ % query)
        mol = list(curs.fetchall())

    elif yachi:
        curs.execute("""SELECT db.*, mp.*FROM "DB_Data" AS db, "DB_Mopac_1" AS mp 
        WHERE db."yaChI"='%s' AND db."SSU_CID"=mp."SSU_CID";""" % query)
        mol = list(curs.fetchall())

    else:
        curs.execute("""SELECT db.*,mp.* FROM "DB_Data" AS db, "DB_Mopac_1" AS mp WHERE 
        mp."SSU_CID" IN (SELECT db."SSU_CID" FROM "DB_Data" as db WHERE db."Formula"='%s' OR db."SMILES"='%s') 
        AND mp."SSU_CID"=db."SSU_CID" ORDER BY db."SSU_CID"; """ % (query, query))


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

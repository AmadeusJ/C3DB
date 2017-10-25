from celery import shared_task, current_task
from django.conf import settings
import re, time
import psycopg2
from rdkit import Chem


@shared_task
def substructure_search(category, super_sub, max_result, query, **kwargs):
    conn_string = settings.DB_CONNECTION_INFO
    conn = psycopg2.connect(conn_string)
    curs = conn.cursor()

    sql_where = """"""
    if kwargs[u'mw_min'] is not None:
        sql_where += """"RDKit_MW" >= %.f AND """ % float(kwargs[u'mw_min'])

    if kwargs[u'mw_max'] is not None:
        sql_where += """"RDKit_MW" <= %.f AND """ % float(kwargs[u'mw_min'])

    if kwargs[u'atom_min'] is not None:
        sql_where += """"AtomNumber" >= %d AND """ % int(kwargs[u'atom_min'])

    if kwargs[u'atom_max'] is not None:
        sql_where += """"AtomNumber" <= %d AND """ % int(kwargs[u'atom_max'])

    if kwargs[u'bond_min'] is not None:
        sql_where += """"BondNumber" >= %d AND """ % int(kwargs[u'bond_min'])

    if kwargs[u'bond_max'] is not None:
        sql_where += """"BondNumber" <= %d AND """ % int(kwargs[u'bond_max'])

    if kwargs[u'ring_min'] is not None:
        sql_where += """"RingNumber" >= %d AND """ % int(kwargs[u'ring_min'])

    if kwargs[u'ring_max'] is not None:
        sql_where += """"RingNumber" <= %d AND """ % int(kwargs[u'ring_max'])

    if kwargs[u'logP_min'] is not None:
        sql_where += """"LogP" >= %f AND """ % float(kwargs[u'logP_min'])

    if kwargs[u'logP_max'] is not None:
        sql_where += """"LogP" <= %f AND """ % float(kwargs[u'logP_max'])

    if kwargs[u'rotate_min'] is not None:
        sql_where += """"RotateBond" >= %d AND """ % int(kwargs[u'rotate_min'])

    if kwargs[u'rotate_max'] is not None:
        sql_where += """"RotateBond" <= %d AND """ % int(kwargs[u'rotate_max'])

    if kwargs[u'formal_min'] is not None:
        sql_where += """FormalCharge" >= %d AND """ % int(kwargs[u'formal_min'])

    if kwargs[u'formal_max'] is not None:
        sql_where += """"FormalCharge" <= %d AND """ % int(kwargs[u'formal_max'])

    if kwargs[u'hba_min'] is not None:
        sql_where += """"HBA" >= %d AND """ % int(kwargs[u'hba_min'])

    if kwargs[u'hba_max'] is not None:
        sql_where += """"HBA" <= %d AND """ % int(kwargs[u'hba_max'])

    if kwargs[u'hbd_min'] is not None:
        sql_where += """"HBD" >= %d AND """ % int(kwargs[u'hbd_min'])

    if kwargs[u'hbd_max'] is not None:
        sql_where += """"HBD" <= %d AND """ % int(kwargs[u'hbd_max'])

    if len(sql_where) != 0:
        sql_where = """AND """ + sql_where[:-5]
        #print sql_where

    inchi = re.match(r'^InChI=', query)

    if inchi:
        query_mol = Chem.MolFromInchi(query)
        query_mol = Chem.MolToSmiles(query_mol)

    else:
        query_mol = query

    results_limit = int(max_result)
    if max_result == u'':
        results_limit = None

    print results_limit

    start_time = time.time()

    sql = None
    if super_sub:
        if len(sql_where) == 0:
            if results_limit is None:
                sql = """ SELECT * from "DB_Data" db WHERE db.id 
                IN (SELECT mols.id FROM mols WHERE m<@'%s'); """ % query_mol
            else:
                sql = """ SELECT * from "DB_Data" db WHERE db.id 
                IN (SELECT mols.id FROM mols WHERE m<@'%s' LIMIT %d); """ % (query_mol, results_limit)

        else:
            if results_limit is None:
                sql = """ SELECT * from "DB_Data" db WHERE db.id 
                IN (SELECT mols.id FROM mols WHERE m<@'%s') %s;""" % (query_mol, sql_where)
            else:
                sql = """ SELECT * from "DB_Data" db WHERE db.id 
                IN (SELECT mols.id FROM mols WHERE m<@'%s' LIMIT %d) %s;""" % (query_mol, results_limit, sql_where)


    else:
        if len(sql_where) == 0:
            if results_limit is None:
                sql = """ SELECT * from "DB_Data" db WHERE db.id 
                IN (SELECT mols.id FROM mols WHERE m@>'%s'); """ % (query_mol)

            else:
                sql = """ SELECT * from "DB_Data" db WHERE db.id 
                IN (SELECT mols.id FROM mols WHERE m@>'%s' LIMIT %d); """ % (query_mol, results_limit)

        else:
            if results_limit is None:
                sql = """ SELECT * from "DB_Data" db WHERE db.id 
                IN (SELECT mols.id FROM mols WHERE m@>'%s') %s; """ % (query_mol, sql_where)
            else:
                sql = """ SELECT * from "DB_Data" db WHERE db.id 
                IN (SELECT mols.id FROM mols WHERE m@>'%s' LIMIT %d) %s; """ % (query_mol, results_limit, sql_where)

    print sql
    curs.execute(sql)

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

    end_time = time.time() - start_time
    end_time = '%.02f' % end_time

    # Count results
    total_count = len(mol)

    context = {
        'result_substruct' : results,
        'time': end_time,
        'Total_result': total_count
    }

    return context

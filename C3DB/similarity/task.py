from celery import shared_task, current_task
from django.conf import settings
import re, time
from rdkit import Chem
import psycopg2


@shared_task
def similar_search(category, fp_category, taminoto_min, max_result, query, exclude_atoms, **kwargs):
    conn_string = settings.DB_CONNECTION_INFO
    conn = psycopg2.connect(conn_string)
    curs = conn.cursor()
    mol = []

    sql_where = """"""
    if kwargs[u'mw_min'] is not None:
        sql_where += """db."RDKit_MW" >= %.f AND """ % float(kwargs[u'mw_min'])

    if kwargs[u'mw_max'] is not None:
        sql_where += """db."RDKit_MW" <= %.f AND """ % float(kwargs[u'mw_min'])

    if kwargs[u'atom_min'] is not None:
        sql_where += """db."AtomNumber" >= %d AND """ % int(kwargs[u'atom_min'])

    if kwargs[u'atom_max'] is not None:
        sql_where += """db."AtomNumber" <= %d AND """ % int(kwargs[u'atom_max'])

    if kwargs[u'bond_min'] is not None:
        sql_where += """db."BondNumber" >= %d AND """ % int(kwargs[u'bond_min'])

    if kwargs[u'bond_max'] is not None:
        sql_where += """db."BondNumber" <= %d AND """ % int(kwargs[u'bond_max'])

    if kwargs[u'ring_min'] is not None:
        sql_where += """db."RingNumber" >= %d AND """ % int(kwargs[u'ring_min'])

    if kwargs[u'ring_max'] is not None:
        sql_where += """db."RingNumber" <= %d AND """ % int(kwargs[u'ring_max'])

    if kwargs[u'logP_min'] is not None:
        sql_where += """db."LogP" >= %f AND """ % float(kwargs[u'logP_min'])

    if kwargs[u'logP_max'] is not None:
        sql_where += """db."LogP" <= %f AND """ % float(kwargs[u'logP_max'])

    if kwargs[u'rotate_min'] is not None:
        sql_where += """db."RotateBond" >= %d AND """ % int(kwargs[u'rotate_min'])

    if kwargs[u'rotate_max'] is not None:
        sql_where += """db."RotateBond" <= %d AND """ % int(kwargs[u'rotate_max'])

    if kwargs[u'formal_min'] is not None:
        sql_where += """db."FormalCharge" >= %d AND """ % int(kwargs[u'formal_min'])

    if kwargs[u'formal_max'] is not None:
        sql_where += """db."FormalCharge" <= %d AND """ % int(kwargs[u'formal_max'])

    if kwargs[u'hba_min'] is not None:
        sql_where += """db."HBA" >= %d AND """ % int(kwargs[u'hba_min'])

    if kwargs[u'hba_max'] is not None:
        sql_where += """db."HBA" <= %d AND """ % int(kwargs[u'hba_max'])

    if kwargs[u'hbd_min'] is not None:
        sql_where += """db."HBD" >= %d AND """ % int(kwargs[u'hbd_min'])

    if kwargs[u'hbd_max'] is not None:
        sql_where += """db."HBD" <= %d AND """ % int(kwargs[u'hbd_max'])

    if kwargs[u'cosmo_area_min'] is not None:
        sql_where += """mp."COSMO_Area" >= %f AND """ % float(kwargs[u'cosmo_area_min'])

    if kwargs[u'cosmo_area_max'] is not None:
        sql_where += """mp."COSMO_Area" =< %f AND """ % float(kwargs[u'cosmo_area_max'])

    if kwargs[u'cosmo_volume_min'] is not None:
        sql_where += """mp."COSMO_Volume" >= %f AND """ % float(kwargs[u'cosmo_volume_min'])

    if kwargs[u'cosmo_volume_max'] is not None:
        sql_where += """mp."COSMO_Volume" =< %f AND """ % float(kwargs[u'cosmo_volume_max'])

    if kwargs[u'dimensions_min'] is not None:
        sql_where += """mp."Dimensions" >= %f AND """ % float(kwargs[u'dimensions_min'])

    if kwargs[u'dimensions_max'] is not None:
        sql_where += """mp."Dimensions" <= %f AND """ % float(kwargs[u'dimensions_max'])

    if kwargs[u'elec_energy_min'] is not None:
        sql_where += """mp."Elec_Energy" >= %f AND """ % float(kwargs[u'elec_energy_min'])

    if kwargs[u'elec_energy_max'] is not None:
        sql_where += """mp."Elec_Energy" <= %f AND """ % float(kwargs[u'elec_energy_max'])

    if kwargs[u'homo_min'] is not None:
        sql_where += """mp."HOMO" >= %f AND """ % float(kwargs[u'homo_min'])

    if kwargs[u'homo_max'] is not None:
        sql_where += """mp."HOMO" <= %f AND """ % float(kwargs[u'homo_max'])

    if kwargs[u'lumo_min'] is not None:
        sql_where += """mp."LUMO" >= %f AND """ % float(kwargs[u'lumo_min'])

    if kwargs[u'lumo_max'] is not None:
        sql_where += """mp."LUMO" <= %f AND """ % float(kwargs[u'lumo_max'])

    if kwargs[u'total_energy_min'] is not None:
        sql_where += """mp."Total_Energy" >= %f AND """ % float(kwargs[u'total_energy_min'])

    if kwargs[u'total_energy_max'] is not None:
        sql_where += """mp."Total_Energy" <= %f AND """ % float(kwargs[u'total_energy_max'])


    if exclude_atoms is not u"":
        exclude_atoms_list = str(exclude_atoms).split(',')
        for atom in exclude_atoms_list:
            sql_where += """"MolFormular" NOT LIKE '%%%s%%' AND """ % atom

    if len(sql_where) != 0:
        sql_where = """WHERE """ + sql_where[:-5]
        # print sql_where

    inchi = re.match(r'^InChI=', query)
    taminoto_min = float(taminoto_min)
    results_limit = int(max_result)
    if max_result == u'':
        results_limit = None

    sql = None
    # MorganFP Search
    start_time = time.time()
    if fp_category == '1':
        if inchi:
            mediate_mol = Chem.MolFromInchi(query)
            query_mol = Chem.MolToSmiles(mediate_mol)

        else:
            query_mol = query

        if len(sql_where) == 0:
            if results_limit is None:
                # SQL Query for similarity search with morgan fingerprint.
                sql = """ SELECT db.*, mp.*, fps.similarity FROM "DB_Data" AS db, "DB_Mopac_1" as mp, 
                (SELECT db.id, similarity FROM "DB_Data" AS db INNER JOIN (SELECT * from get_mfp_neighbors('%s') 
                WHERE similarity >= %.1f) AS fps ON db.id=fps.id) as fps 
                WHERE fps.id=db.id AND db."SSU_CID"=mp."SSU_CID" ORDER BY db."SSU_CID"; """ % (query_mol, taminoto_min)
            else:
                # SQL Query for similarity search with morgan fingerprint.
                sql = """ SELECT db.*, mp.*, fps.similarity FROM "DB_Data" AS db, "DB_Mopac_1" as mp, 
                (SELECT db.id, similarity FROM "DB_Data" AS db INNER JOIN (SELECT * from get_mfp_neighbors('%s') 
                WHERE similarity >= %.1f LIMIT %d) AS fps ON db.id=fps.id) as fps 
                WHERE fps.id=db.id AND db."SSU_CID"=mp."SSU_CID" ORDER BY db."SSU_CID"; """ % (query_mol, taminoto_min, results_limit)

        else:
            if results_limit is None:
                sql = """ SELECT db.*, mp.*, fps.similarity FROM "DB_Data" AS db, "DB_Mopac_1" as mp, 
                (SELECT db.id, similarity FROM "DB_Data" AS db INNER JOIN (SELECT * from get_mfp_neighbors('%s') 
                WHERE similarity >= %.1f) AS fps ON db.id=fps.id) as fps 
                WHERE fps.id=db.id AND db."SSU_CID"=mp."SSU_CID" %s ORDER BY db."SSU_CID"; """ % (query_mol, taminoto_min, sql_where)

            else:
                sql = """ SELECT db.*, mp.*, fps.similarity FROM "DB_Data" AS db, "DB_Mopac_1" as mp, 
                (SELECT db.id, similarity FROM "DB_Data" AS db INNER JOIN (SELECT * from get_mfp_neighbors('%s') 
                WHERE similarity >= %.1f LIMIT %d) AS fps ON db.id=fps.id) as fps 
                WHERE fps.id=db.id AND db."SSU_CID"=mp."SSU_CID" %s ORDER BY db."SSU_CID"; """ % (query_mol, taminoto_min, results_limit, sql_where)

        print sql
        curs.execute(sql)

    else:
        pass

    try:
        mol = list(curs.fetchall())
    except Exception as err:
        print err
        mol = []

    # Append results to be enable parsed by JS.
    results = []
    if len(mol) >= 1:
        try:
            if len(mol) != 1:
                if mol[0] != mol[1]:
                    for m in mol:
                        process_percent = int(100 * len(results) / len(mol))
                        current_task.update_state(state='PROGRESS',
                                                  meta={'process_percent': process_percent})

                        results.append(m)
                else:
                    results.append(mol[0])

            else:
                results.append(mol[0])

        except IndexError:
            pass
    else:
        pass

    # Search time chenk.
    end_time = time.time() - start_time
    end_time = '%.02f' % end_time
    #    print "This is the end_time", end_time

    # Count results
    total_count = len(mol)

    # Render variables to ajax calling(html page).
    context = {
        'result_similarity': results,
        'time': end_time,
        'Total_result': total_count
    }

    return context

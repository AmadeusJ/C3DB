from celery import shared_task, current_task
from django.conf import settings
import time, re
import psycopg2

atoms = {'H': 1.0080, 'He': 4.0026, 'Li': 6.9400, 'Be': 9.0122, 'B': 10.8100, 'C': 12.0110, 'N': 14.0070, 'O': 15.9990,
         'F': 18.9984, 'Ne': 20.1797, 'Na': 22.9897, 'Mg': 24.3050, 'Al': 26.9815, 'Si': 28.085, 'P': 30.9737,
         'S': 32.0600, 'Cl': 35.4500, 'Ar': 39.9480, 'K': 39.0983, 'Ca': 40.0780, 'Sc': 44.9559, 'Ti': 47.8670,
         'V': 50.9415, 'Cr': 51.9961, 'Mn': 54.9380, 'Fe': 55.8450, 'Co': 58.9331, 'Ni': 58.6934, 'Cu': 63.5460,
         'Zn': 65.3800, 'Ga': 69.7230, 'Ge': 72.6300, 'As': 74.9216, 'Se': 78.9600, 'Br': 79.9600, 'Kr': 83.7980,
         'Rb': 85.4678, 'Sr': 87.6200, 'Y': 88.9058, 'Zr': 91.2240, 'Nb': 92.9064, 'Mo': 95.9600, 'Tc': 98.0000,
         'Ru': 101.0700, 'Rh': 102.9050, 'Pd': 106.4200, 'Ag': 107.8682, 'Cd': 112.4110, 'In': 114.8180, 'Sn': 118.7100,
         'Sb': 121.7600, 'Te': 127.6000, 'I': 126.9040, 'Xe': 131.2930, 'Cs': 132.9050, 'Ba': 137.3270, 'Hf': 178.4900,
         'Ta': 180.9470, 'W': 183.8400, 'Re': 186.2070, 'Os': 190.2300, 'Ir': 192.2170, 'Pt': 195.084, 'Au': 196.966,
         'Hg': 200.5900, 'Tl': 204.3800, 'Pb': 207.200, 'Bi': 208.9800, 'Po': 209.0000, 'At': 210.0000, 'Rn': 222.0000,
         'Fr': 223.0000, 'Ra': 226.0000, 'La': 138.9050, 'Ce': 140.1160, 'Pr': 140.9070, 'Nd': 144.2420, 'U': 238.0280}


# Calculate the "MW" from the molecule formula
def CalculateMW(molFormula):
    new = re.findall(r'[A-Z][a-z]?\d*|\([^()]*(?:\(.*\))?[^()]*\)\d+', molFormula)
    print new
    new2 = ''
    for i in new:
        if (len(i) == 1) and (i in atoms.keys()):
            i = i + '1'
        new2 += i
    # print new2

    Number = re.findall(r'[0-9]+', new2)
    Atoms = re.split(r'[0-9]+', new2)

    try:
        Atoms.remove('')  # Must activate when use in windows!!
    except ValueError:
        pass

    MW = 0
    for atom, number in zip(Atoms, Number):
        if atom in atoms.keys():
            atom_weight = int(number) * float(atoms[atom])
            MW = MW + atom_weight

    return round(MW, 4)


# Check the floating point from the number
def ApplyErrorRange(mw):
    mw = str(mw)
    num = re.findall(r'[-+]?\d*\.\d+|\d+', mw)
    prime = None
    error = 0

    for i in num:
        prime = re.findall(r'.\d+', i)

    mw = float(mw)
    if len(prime) > 1:
        if len(prime[1]) == 2:
            error = 0.1

        elif len(prime[1]) == 3:
            error = 0.01

        elif len(prime[1]) == 4:
            error = 0.001

        elif len(prime[1]) == 5:
            error = 0.0001
    else:
        error = 1

    mw_min = mw - error
    mw_max = mw + error

    mw = {'MAX': mw_max, 'MIN': mw_min}

    #    print "Error is : ", error
    #    print "Min is : ", mw_min
    #    print "Max is : ", mw_max

    return mw


@shared_task
def functional_search(category, query, mw, molFormula):
    conn_string = settings.DB_CONNECTION_INFO
    conn = psycopg2.connect(conn_string)
    curs = conn.cursor()

    start_time = time.time()

    LIMIT = 100  # DB Search limitation.

    if mw is not u"":
        mw_range = ApplyErrorRange(mw)

    # Case 1
    # When query has 'MF' and 'SMARTs query'
    if (molFormula is not u"") and (mw is u"") and (query is not u""):

        #        MW = CalculateMW(molFormula)

        sql = """ SELECT db.*, mp.* FROM "DB_Data" db, "DB_Mopac_1" mp 
         WHERE db.id IN (
         SELECT mols.id FROM mols WHERE mols.id IN (
         SELECT db.id FROM "DB_Data" db WHERE db."Formula"='%s' LIMIT %d) 
         AND m@>'%s'::qmol) AND db."SSU_CID"=mp."SSU_CID" ORDER BY db."SSU_CID"; """ % (molFormula, LIMIT, query)
        curs.execute(sql)

    # Case 2
    # When query has only 'MF'
    elif (molFormula is not u"") and (mw is u"") and (query is u""):
        sql = """ SELECT db.*, mp.* FROM "DB_Data" db, "DB_Mopac_1" mp 
        WHERE db."Formula"='%s' AND db."SSU_CID"=mp."SSU_CID" LIMIT %d; """ % (molFormula, LIMIT)
        curs.execute(sql)

    # Case 3
    # When query has 'MF', 'SMARTs query' and 'MW'
    elif (molFormula is not u"") and (mw is not u"") and (query is not u""):
        mw_min = mw_range['MIN']
        mw_max = mw_range['MAX']

        sql = """ SELECT db.*, mp.* FROM "DB_Data" db, "DB_Mopac_1" mp 
         WHERE db.id IN (
         SELECT mols.id FROM mols WHERE mols.id IN (
         SELECT db.id FROM "DB_Data" db WHERE db."Formula" LIKE '%%%s%%' AND db."RDKit_MW">='%.4f' AND db."RDKit_MW"<='%.4f' LIMIT %d)
         AND m@>'%s'::qmol) AND db."SSU_CID"=mp."SSU_CID" ORDER BY db."SSU_CID"; """ % (molFormula, mw_min, mw_max, LIMIT, query)
        #        print sql
        curs.execute(sql)

    # Case 4
    # When query has 'MF' and 'MW'
    elif (molFormula is not u"") and (mw is not u"") and (query is u""):
        mw_min = mw_range['MIN']
        mw_max = mw_range['MAX']
        sql = """ SELECT db.*, mp.* FROM "DB_Data" db, "DB_Mopac_1" mp 
        WHERE db."Formula" LIKE '%%%s%%' 
        AND db."RDKit_MW">='%.4f' 
        AND db."RDKit_MW"<='%.4f' AND db."SSU_CID"=mp."SSU_CID" LIMIT %d ORDER BY db."SSU_CID"; """ % (molFormula, mw_min, mw_max, LIMIT)
        #        print sql
        curs.execute(sql)

    # Case 5
    # When query has 'MW' and 'SMARTs query'
    elif (molFormula is u"") and (mw is not u"") and (query is not u""):
        mw_min = mw_range['MIN']
        mw_max = mw_range['MAX']

        sql = """ SELECT db.*, mp.* FROM "DB_Data" db, "DB_Mopac_1" mp 
         WHERE db.id IN (
         SELECT mols.id FROM mols WHERE mols.id IN (
         SELECT db.id FROM "DB_Data" db WHERE db."RDKit_MW">='%.4f' AND db."RDKit_MW"<='%.4f' LIMIT %d)
         AND m@>'%s'::qmol) AND db."SSU_CID"=mp."SSU_CID" ORDER BY db."SSU_CID"; """ % (mw_min, mw_max, LIMIT, query)
        curs.execute(sql)

    # Case 6
    # When query has only 'MW'
    elif (molFormula is u"") and (mw is not u"") and (query is u""):
        mw_min = mw_range['MIN']
        mw_max = mw_range['MAX']
        #        print "MW_MIN : ", mw_min
        #        print "MW_MAX : ", mw_max

        sql = """ SELECT db.*, mp.* FROM "DB_Data" db, "DB_Mopac_1" mp 
        WHERE db."RDKit_MW">='%.4f' 
        AND db."RDKit_MW"<='%.4f' AND db."SSU_CID"=mp."SSU_CID" LIMIT %d ORDER BY db."SSU_CID"; """ % (mw_min, mw_max, LIMIT)
        curs.execute(sql)

    try:
        mol = list(curs.fetchall())

    except Exception as e:
        print e
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

    if total_count >= 100:
        total_count = '100+'

    else:
        pass

    # Render variables to ajax calling(html page).
    context = {
        'result_functional': results,
        'time': end_time,
        'Total_result': total_count
    }

    return context

from django.conf import settings


class SearchSession(object):
    def __init__(self, request):
        """
        Initialize Search Session
        :param request: 
        """
        # Get 'request.session' object
        self.session = request.session
        # self.session_key = request.session.session_key

        search = self.session.get(settings.SEARCH_SESSION_ID)
        if not search:
            search = self.session[settings.SEARCH_SESSION_ID] = {}

        self.search = search

    def get_functioinal_search_query(self, task_id, SmartsQuery=None, mw=None, Formulaquery=None):
        """
        Get the query what users input to show during search-loading
        :param job:
        :param SmartsQuery: 
        :param mw_max: 
        :param mw_min: 
        :param Formulaquery: 
        :return: 
        """
        # search_id = task_id
        self.search['task_id'] = task_id

        # Case 1 => 'MF' and 'Smarts'
        if (SmartsQuery is not u"") and (Formulaquery is not u"") and (mw is u""):
            self.search['SmartsQuery'] = SmartsQuery
            self.search['Formulaquery'] = Formulaquery
            self.search['MoleculeWeight'] = 'None'

        # Case 2 => 'MF'
        elif (Formulaquery is not u"") and (SmartsQuery is u"") and (mw is u""):
            self.search['SmartsQuery'] = 'None'
            self.search['Formulaquery'] = Formulaquery
            self.search['MoleculeWeight'] = 'None'

        # Case 3 => 'MF' and 'Smarts' and 'MW'
        elif (SmartsQuery is not u"") and (mw is not u"") and (Formulaquery is not u""):
            self.search['SmartsQuery'] = SmartsQuery
            self.search['Formulaquery'] = Formulaquery
            self.search['MoleculeWeight'] = mw

        # Case 4 => 'MF' and 'MW'
        elif (Formulaquery is not u"") and (mw is not u"") and (SmartsQuery is u""):
            self.search['MoleculeWeight'] = mw
            self.search['Formulaquery'] = Formulaquery
            self.search['SmartsQuery'] = 'None'

        # Case 5 => 'MW' and 'Smarts'
        elif (SmartsQuery is not u"") and (mw is not u"") and (Formulaquery is u""):
            self.search['SmartsQuery'] = SmartsQuery
            self.search['Formulaquery'] = 'None'
            self.search['MoleculeWeight'] = mw

        # Case 6 => 'MW'
        elif (SmartsQuery is u"") and (mw is not u"") and (Formulaquery is u""):
            self.search['SmartsQuery'] = 'None'
            self.search['Formulaquery'] = 'None'
            self.search['MoleculeWeight'] = mw

    def get_exact_search_query(self, task_id, query=None):
        """
        Get the query what users input to show during search-loading
        :param task_id: 
        :param cid: 
        :param MolInchi: 
        :param MolSmiles: 
        :return: 
        """
        # search_id = task_id
        self.search['task_id'] = task_id
        self.search['exact_query'] = query
    """
        cid = re.match(r'^[0-9]', query)
        inchi = re.match(r'InChI=', query)


        # Case 1 => 'cid'
        if cid:
            self.search['exact_query'] = cid
            #self.search['MolInchi'] = 'None'
            #self.search['MolSmiles'] = 'None'

        # Case 2 => 'MolInchi'
        elif inchi:
            #self.search['cid'] = 'None'
            self.search['exact_query'] = inchi
            #self.search['MolSmiles'] = 'None'

        # Case 3 => 'MolSmiles'
        else:
            smiles = query
            #self.search['cid'] = 'None'
            #self.search['MolInchi'] = 'None'
            self.search['exact_query'] = smiles
    """

    def get_substruct_search_query(self, task_id, query=None):
        """
        Get the query what users input to show during search-loading
        :param task_id: 
        :param query: 
        :return: 
        """
        # search_id = task_id
        self.search['task_id'] = task_id
        self.search['substruct_query'] = query

    def get_similarity_search_query(self, task_id, query=None, tanimoto=None):
        """
        Get the query what users input to show during search-loading
        :param task_id: 
        :param query: 
        :return: 
        """
        self.search['task_id'] = task_id
        self.search['similarity_query'] = query
        self.search['tanimoto'] = tanimoto

    def get_mass_search_query(self, task_id, query=None):
        """ Get the query what users input to show during search-loading """
        self.search['task_id'] = task_id
        self.search['mass'] = query

    def show(self):
        """
        Show query on loading page.
        :return: 
        """
        return self.search

    def clear(self):
        """
        Remove query from session
        :return: 
        """
        del self.session[settings.SEARCH_SESSION_ID]
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf.urls import url
from django.contrib.auth.views import logout
from . import views
from exact.views import exact_search_form
from similarity.views import similar_search_form
from substruct.views import substruct_search_form
from functional.views import functional_search_form, kill_job
from mw_search.views import MassSearch_form
from user_section.views import user_db, user_db_create_ui, mol_show, mol_add, user_db_delete, mol_delete
from MolConverter.views import MolConversion, InChIFromMarvinJS, SmilesFromMarvinJS, YaChIFromMarvinJS
from mol_detail.views import result_detail, getMolFileContent, JMol3DViewer
from progress.views import poll_state


urlpatterns = [
    # == \ main page
    url(r'^$', views.index, name='index'),

    # ====== \ exact_search page
    url(r'^exact_search/$', exact_search_form, name='exact'),

    # =========== \ Similar_search page
    url(r'^similar_search/$', similar_search_form, name='similar'),

    # =============== \ Substruct_search page
    url(r'^substruct_search/$', substruct_search_form, name='substruct'),

    # ==================== \ Functional_search page
    url(r'^functional_search/$', functional_search_form, name='functional'),

    # ===================== \ Mass_search page
    url(r'^mass_search/$', MassSearch_form, name='mass'),



    # ======================== \ molecue detailed info page
    url(r'^result/(?P<SSU_CID>\d+)/$', result_detail, name='result_detail'),

    # JSMol Viewer
    url(r'^result_JSMol/(?P<SSU_CID>\d+)/$', JMol3DViewer, name='JMolViewer'),

    # ======================== \ Get molecule file content from server
    url(r'^result/molFileContent/$', getMolFileContent, name='mol_file'),



    # ============ \ Molconverter for MarvinJS
    url(r'^marvinJS/$', MolConversion, name='converter'),
    url(r'^marvinJSInchi/$', InChIFromMarvinJS, name='marvinToInchi'),
    url(r'^marvinJSSmiles/$', SmilesFromMarvinJS, name='marvinToSmiles'),
    url(r'^marvinJSYachi/$', YaChIFromMarvinJS, name='marvinToYachi'),



    # ================================= \ User section page
    # user_section main page.
    url(r'^user/user_db/$', user_db, name='user_db'),

    # user_db create form page.
    url(r'^user/user_db/create/$', user_db_create_ui, name='user_db_create'),

    # user_db delete
    url(r'^user/user_db/delete/$', user_db_delete, name='user_db_delete'),

    # mol_show
    url(r'^user/user_db/show/$', mol_show, name='mol_show'),

    # mol_add
    url(r'^user/user_db/add/$', mol_add, name='mol_add'),

    # mol_delete
    url(r'^user/user_db/mol_delete/$', mol_delete, name='mol_delete'),

    # - Django: user logout page
    url(r'^accounts/logout/$', logout, {'next_page': 'account/logout/'}, name='logout'),

    # --- Progress bar
    url(r'^progress/$', poll_state, name='poll'),

    # --- Kill job
    url(r'^kill_job/$', kill_job, name='kill_job'),

]


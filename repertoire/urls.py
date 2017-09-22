from django.conf.urls import include, url
from . import views

app_name = 'repertoire'

urlpatterns = [
    url(r'^$', views.ElementList.as_view(), name='list_oeuvres'),
    url(r'^zotero$', views.zotero_list, name='synchro_zotero'),
    url(r'new/$', views.ElementNew.as_view(), name='new_oeuvre'),
    url(r'^(?P<pk>.+)/$', views.ElementDisplay.as_view(), name='display_oeuvre'),
    url(r'^(?P<pk>.+)/edit$', views.ElementEdit.as_view(), name='edit_oeuvre'),
]

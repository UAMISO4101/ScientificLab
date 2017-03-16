from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^patrocinadores/$', views.patrocinadores, name='patrocinadores'),
    url(r'^patrocinadores/(?P<id>\d+)/$', views.patrocinadores_id, name='patrocinadorId'),
    url(r'^proyectos/$', views.proyectos, name='proyectos'),
    url(r'^proyectos/(?P<id>\d+)/$', views.proyectos_id, name='proyectoId'),

    url(r'^responsables/$', views.responsables, name='responsables'),
    url(r'^responsables/(?P<id>\d+)/$', views.responsables_id, name='responsableId'),
    url(r'^experimentos/$', views.experimentos, name='experimentos'),
    url(r'^experimentos/(?P<id>\d+)/$', views.experimentos_id, name='experimentoId'),
    url(r'^protocolos/$', views.protocolos, name='protocolos'),
    url(r'^protocolos/(?P<id>\d+)/$', views.protocolos_id, name='protocoloId'),
    url(r'^protocolosExperimento/$', views.protocolosExperimento, name='protocolosExperimento'),
    url(r'^protocolosExperimento/(?P<id>\d+)/$', views.protocolosExperimento_id, name='protocolosExperimentoId'),
    url(r'^pasos/$', views.pasos, name='pasos'),
    url(r'^pasos/(?P<id>\d+)/$', views.pasos_id, name='pasoId'),
    url(r'^elementos/$', views.elementos, name='elementos'),
    url(r'^elementos/(?P<id>\d+)/$', views.elementos_id, name='elementoId'),
]
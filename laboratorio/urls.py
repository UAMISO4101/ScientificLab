from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^agregarProyecto/$', views.agregar_proyecto, name='agregarProyecto'),
    url(r'^proyectos/$', views.mostrar_proyectos, name='listaProyectos'),

    #rest services
    url(r'^patrocinadores/$', views.patrocinadores, name='patrocinadores'),
    url(r'^patrocinadores/(?P<id>\d+)/$', views.patrocinadores_id, name='patrocinadorId'),
    url(r'^proyectos/$', views.proyectos, name='proyectos'),
    url(r'^proyectos/$', views.crear_proyecto, name='crearProyecto'),
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
    url(r'^elementos/(?P<id>\d+)/$', views.elementos_id, name='elementoId')

    url(r'^patrocinadores/(?P<id>\d+)/proyectos/$', views.patrocinadores_id_proyectos, name='patrocinadoresIdProyectos'),
    url(r'^proyectos/(?P<id>\d+)/experimentos/$', views.proyectos_id_experimentos, name='proyectosIdExperimentos'),
    url(r'^responsables/(?P<id>\d+)/experimentos/$', views.responsables_id_experimentos, name='responsablesIdExperimentos'),
    url(r'^experimentos/(?P<id>\d+)/protocolos/$', views.experimentos_id_protocolos, name='experimentosIdProtocolos'),
    url(r'^protocolos/(?P<id>\d+)/experimentos/$', views.protocolos_id_experimentos, name='protocolosIdExperimentos'),
    url(r'^protocolos/(?P<id>\d+)/pasos/$', views.protocolos_id_pasos, name='protocolosIdPasos'),
    url(r'^pasos/(?P<id>\d+)/elementos/$', views.pasos_id_elementos, name='pasosIdElementos'),

]
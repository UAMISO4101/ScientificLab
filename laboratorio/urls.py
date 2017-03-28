from django.conf.urls import url
from .views import  ProtocoloList
from . import views


urlpatterns = [
    url(r'^protocolofiltro/$', ProtocoloList.as_view(),name='ProtocoloFiltro'),
    url(r'^$', views.index, name='index'),
    url(r'^Proyecto/agregarProyecto/$', views.agregar_proyecto, name='agregarProyecto'),
    url(r'^Proyecto/editarProyecto/(?P<id>\d+)/$', views.editar_proyecto, name='editarProyecto'),
    url(r'^Experimento/agregarExperimento/$', views.agregar_experimento, name='agregarExperimento'),
    url(r'^Experimento/editarExperimento/(?P<id>\d+)/$', views.editar_experimento, name='editarExperimento'),
    url(r'^Proyecto/listarProyectos/$', views.listar_proyectos, name='listarProyectos'),
    url(r'^Experimento/listarExperimentos/$', views.listar_experimentos, name='listarExperimentos'),
    url(r'^Experimento/detallarExperimento/$', views.detallar_experimento, name='detallarExperimento'),

    url(r'^patrocinadores/$', views.patrocinadores, name='patrocinadores'),
    url(r'^patrocinadores/(?P<id>\d+)/$', views.patrocinadores_id, name='patrocinadorId'),
    url(r'^Proyecto/proyectos/$', views.proyectos, name='proyectos'),
    url(r'^Proyecto/proyectos/(?P<id>\d+)/$', views.proyectos_id, name='proyectoId'),

    url(r'^responsables/$', views.responsables, name='responsables'),
    url(r'^responsables/(?P<id>\d+)/$', views.responsables_id, name='responsableId'),
    url(r'^Experimento/experimentos/$', views.experimentos, name='experimentos'),
    url(r'^Experimento/experimentos/(?P<id>\d+)/$', views.experimentos_id, name='experimentoId'),
    url(r'^protocolos/$', views.protocolos, name='protocolos'),
    url(r'^Protocolo/listarProtocolos/$', views.listar_protocolos, name='listarProtocolos'),
    url(r'^protocolos/(?P<id>\d+)/$', views.protocolos_id, name='protocoloId'),
    url(r'^protocolosExperimento/$', views.protocolosExperimento, name='protocolosExperimento'),
    url(r'^protocolosExperimento/(?P<id>\d+)/$', views.protocolosExperimento_id, name='protocolosExperimentoId'),
    url(r'^pasos/$', views.pasos, name='pasos'),
    url(r'^pasos/(?P<id>\d+)/$', views.pasos_id, name='pasoId'),
    url(r'^elementos/$', views.elementos, name='elementos'),
    url(r'^elementos/(?P<id>\d+)/$', views.elementos_id, name='elementoId'),

    url(r'^patrocinadores/(?P<id>\d+)/proyectos/$', views.patrocinadores_id_proyectos, name='patrocinadoresIdProyectos'),
    url(r'^Proyecto/proyectos/(?P<id>\d+)/experimentos/$', views.proyectos_id_experimentos, name='proyectosIdExperimentos'),
    url(r'^responsables/(?P<id>\d+)/experimentos/$', views.responsables_id_experimentos, name='responsablesIdExperimentos'),
    url(r'^Experimento/experimentos/(?P<id>\d+)/protocolos/$', views.experimentos_id_protocolos, name='experimentosIdProtocolos'),
    url(r'^protocolos/(?P<id>\d+)/experimentos/$', views.protocolos_id_experimentos, name='protocolosIdExperimentos'),
    url(r'^protocolos/(?P<id>\d+)/pasos/$', views.protocolos_id_pasos, name='protocolosIdPasos'),
    url(r'^pasos/(?P<id>\d+)/elementos/$', views.pasos_id_elementos, name='pasosIdElementos'),

    url(r'^protocolos/(?P<id>\d+)/nuevaVersion/$', views.protocolos_id_nueva_version, name='protocoloIdNuevaVersion'),
    url(r'^listaEstadosProyecto/$', views.lista_estados_proyecto, name='listaEstadosProyecto'),
    url(r'^listaEstadosExperimento/$', views.lista_estados_experimento, name='listaEstadosExperimento'),
    url(r'^listaNombreProyectos/$', views.lista_nombre_proyecto, name='listaNombreProyectos'),

    url(r'^listaResultadosExperimento/$', views.lista_resultados_experimento, name='listaResultadosExperimento'),
    url(r'^listaCategoriasProtocolo/$', views.lista_categorias_protocolo, name='listaCategoriasProtocolo'),
    url(r'^listaUnidadesElemento/$', views.lista_unidades_elemento, name='listaUnidadesElemento'),
]
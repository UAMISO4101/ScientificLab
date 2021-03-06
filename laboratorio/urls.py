from django.conf.urls import url
from laboratorio.views import ProjectTraza, UsuariosProyecto, ProtocolosExperimentosProyecto, ExperimentosProyecto
from .views import ProtocoloList, ProyectosLista, ExperimentoLista, ProtocolosExperimentoLista, ProjectProgressList, UsuariosLista
from . import views


urlpatterns = [
    url(r'^protocolofiltro/$', ProtocoloList.as_view(),name='ProtocoloFiltro'),
    url(r'^$', views.index, name='index'),
    url(r'^Proyecto/agregarProyecto/$', views.agregar_proyecto, name='agregarProyecto'),
    url(r'^Proyecto/editarProyecto/(?P<id>\d+)/$', views.editar_proyecto, name='editarProyecto'),
    url(r'^Experimento/agregarExperimento/(?P<idProy>\d+)/$', views.agregar_experimento, name='agregarExperimento'),
    url(r'^Experimento/editarExperimento/(?P<idExp>\d+)/$', views.editar_experimento, name='editarExperimento'),
    url(r'^Proyecto/listarProyectos/$', views.listar_proyectos, name='listarProyectos'),
    url(r'^Proyecto/filtrarProyectos/$', ProyectosLista.as_view(), name='filtrarProyectos'),
    url(r'^Experimento/listarExperimentos/$', views.listar_experimentos, name='listarExperimentos'),
    url(r'^Experimento/filtrarExperimentos/$', ExperimentoLista.as_view(), name='filtrarExperimentos'),
    url(r'^Experimento/detallarExperimento/(?P<idExp>\d+)/$', views.detallar_experimento, name='detallarExperimento'),
    url(r'^Experimento/iniciarExperimento/(?P<id>\d+)/$', views.start_experiment, name='startExperiment'),

    url(r'^patrocinadores/$', views.patrocinadores, name='patrocinadores'),
    url(r'^patrocinadores/(?P<id>\d+)/$', views.patrocinadores_id, name='patrocinadorId'),
    url(r'^Proyecto/proyectos/$', views.proyectos, name='proyectos'),
    url(r'^Proyecto/proyectos/(?P<id>\d+)/$', views.proyectos_id, name='proyectoId'),

    url(r'^responsables/$', views.responsables, name='responsables'),
    url(r'^responsables/(?P<id>\d+)/$', views.responsables_id, name='responsableId'),
    url(r'^Experimento/experimentos/$', views.experimentos, name='experimentos'),

    url(r'^Proyecto/proyectos/(?P<id>\d+)/experimentos/$', views.proyectos_id_experimentos, name='proyectoListExperimentos'),
    url(r'^Proyecto/proyectos/(?P<id>\d+)/experimentos/$', views.listar_experimentos, name='proyectoIdExperimentos'),
    url(r'^Experimento/experimentos/(?P<idProy>\d+)/experimentos/$', views.listar_experimentos, name='listaExperimentos'),

    url(r'^Experimento/experimentos/(?P<id>\d+)/$', views.experimentos_id, name='experimentoId'),
    url(r'^protocolos/$', views.protocolos, name='protocolos'),
    url(r'^Protocolo/listarProtocolos/$', views.listar_protocolos, name='listarProtocolos'),
    url(r'^protocolos/(?P<id>\d+)/$', views.protocolos_id, name='protocoloId'),
    url(r'^protocolos/editar/(?P<id>\d+)/$', views.edit_protocol, name='editProtocol'),
    url(r'^protocolosExperimento/$', views.protocolosExperimento, name='protocolosExperimento'),
    url(r'^protocolosExperimento/(?P<id>\d+)/$', views.protocolosExperimento_id, name='protocolosExperimentoId'),
    url(r'^Protocolo/detallarProtocolo/(?P<id>\d+)/$', views.detallar_protocolo, name='detallarProtocolo'),
    url(r'^pasos/$', views.pasos, name='pasos'),
    url(r'^pasos/(?P<id>\d+)/$', views.pasos_id, name='pasoId'),
    url(r'^elementos/$', views.elementos, name='elementos'),
    url(r'^elementos/(?P<id>\d+)/$', views.elementos_id, name='elementoId'),
    url(r'^protocolosExperimento/filtrarProtocolosExperimento/$', ProtocolosExperimentoLista.as_view(), name='filtrarProtocolosExperimentos'),

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
    url(r'^Experimento/agregarExperimentoProtocolo/(?P<id>\d+)/$', views.agregar_expeprotocolo, name='agregarExperimentoProtocolo'),

    # Usuarios
    # URL paginas usuarios
    url(r'^agregarUsuario/$', views.agregar_usuario, name='agregarUsuario'),
    url(r'^login/$', views.inicio_sesion, name='login'),
    url(r'^usuarios/usuariosProyecto/(?P<id>\d+)/$', views.listar_usuariosProyecto, name='usuariosProyecto'),
    url(r'^usuarios/ListUserProject/', UsuariosLista.as_view(), name='listaUsuariosProy'),

    # URL servicios REST
    url(r'^usuarios/$', views.usuarios, name='usuarios'),
    url(r'^usuarios/(?P<id>\d+)/$', views.usuarios_id, name='usuarioId'),
    url(r'^iniciarSesion/$', views.iniciar_sesion, name='iniciarSesion'),
    url(r'^cerrarSesion/$', views.cerrar_sesion, name='cerrarSesion'),
    url(r'^estaLogueado/$', views.esta_logueado, name='estaLogueado'),

    #Project Progress
    url(r'^Proyecto/Avances/(?P<id>\d+)/$', views.list_progress, name='avance'),
    url(r'^Proyecto/AgregarAvance/(?P<id>\d+)/$', views.add_progress, name='agregarAvance'),
    url(r'^Proyecto/GuardarAvance/$', views.save_progress, name='guardarAvance'),
    url(r'^Proyecto/AvancesReportados/', ProjectProgressList.as_view(), name='avancesReportados'),

    #reports
    url(r'^Reportes/AvanceProyectos/', views.progress, name='reporteAvance'),
    url(r'^Reportes/trazabilidad/', views.trazabilidad, name='reporteTraza'),

    #Protocolos
    url(r'^agregarProtocolo/$', views.agregar_protocolo, name='agregarProtocolo'),

    #Trazabilidad
    url(r'^Proyecto/dataTraza/', UsuariosProyecto.as_view(), name='ProjectTraza'),
    url(r'^Proyecto/dataProto/', ProtocolosExperimentosProyecto.as_view(), name='ProjectProto'),
    url(r'^Proyecto/dataProto/', ExperimentosProyecto.as_view(), name='ProjectExpe'),

    #Deshabilitar protocolo
    url(r'^protocolos/(?P<id>\d+)/deshabilitar/$', views.protocolos_deshabilitar, name='protocoloIdDesahabilitar'),

]
from django.conf.urls import url

from . import views

#The wrong way to declare Django urls is to place the broader regular expressions first
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^patrocinadores/$', views.patrocinadores, name='patrocinadores'),
    url(r'^patrocinadores/(?P<id>\d+)/$', views.patrocinadores, name='patrocinadorId'),

]
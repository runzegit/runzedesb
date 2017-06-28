from django.conf.urls import url, include
from rest_framework import routers
from . import views

app_name = "clientes"
#router = routers.DefaultRouter()
#router.register(r'cliente', views.ClienteViewSet)

urlpatterns = [
	#url(r'^api/', include(router.urls)),
	url(r'^api/$', views.cliente_api, name="cliente_api"),
	url(r'^$', views.cliente_list, name="cliente_list"), 
	url(r'^desb/$', views.cliente_desb, name="cliente_desb"), 
	url(r'^busca/$', views.cliente_busca, name="cliente_busca"), 
	url(r'^desbbusca/$', views.cliente_desb_busca, name="cliente_desb_busca"), 		
	url(r'^bloqueado/$', views.cliente_bloqueado, name="cliente_bloqueado"), 
	url(r'^new/$', views.cliente_new, name="cliente_new"), 
	url(r'^(?P<pk>[0-9]+)/edit/$', views.cliente_edit, name="cliente_edit"), 
	url(r'^(?P<pk>[0-9]+)/delete/$', views.cliente_delete, name="cliente_delete"), 	
]
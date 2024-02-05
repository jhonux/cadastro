from django.urls import path
from . import views
# from .views import (ClienteList, ClienteCreate, ClienteUpdate, delete_veiculo)


urlpatterns = [
    # path('', views.clientes, name="clientes"),
    path('clientes/', views.clientes, name="inlineform_lista"),
    path('cadastrar/', views.cadastrar, name="cadastrar_clientes"),
    path('editar/<int:cliente_id>/', views.editar, name='inlineform_editar'),

    # path('criar_orcamento/', views.criar_orcamento, name='criar_orcamento'),
    # path('listar_orcamentos/', views.listar_orcamentos, name='listar_orcamentos'),
    # path('get_veiculos/<int:cliente_id>/', views.get_veiculos, name='get_veiculos'),

]

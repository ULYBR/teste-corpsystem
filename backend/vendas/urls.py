from django.urls import path
from .views import VendaViewSet

urlpatterns = [
    path('vendas/', VendaViewSet.as_view({'get': 'list', 'post': 'create'}), name='venda-list'),
    path('vendas/<int:pk>/', VendaViewSet.as_view({'get': 'retrieve'}), name='venda-detail'),
    path('relatorio/', VendaViewSet.as_view({'get': 'relatorio'}), name='venda-relatorio'),
    path('relatorio-pdf/', VendaViewSet.as_view({'get': 'relatorio_pdf'}), name='venda-relatorio-pdf'),
    path('listar-vendas/', VendaViewSet.as_view({'get': 'listar_vendas'}), name='listar-vendas'),  # Nova rota para JSON
]
